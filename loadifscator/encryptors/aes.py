from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os, base64

def aes_encrypt(input_file, key, output_file):
    key_bytes = key.encode().ljust(32, b'0')[:32]
    iv = os.urandom(16)
    with open(input_file, 'rb') as f:
        data = f.read()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(padded_data) + encryptor.finalize()
    b64_ct = base64.b64encode(iv + ct).decode()
    stub = f"""
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
key = '{key}'.encode().ljust(32, b'0')[:32]
data = base64.b64decode('{b64_ct}')
iv, ct = data[:16], data[16:]
cipher = AES.new(key, AES.MODE_CBC, iv)
pt = unpad(cipher.decrypt(ct), 16)
exec(pt.decode())
"""
    with open(output_file, 'w') as f:
        f.write(stub)
    print(f"[+] AES-encrypted payload written to {output_file}") 