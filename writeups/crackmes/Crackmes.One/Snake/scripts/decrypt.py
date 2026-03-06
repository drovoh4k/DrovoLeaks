#!/usr/bin/env python3

from Crypto.Cipher import ChaCha20

ciphertext = bytes.fromhex("F4B8C090CDF6CBF7C54230F375042C4BFD9D960257799A7AEE75D9F04C")

nxt=0
def srand (s):
    global nxt
    nxt = s & 0xffffffff

def rand():
    global nxt
    nxt = 0x41c64e6d * nxt + 0x3039 & 0xffffffff
    return (nxt >> 16) & 0x7fff

for seed in range(20000):
    key = bytearray(32)

    srand(seed)

    idx = 0
    for i in range(547):
        y = rand() % 18 + 1
        x = rand() % 38 + 1

        key[idx] = (key[idx] + x) & 0xff
        key[idx] = (key[idx] * y) & 0xff
        idx = (idx + 1) % 32

    cipher = ChaCha20.new(key=bytes(key), nonce=b"\00"*12)
    cipher.seek(0)
    plaintext = cipher.decrypt(ciphertext)

    if plaintext.startswith(b"brb{"):
        print(plaintext.decode())
        exit()