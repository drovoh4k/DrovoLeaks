from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key       = get_random_bytes(32)   # AES-256
plaintext = b"Texto en claro"

cipher                  = AES.new(key, AES.MODE_GCM)
nonce                   = cipher.nonce
ciphertext, tag         = cipher.encrypt_and_digest(plaintext)

decipher                = AES.new(key, AES.MODE_GCM, nonce=nonce)
plaintext_dec           = decipher.decrypt_and_verify(ciphertext, tag)

print(f"Key:        {key.hex()}")
print(f"Nonce:      {nonce.hex()}")
print(f"Tag:        {tag.hex()}")
print(f"Ciphertext: {ciphertext.hex()}")
print(f"Plaintext:  {plaintext_dec}")
