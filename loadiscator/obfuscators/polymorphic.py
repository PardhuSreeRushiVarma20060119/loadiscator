import random
import string
import re
from loadiscator.utils.random_name import random_name

def polymorphic_obfuscate(input_file, output_file):
    """Apply polymorphic obfuscation with junk code and variable renaming."""
    with open(input_file, 'r') as f:
        code = f.read()
    
    # Variable renaming
    var_mapping = {}
    
    def rename_var(match):
        var_name = match.group(1)
        if var_name not in var_mapping:
            var_mapping[var_name] = random_name()
        return var_mapping[var_name]
    
    # Rename variables (simple approach)
    code = re.sub(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=', rename_var, code)
    
    # Add junk code
    junk_code = generate_junk_code()
    
    # Add timing delays
    timing_code = generate_timing_code()
    
    # Combine all
    final_code = f"""# Polymorphic obfuscated payload
{timing_code}
{junk_code}
{code}
"""
    
    with open(output_file, 'w') as f:
        f.write(final_code)
    
    print(f"[+] Polymorphic obfuscated payload written to {output_file}")

def generate_junk_code():
    """Generate random junk code to confuse analysis."""
    junk_patterns = [
        f"{random_name()} = {random.randint(1, 1000)}",
        f"{random_name()} = '{random_name()}'",
        f"if {random.randint(0, 1)}: {random_name()} = {random.randint(1, 100)}",
        f"for {random_name()} in range({random.randint(1, 5)}): pass",
        f"try: {random_name()} = {random.randint(1, 100)} / {random.randint(1, 10)}\nexcept: pass"
    ]
    
    return "\n".join(random.sample(junk_patterns, random.randint(3, 6)))

def generate_timing_code():
    """Generate timing-based anti-analysis code."""
    return f"""
import time
import random
# Anti-analysis timing
time.sleep(random.uniform(0.1, 0.5))
""" 