from Crypto.Cipher import Salsa20
from Crypto.Random import get_random_bytes

key       = get_random_bytes(32)   # 256 bits
nonce     = get_random_bytes(8)    # 64 bits
plaintext = b"Texto en claro"

cipher                  = Salsa20.new(key=key, nonce=nonce)
ciphertext              = cipher.encrypt(plaintext)

decipher                = Salsa20.new(key=key, nonce=nonce)
plaintext_dec           = decipher.decrypt(ciphertext)

print(f"Key:        {key.hex()}")
print(f"Nonce:      {nonce.hex()}")
print(f"Ciphertext: {ciphertext.hex()}")
print(f"Plaintext:  {plaintext_dec}")
