# ADVERTENCIA: RC4 es criptográficamente inseguro. Solo para fines educativos.

from Crypto.Cipher import ARC4
from Crypto.Random import get_random_bytes

key       = get_random_bytes(16)   # 128 bits
plaintext = b"Texto en claro"

cipher                  = ARC4.new(key)
ciphertext              = cipher.encrypt(plaintext)

decipher                = ARC4.new(key)
plaintext_dec           = decipher.decrypt(ciphertext)

print(f"Key:        {key.hex()}")
print(f"Ciphertext: {ciphertext.hex()}")
print(f"Plaintext:  {plaintext_dec}")
