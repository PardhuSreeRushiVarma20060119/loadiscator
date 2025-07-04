import openai
import json
import os
from typing import Dict, List

class AIPayloadOptimizer:
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if self.api_key:
            openai.api_key = self.api_key
    
    def optimize_payload(self, payload: str, target_av: str = "generic") -> str:
        """Use AI to optimize payload for specific AV evasion."""
        if not self.api_key:
            return payload
        
        prompt = f"""
        Optimize this payload for {target_av} evasion:
        
        {payload}
        
        Apply these techniques:
        1. Variable renaming
        2. String obfuscation
        3. Control flow obfuscation
        4. Anti-analysis techniques
        5. Living-off-the-land techniques
        
        Return only the optimized code.
        """
        
        try:
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1000
            )
            return response.choices[0].message.content or payload
        except Exception as e:
            print(f"[!] AI optimization failed: {e}")
            return payload
    
    def generate_custom_payload(self, description: str, lang: str = "python") -> str:
        """Generate custom payload from natural language description."""
        if not self.api_key:
            return "# AI features require OpenAI API key"
        
        prompt = f"""
        Generate a {lang} payload based on this description:
        "{description}"
        
        Requirements:
        - Stealthy and evasive
        - Use living-off-the-land techniques
        - Include anti-analysis features
        - Minimal dependencies
        
        Return only the code.
        """
        
        try:
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1000
            )
            return response.choices[0].message.content or "# AI generation failed"
        except Exception as e:
            print(f"[!] AI generation failed: {e}")
            return "# AI generation failed"
    def suggest_evasion_techniques(self, payload: str) -> List[str]:
        """Get AI suggestions for evasion techniques."""
        if not self.api_key:
            return ["AI features require OpenAI API key"]
        
        prompt = f"""
        Analyze this payload and suggest 5 specific evasion techniques:
        
        {payload}
        
        Return as JSON array of strings.
        """
        
        try:
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500
            )
            suggestions = json.loads(response.choices[0].message.content or "[]")
            return suggestions
        except Exception as e:
            return [f"AI analysis failed: {e}"] 