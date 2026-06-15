# ADVERTENCIA: 3DES es criptográficamente débil. Solo para fines educativos.

from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key       = DES3.adjust_key_parity(get_random_bytes(24))  # 3 × 64 bits (168 bits efectivos)
plaintext = b"Texto en claro"

cipher                  = DES3.new(key, DES3.MODE_CBC)
iv                      = cipher.iv
ciphertext              = cipher.encrypt(pad(plaintext, DES3.block_size))

decipher                = DES3.new(key, DES3.MODE_CBC, iv)
plaintext_dec           = unpad(decipher.decrypt(ciphertext), DES3.block_size)

print(f"Key:        {key.hex()}")
print(f"IV:         {iv.hex()}")
print(f"Ciphertext: {ciphertext.hex()}")
print(f"Plaintext:  {plaintext_dec}")
