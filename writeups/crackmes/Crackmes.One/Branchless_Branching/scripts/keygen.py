#!/usr/bin/env python3

TABLA = "!@$defghijklmn9pqrstuvwxyz012345"

username = ("patataa" + "\n").encode() # 8 bytes

derived = [0] * 16

for i in range(8):

    idx1 = (i*7 + username[i]) & 0x1F
    derived[i] = ord(TABLA[idx1])

    idx2 = (derived[i] * username[i]) & 0x1F
    derived[i+8] = ord(TABLA[idx2])

password = "".join(chr(b + 1) for b in derived)

print(f"User: {username.decode()}Password: {password}")