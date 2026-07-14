<!-- drovoleaks-banner:start -->
<a href="https://drovoleaks.re/">
  <picture>
    <source media="(max-width: 768px)" srcset="https://raw.githubusercontent.com/drovoh4k/DrovoLeaks/main/.github/banner-archivado-movil.svg">
    <img src="https://raw.githubusercontent.com/drovoh4k/DrovoLeaks/main/.github/banner-archivado.svg" alt="Este repositorio ya no se actualiza — contenido movido a drovoleaks.re" width="100%">
  </picture>
</a>
<!-- drovoleaks-banner:end -->

# Snake

[![YouTube](https://img.shields.io/badge/YouTube-@drovoh4k-DD0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/@drovoh4k)
[![Discord](https://img.shields.io/badge/Discord-DrovoHub-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.gg/kFrpheJkdN)

[![tipo](https://img.shields.io/badge/tipo-writeup::crackme-111827?style=flat-square)]()
[![fuente](https://img.shields.io/badge/fuente-crackmes.one-111827?style=flat-square)]()

[![categoria](https://img.shields.io/badge/categoria-Reversing-0969da?style=flat-square)]()
[![dificultad](https://img.shields.io/badge/dificultad-Media-de7d00?style=flat-square)]()

[![arquitectura](https://img.shields.io/badge/arquitectura-x86--64-8250df?style=flat-square)]()
[![plataforma](https://img.shields.io/badge/plataforma-Unix%2FLinux%20etc.-8250df?style=flat-square)]()
[![lenguaje](https://img.shields.io/badge/lenguaje-C%2FC%2B%2B-8250df?style=flat-square)]()

| Links | |
|---|---|
| 🧩 Source | https://crackmes.one/crackme/64f1f7afd931496abf909525 |
| 🪞 Mirror | [challenge/snake.zip](challenge/snake.zip) - Password: `crackmes.one` |
| 🎥 WriteUp | https://youtu.be/U5wPKmfl6TM |


## 📦 Recursos

### Enlaces

1. **Documentación técnica**
    - [FelixCloutier: x86 and amd64 instruction reference](https://www.felixcloutier.com/x86)
        - Referencia rápida para consultar instrucciones assembly.
        - Aunque para la resolución de los challenges de este repositorio es más que suficiente, es solo para tener una referencia.
        - Para cualquier proyecto serio, consultar documentación oficial como, por ejemplo, el [Intel® 64 and IA-32 Architectures Software Developer Manuals](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html).

    - [Libreria de Pycryptodome - Chacha20](https://pycryptodome.readthedocs.io/en/latest/src/cipher/chacha20.html)
        - Documentación oficial de la libreria Chacha20.
        - Permite utilizar este cifrado simétrico en Python para proteger datos mediante operaciones de cifrado y descifrado, gestionando claves, nonces y flujo de bytes de forma sencilla.

2. **De apoyo**
    - [UPX: the Ultimate Packer for eXecutables](https://upx.github.io)
        - Web oficial del packer de UPX
        - Permite comprimir ejecutables reduciendo su tamaño y empaquetándolos.

3. **Para profundizar**
    - [Medium: La entropía de Shannon como medida de la incertidumbre y la información potencial. Parte I](https://medium.com/@JuanEnredado/la-entrop%C3%ADa-de-shannon-como-medida-de-la-incertidumbre-parte-i-6a12c4d5d36) y [Parte II](https://medium.com/@JuanEnredado/la-entrop%C3%ADa-de-shannon-como-medida-de-la-incertidumbre-y-la-informaci%C3%B3n-potencial-parte-ii-fc5e32a2b80e)
        - Artículos que explican el concepto de entropía de Shannon dentro de la teoría de la información.
        - Se describe cómo la entropía mide la incertidumbre o cantidad de información presente en un conjunto de datos, un concepto muy utilizado en áreas como criptografía, compresión de datos y análisis de malware.

    - [GitHub Ginurx: chacha20-c](https://github.com/Ginurx/chacha20-c)
        - Repositorio de github de la implementación de chacha20 utilizada en el binario.
 
### Documentos
- Infografia entropia de Shannon

    <p align="center">
        <img src="resources/Infografia_Shannon.png" alt="Infografia entropia de Shannon" width="800" />
    </p>


### Snippets
- Creación entorno virtual Python
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```
    ```
    pip install pycryptodome
    ```


### Scripts

- [`scripts/decrypt.py`](scripts/decrypt.py)
    - Utilizado para automatizar el desencriptado de la flag.