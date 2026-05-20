#!/usr/bin/env python3

from pwn import rol

def generate_serials(n=10):
    serials = []

    for k1 in range(0xFFFF):
        if not (k1 & 0b10000000):   # bit 7 encendido
            continue

        k2 = k1 ^ 0xDEAD
        k3 = (0x1337 - k2) & 0xFFFF
        k4 = rol(k3, 4, 16)

        serials.append(f"{k1:04X}-{k2:04X}-{k3:04X}-{k4:04X}")

        if len(serials) == n:
            break

    return serials


if __name__ == "__main__":
    print(*generate_serials(10), sep="\n")
