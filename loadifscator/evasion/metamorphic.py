import random
import string
import re
import hashlib
from typing import Dict, List

class MetamorphicEngine:
    """Metamorphic engine for advanced code transformation."""
    
    def __init__(self):
        self.transformations = [
            self._add_junk_code,
            self._reorder_statements,
            self._change_control_flow,
            self._modify_strings,
            self._add_dead_code,
            self._change_variable_names
        ]
    
    def metamorphic_transform(self, code: str, iterations: int = 3) -> str:
        """Apply multiple metamorphic transformations."""
        transformed_code = code
        
        for i in range(iterations):
            # Randomly select transformations
            selected_transforms = random.sample(
                self.transformations, 
                random.randint(2, len(self.transformations))
            )
            
            for transform in selected_transforms:
                transformed_code = transform(transformed_code)
        
        return transformed_code
    
    def _add_junk_code(self, code: str) -> str:
        """Add junk code blocks."""
        junk_patterns = [
            f"if {random.randint(0, 1)}: {random_name()} = {random.randint(1, 100)}",
            f"for {random_name()} in range({random.randint(1, 5)}): pass",
            f"try: {random_name()} = {random.randint(1, 100)} / {random.randint(1, 10)}\nexcept: pass",
            f"{random_name()} = lambda x: x + {random.randint(1, 10)}",
            f"class {random_name()}: pass"
        ]
        
        lines = code.split('\n')
        insert_pos = random.randint(0, len(lines))
        junk_lines = random.sample(junk_patterns, random.randint(1, 3))
        
        lines.insert(insert_pos, '\n'.join(junk_lines))
        return '\n'.join(lines)
    
    def _reorder_statements(self, code: str) -> str:
        """Reorder non-dependent statements."""
        lines = code.split('\n')
        
        # Find independent statement blocks
        blocks = []
        current_block = []
        
        for line in lines:
            if line.strip().startswith(('import', 'from', 'class', 'def')):
                if current_block:
                    blocks.append(current_block)
                    current_block = []
            current_block.append(line)
        
        if current_block:
            blocks.append(current_block)
        
        # Shuffle blocks that can be reordered
        if len(blocks) > 1:
            # Keep imports at top, shuffle others
            imports = blocks[0] if blocks[0][0].strip().startswith(('import', 'from')) else []
            others = blocks[1:] if imports else blocks
            
            random.shuffle(others)
            blocks = [imports] + others if imports else others
        
        return '\n'.join(['\n'.join(block) for block in blocks])
    
    def _change_control_flow(self, code: str) -> str:
        """Modify control flow structures."""
        # Replace if-else with ternary
        code = re.sub(
            r'if\s+(\w+):\s*\n\s*(\w+)\s*=\s*(\w+)\s*\n\s*else:\s*\n\s*(\w+)\s*=\s*(\w+)',
            r'\2 = \3 if \1 else \5',
            code
        )
        
        # Add unnecessary conditions
        code = re.sub(
            r'(\w+)\s*=\s*(\w+)',
            lambda m: f'{m.group(1)} = {m.group(2)} if True else {m.group(2)}',
            code
        )
        
        return code
    
    def _modify_strings(self, code: str) -> str:
        """Modify string literals."""
        def modify_string(match):
            original = match.group(0)
            content = original[1:-1]
            
            if len(content) < 3:
                return original
            
            # Random string modification
            technique = random.choice(['split', 'encode', 'reverse'])
            
            if technique == 'split':
                parts = []
                while content:
                    split_point = random.randint(1, min(3, len(content)))
                    parts.append(f"'{content[:split_point]}'")
                    content = content[split_point:]
                return " + ".join(parts)
            
            elif technique == 'encode':
                encoded = content.encode('rot13') if hasattr(str, 'encode') else content
                return f"'{encoded}'.encode('rot13').decode()"
            
            elif technique == 'reverse':
                return f"'{content}'[::-1][::-1]"
            
            return original
        
        return re.sub(r'"[^"]*"|\'[^\']*\'', modify_string, code)
    
    def _add_dead_code(self, code: str) -> str:
        """Add dead code paths."""
        dead_code = f"""
# Dead code block
{random_name()} = {random.randint(1, 100)}
if {random_name()} > 1000:
    {random_name()} = {random.randint(1, 100)}
    {random_name()} = {random.randint(1, 100)}
"""
        
        lines = code.split('\n')
        insert_pos = random.randint(0, len(lines))
        lines.insert(insert_pos, dead_code)
        
        return '\n'.join(lines)
    
    def _change_variable_names(self, code: str) -> str:
        """Change variable names randomly."""
        var_mapping = {}
        
        def rename_var(match):
            var_name = match.group(1)
            if var_name not in var_mapping:
                var_mapping[var_name] = random_name()
            return var_mapping[var_name]
        
        # Rename variables (simple approach)
        return re.sub(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=', rename_var, code)
    
    def generate_unique_build(self, code: str) -> str:
        """Generate a unique build with metamorphic transformations."""
        # Add build-specific modifications
        build_id = hashlib.md5(code.encode()).hexdigest()[:8]
        
        # Apply metamorphic transformations
        transformed = self.metamorphic_transform(code)
        
        # Add build identifier
        header = f"# Build ID: {build_id}\n# Metamorphic transformation applied\n"
        
        return header + transformed

def random_name(length: int = 8) -> str:
    """Generate random variable name."""
    return ''.join(random.choices(string.ascii_letters, k=length)) 