import random
import string
import re

def string_mangle(input_file, output_file):
    """Mangle strings in the code to make them harder to detect."""
    with open(input_file, 'r') as f:
        code = f.read()
    
    # Find all string literals
    string_pattern = r'"[^"]*"|\'[^\']*\''
    
    def mangle_string(match):
        original = match.group(0)
        content = original[1:-1]  # Remove quotes
        
        if len(content) < 3:
            return original
        
        # Randomly choose mangling technique
        technique = random.choice(['split', 'case', 'concat', 'hex'])
        
        if technique == 'split':
            # Split string into parts
            parts = []
            while content:
                split_point = random.randint(1, min(3, len(content)))
                parts.append(f"'{content[:split_point]}'")
                content = content[split_point:]
            return " + ".join(parts)
        
        elif technique == 'case':
            # Random case changes
            mangled = ''.join(c.upper() if random.choice([True, False]) else c.lower() for c in content)
            return f"'{mangled}'.lower()" if mangled.isupper() else f"'{mangled}'.upper()"
        
        elif technique == 'concat':
            # Add random characters and remove them
            chars = ''.join(random.choices(string.ascii_letters, k=random.randint(2, 5)))
            return f"('{chars}' + '{content}' + '{chars}')[{len(chars)}:-{len(chars)}]"
        
        elif technique == 'hex':
            # Convert to hex and back
            hex_str = ''.join(f'\\x{ord(c):02x}' for c in content)
            return f"'{hex_str}'.encode('latin1').decode('unicode_escape')"
        
        return original
    
    mangled_code = re.sub(string_pattern, mangle_string, code)
    
    with open(output_file, 'w') as f:
        f.write(mangled_code)
    
    print(f"[+] String mangled payload written to {output_file}") 