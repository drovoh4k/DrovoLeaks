#!/usr/bin/env python3

from sympy import mod_inverse

n = 3233
e = 17
encrypted = [3000, 529, 2310, 855, 2412, 1230, 1632, 119, 281, 2185, 2235, 119, 612, 2412, 3179, 2271, 2185, 1230, 119, 612, 1313, 1627, 2160, 1313, 2235, 2185, 1230, 119, 1313, 1230, 119, 3179, 2235, 1230, 1313, 2923, 2160, 2412, 2185, 1516]


# Factorización de n
p, q = factorint(n).keys()

# Phi de Eulerla
phi = (p - 1) * (q - 1)

# Clave privada d
d = mod_inverse(e, phi)


# Desencriptar
decrypted = [pow(c, d, n) for c in encrypted]

# Convertir a texto
message = ''.join(chr(m) for m in decrypted)

print("Clave_privada =", d)
print("Mensaje desencriptado:", message)
