# ADVERTENCIA: DES es criptográficamente inseguro. Solo para fines educativos.

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key       = get_random_bytes(8)    # 64 bits (56 bits efectivos)
plaintext = b"Texto en claro"

cipher                  = DES.new(key, DES.MODE_CBC)
iv                      = cipher.iv
ciphertext              = cipher.encrypt(pad(plaintext, DES.block_size))

decipher                = DES.new(key, DES.MODE_CBC, iv)
plaintext_dec           = unpad(decipher.decrypt(ciphertext), DES.block_size)

print(f"Key:        {key.hex()}")
print(f"IV:         {iv.hex()}")
print(f"Ciphertext: {ciphertext.hex()}")
print(f"Plaintext:  {plaintext_dec}")
