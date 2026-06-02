from Crypto.Cipher import ChaCha20_Poly1305
from Crypto.Random import get_random_bytes

key       = get_random_bytes(32)   # 256 bits
nonce     = get_random_bytes(12)   # 96 bits
plaintext = b"Texto en claro"

cipher                  = ChaCha20_Poly1305.new(key=key, nonce=nonce)
ciphertext, tag         = cipher.encrypt_and_digest(plaintext)

decipher                = ChaCha20_Poly1305.new(key=key, nonce=nonce)
plaintext_dec           = decipher.decrypt_and_verify(ciphertext, tag)

print(f"Key:        {key.hex()}")
print(f"Nonce:      {nonce.hex()}")
print(f"Tag:        {tag.hex()}")
print(f"Ciphertext: {ciphertext.hex()}")
print(f"Plaintext:  {plaintext_dec}")
