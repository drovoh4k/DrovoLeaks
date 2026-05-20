# 🧑‍🏫 Criptografía clásica

<!-- CHANNEL -->
[![YouTube](https://img.shields.io/badge/YouTube-@drovoh4k-DD0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/@drovoh4k)
[![Discord](https://img.shields.io/badge/Discord-DrovoHub-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.gg/kFrpheJkdN)

<!-- VIDEO META -->
[![tipo](https://img.shields.io/badge/tipo-curso%3A%3Aclase-111827?style=flat-square)]()
[![duración](https://img.shields.io/badge/duración-18%20min-111827?style=flat-square)]()


## 📄 Resumen

**📺 Clase:** https://youtu.be/c6PDx-LqvTU?list=PLKYfwBIKMkXdzMEfY64rQq-BLLubWVqm7

En esta clase introducimos la criptografía clásica, viendo los primeros sistemas de cifrado, los tipos básicos como sustitución y transposición, cómo funcionan cifrados como César y Vigenère, y por qué estos sistemas terminan siendo vulnerables a distintos tipos de ataques.


## 📦 Recursos

### Enlaces

1. **Fundamentos**
    - [Wikipedia: Criptografía clásica](https://en.wikipedia.org/wiki/Classical_cipher)
        - Introduce los cifrados clásicos utilizados antes de la criptografía moderna, basados en transformaciones manuales como sustitución y transposición.
    - [Wikipedia: Cifrado substitución](https://en.wikipedia.org/wiki/Substitution_cipher)
        - Describe los cifrados de sustitución, donde cada símbolo del mensaje se reemplaza por otro siguiendo una regla determinada.
    - [Wikipedia: Cifrado transposición](https://en.wikipedia.org/wiki/Transposition_cipher)
        - Explica los cifrados de transposición, en los que las letras del mensaje se reordenan sin cambiar su identidad.
    - [Inventive HQ: Classical Ciphers Explained - From Caesar to Enigma](https://inventivehq.com/blog/classical-ciphers-explained-caesar-to-enigma)
        - Explica los cifrados clásicos desde sustitución hasta sistemas más complejos, mostrando cómo evolucionaron y por qué eran vulnerables.


2. **Cifrado César**
    - [Wikipedia: Cifrado César](https://en.wikipedia.org/wiki/Caesar_cipher)
        - Cifrado por sustitución donde cada letra se desplaza un número fijo de posiciones en el alfabeto.
    - [Wikipedia: Key Space](https://en.wikipedia.org/wiki/Key_space_(cryptography))
        - Define el espacio de claves como el conjunto de todas las claves posibles que puede usar un sistema criptográfico, y explica por qué su tamaño determina la resistencia frente a ataques por fuerza bruta.
    - [CesarCipher.org: Caesar Cipher Tutorial -  Complete Beginner's Guide with Examples](https://caesarcipher.org/learn/caesar-cipher-tutorial-complete-beginners-guide-with-examples)
        - Tutorial completo del cifrado César con ejemplos, implementación y explicación de por qué es vulnerable a fuerza bruta.


3. **Cifrado Vigenère**
    - [Wikipedia: Cifrado Vigenère](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)
        - Cifrado polialfabético que usa múltiples desplazamientos controlados por una clave.
    - [Wikipedia: Análisis Frecuencias](https://en.wikipedia.org/wiki/Frequency_analysis)
        - Técnica usada para romper cifrados detectando patrones estadísticos del lenguaje.
    - [Wikipedia: Método de Kasiski](https://en.wikipedia.org/wiki/Kasiski_examination)
        - Usado para estimar la longitud de la clave en cifrados polialfabéticos.
    - [Wikipedia: Índice de Coincidencia](https://en.wikipedia.org/wiki/Index_of_coincidence)
        - Medida estadística usada para detectar periodicidad en textos cifrados.
    - [Blog of Osanda: Breaking the Vigenère Cipher](https://osandamalith.com/2015/05/02/breaking-the-vigenere-cipher)
        - Explica cómo romper el cifrado Vigenère y por qué la repetición de la clave introduce vulnerabilidades.

### Libros
- [Crypto101 by lvh (gratuito)](https://www.crypto101.io)
    - Es un libro introductorio de criptografía dirigido principalmente a programadores y profesionales de seguridad, disponible gratuitamente en formato web y PDF.
- [Serious Cryptography, 2nd Edition by Jean-Philippe Aumasson (≈ $50)](https://nostarch.com/serious-cryptography-2nd-edition)
    - Es una introducción práctica a la criptografía moderna, centrada en entender cómo funcionan realmente los algoritmos y sistemas criptográficos utilizados en la práctica.

### Demos

- Demo del cifrado César
    - [demos/demo_cesar.PY](demos/demo_cesar.py)

- Demo del cifrado Vigenère
    - [demos/demo_vigenere.PY](demos/demo_vigenere.py)