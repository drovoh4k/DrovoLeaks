#!/usr/bin/env python3

from pwn import xor

encrypted_hex = bytes.fromhex("107b072337622a10206b3f612c7e3668103c6810376d10216b28272a7f2f")

known_prefix = b"H4U{"

# Recuperamos fragmento de clave
key_fragment = xor(encrypted_hex[:len(known_prefix)], known_prefix)
print("Fragmento clave:", key_fragment.decode())

# Buscamos la clave mínima que se repite
for length in range(1, len(key_fragment) + 1):
    key = key_fragment[:length]
    generated = (key * len(key_fragment))[:len(key_fragment)]
    
    print(f"\nProbando longitud = {length}")
    print(f"Clave candidata: '{key}'")
    print(f"Cadena generada repitiendo key: '{generated}'")
    print(f"¿Coincide con key_fragment? {generated == key_fragment}")
    
    if generated == key_fragment:
        break

# Desciframos todo
flag = xor(encrypted_hex, key)
print("Flag:", flag.decode())