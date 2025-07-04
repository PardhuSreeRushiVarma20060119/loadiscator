def xor_obfuscate(input_file, key, output_file):
    key_bytes = bytes.fromhex(key.replace('0x','')) if key.startswith('0x') else key.encode()
    with open(input_file, 'rb') as f:
        data = f.read()
    xored = bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(data)])
    stub = f"""
key = {list(key_bytes)}
data = {list(xored)}
import sys
sys.stdout = open(1, 'w')
exec(bytes([b ^ key[i % len(key)] for i, b in enumerate(data)]).decode())
"""
    with open(output_file, 'w') as f:
        f.write(stub)
    print(f"[+] XOR obfuscated payload written to {output_file}") 