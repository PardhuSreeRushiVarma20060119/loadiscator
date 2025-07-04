import base64

def base64_obfuscate(input_file, output_file):
    with open(input_file, 'r') as f:
        code = f.read()
    encoded = base64.b64encode(code.encode()).decode()
    stub = f"""
import base64
exec(base64.b64decode('{encoded}').decode())
"""
    with open(output_file, 'w') as f:
        f.write(stub)
    print(f"[+] Base64 obfuscated payload written to {output_file}") 