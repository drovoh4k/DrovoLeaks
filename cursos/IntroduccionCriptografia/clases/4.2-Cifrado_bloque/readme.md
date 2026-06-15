# 🧑‍🏫 Criptografía simétrica: Cifrado en bloque

<!-- CHANNEL -->
[![YouTube](https://img.shields.io/badge/YouTube-@drovoh4k-DD0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/@drovoh4k)
[![Discord](https://img.shields.io/badge/Discord-DrovoHub-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.gg/kFrpheJkdN)

<!-- VIDEO META -->
[![tipo](https://img.shields.io/badge/tipo-curso%3A%3Aclase-111827?style=flat-square)]()
[![duración](https://img.shields.io/badge/duración-29%20min-111827?style=flat-square)]()


## 📄 Resumen

**📺 Clase:** https://youtu.be/HabsogvAvY8?list=PLKYfwBIKMkXdzMEfY64rQq-BLLubWVqm7

En esta clase vemos las bases del cifrado en bloque dentro de la criptografía simétrica, pero el objetivo real es entender los algoritmos por dentro. Primero explicamos qué significa trocear un mensaje en bloques de tamaño fijo, por qué aparece el problema del último bloque y para qué sirve el padding. A partir de ahí, analizamos a bajo nivel DES, 3DES y AES: cómo DES usa rondas Feistel, permutaciones, S-Boxes y key schedule; cómo 3DES intenta reforzar DES aplicándolo varias veces; y cómo AES organiza su estado interno, expande la clave y transforma los datos ronda a ronda hasta convertirse en el estándar moderno usado en TLS, VPNs, Wi-Fi y discos cifrados.


## 📦 Recursos

### Enlaces

1. **Fundamentos**
    - [Wikipedia: Cifrado simétrico](https://en.wikipedia.org/wiki/Symmetric-key_algorithm)
        - Explica los algoritmos de clave simétrica, en los que la misma clave se utiliza tanto para cifrar como para descifrar la información.

    - [Wikipedia: Cifrado por bloques](https://en.wikipedia.org/wiki/Block_cipher)
        - Introduce el concepto de cifrador de bloque, un tipo de algoritmo de cifrado simétrico que trabaja sobre bloques de tamaño fijo, transformando cada bloque de texto plano en un bloque de texto cifrado mediante una clave.

    - [Wikipedia: Red de Feistel](https://en.wikipedia.org/wiki/Feistel_cipher)
        - Explica la estructura de red de Feistel, utilizada en algoritmos como DES. Divide el bloque en dos mitades y aplica varias rondas de transformación para conseguir confusión y difusión.

    - [Wikipedia: Substitution–permutation network](https://en.wikipedia.org/wiki/Substitution%E2%80%93permutation_network)
        - Describe las redes de sustitución-permutación, una estructura criptográfica utilizada en cifradores modernos como AES para combinar sustituciones no lineales y permutaciones que aumentan la seguridad.



2. **DES**
    - [DES](https://en.wikipedia.org/wiki/Data_Encryption_Standard)
        - Describe DES, un cifrador de bloque simétrico basado en una red de Feistel. Fue un estándar ampliamente utilizado durante décadas, pero actualmente se considera inseguro por su tamaño de clave reducido.

    - [Wikipedia: DES supplementary material](https://en.wikipedia.org/wiki/DES_supplementary_material)
        - Recoge material complementario sobre DES, incluyendo tablas de permutación, cajas S y detalles internos del algoritmo. Es útil para estudiar con más detalle las operaciones que se aplican en cada ronda.

    - [NIST CSRC: FIPS 46-3 Data Encryption Standard](https://csrc.nist.gov/pubs/fips/46-3/final)
        - Página del NIST correspondiente a FIPS 46-3. Sirve para contextualizar el estado histórico de DES y su retirada como estándar seguro.

    - [NIST FIPS 46-3: Data Encryption Standard](https://csrc.nist.gov/files/pubs/fips/46-3/final/docs/fips46-3.pdf)
        - Publicación oficial del NIST sobre DES. Define el algoritmo DES y también incluye el uso de Triple DES como evolución del estándar original. Aunque está retirado, es una fuente primaria para estudiar cómo se especificaba formalmente DES.

3. **3DES**
    - [Wikipedia: 3DES](https://en.wikipedia.org/wiki/Triple_DES)
        - Explica Triple DES, una variante que aplica DES tres veces con distintas claves para aumentar la seguridad frente al DES original. Aunque fue una solución de transición importante, hoy se considera obsoleto frente a algoritmos modernos como AES.

    - [NIST SP 800-67 Rev. 2: Recommendation for the Triple Data Encryption Algorithm](https://csrc.nist.gov/pubs/sp/800/67/r2/final)
        - Recomendación del NIST dedicada a TDEA, también conocido como Triple DES. Describe formalmente el algoritmo, sus variantes de claves y su relación con el motor criptográfico original de DES.

    - [NIST SP 800-67 Rev. 2 PDF](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-67r2.pdf)
        - Versión en PDF de la recomendación del NIST sobre Triple DES. Es útil como referencia técnica completa para estudiar los detalles del algoritmo y sus restricciones de uso.

    - [RFC 3217: Triple-DES and RC2 Key Wrapping](https://datatracker.ietf.org/doc/html/rfc3217)
        - RFC que describe mecanismos de envoltura de claves usando Triple DES y RC2. Permite ver un uso práctico de 3DES dentro de protocolos y sistemas de gestión de claves.

4. **AES**
    - [AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)
        - Presenta AES, el estándar moderno de cifrado por bloques basado en el algoritmo Rijndael. Trabaja con bloques de 128 bits y claves de 128, 192 o 256 bits, y es ampliamente utilizado en comunicaciones seguras, almacenamiento cifrado y protocolos criptográficos actuales.

    - [AES key schedule](https://en.wikipedia.org/wiki/AES_key_schedule)
        - Explica el proceso de expansión de clave de AES, mediante el cual la clave original se transforma en múltiples subclaves utilizadas en las diferentes rondas del algoritmo.

    - [Rijndael S-box](https://en.wikipedia.org/wiki/Rijndael_S-box)
        - Describe la caja S de Rijndael, una transformación no lineal fundamental en AES. Su función es introducir confusión, dificultando la relación directa entre la clave, el texto plano y el texto cifrado.

    - [Rijndael MixColumns](https://en.wikipedia.org/wiki/Rijndael_MixColumns)
        - Explica la operación MixColumns de Rijndael, utilizada en AES para proporcionar difusión mezclando los bytes de cada columna del estado interno.

    - [NIST FIPS 197: Advanced Encryption Standard](https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.197.pdf)
        - Publicación oficial del NIST que define AES como estándar de cifrado. Es la fuente primaria para estudiar la estructura del algoritmo, sus tamaños de clave y sus transformaciones internas.

    - [NIST FIPS 197 actualización 2023](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf)
        - Versión actualizada de FIPS 197. Mantiene la especificación de AES, pero mejora la presentación y añade diagramas y aclaraciones editoriales que facilitan su estudio.

### Documentos

- [PPT_clase.pdf](resources/PPT_clase.pdf)
    - PDF con las slides de la presentación utilizada en el vídeo.

- [Pseudocódigos: DES, 3DES y AES](resources/pseudocodes/)
    - Pseudocódigos de los algoritmos explicados.

### Demos

- [Demos: DES.py, 3DES.py y AES.py](resources/demos/)
    - Demos en Python de los algoritmos explicados.
    - Requisitos:
        ```
        python3 -m venv .venv
        source .venv/bin/activate
        pip install -r requirements.txt
        ```

### Libros

- [Crypto101 by lvh (gratuito)](https://www.crypto101.io)
    - Es un libro introductorio de criptografía dirigido principalmente a programadores y profesionales de seguridad, disponible gratuitamente en formato web y PDF.

- [Serious Cryptography, 2nd Edition by Jean-Philippe Aumasson (≈ $50)](https://nostarch.com/serious-cryptography-2nd-edition)
    - Es una introducción práctica a la criptografía moderna, centrada en entender cómo funcionan realmente los algoritmos y sistemas criptográficos utilizados en la práctica.