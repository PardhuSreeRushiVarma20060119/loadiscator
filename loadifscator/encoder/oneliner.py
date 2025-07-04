import base64

def generate_oneliner(input_file, lang):
    with open(input_file, 'r') as f:
        code = f.read()
    b64 = base64.b64encode(code.encode()).decode()
    if lang == 'python':
        print(f"python -c \"import base64;exec(base64.b64decode('{b64}'))\"")
    elif lang == 'bash':
        print(f"bash -c \"echo {b64} | base64 -d | bash\"")
    elif lang == 'powershell':
        ps_b64 = base64.b64encode(code.encode('utf-16le')).decode()
        print(f"powershell -enc {ps_b64}")
    else:
        print('Language not supported for one-liner.') 