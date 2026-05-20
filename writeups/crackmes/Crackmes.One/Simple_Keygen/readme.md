# Simple Keygen

[![YouTube](https://img.shields.io/badge/YouTube-@drovoh4k-DD0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/@drovoh4k)
[![Discord](https://img.shields.io/badge/Discord-DrovoHub-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.gg/kFrpheJkdN)

[![tipo](https://img.shields.io/badge/tipo-writeup::crackme-111827?style=flat-square)]()
[![fuente](https://img.shields.io/badge/fuente-crackmes.one-111827?style=flat-square)]()

[![categoria](https://img.shields.io/badge/categoria-Reversing-0969da?style=flat-square)]()
[![dificultad](https://img.shields.io/badge/dificultad-Fácil-2ea043?style=flat-square)]()

[![arquitectura](https://img.shields.io/badge/arquitectura-x86--64-8250df?style=flat-square)]()
[![plataforma](https://img.shields.io/badge/plataforma-Unix%2FLinux%20etc.-8250df?style=flat-square)]()
[![lenguaje](https://img.shields.io/badge/lenguaje-C%2FC%2B%2B-8250df?style=flat-square)]()

| Links | |
|---|---|
| 🧩 Source | https://crackmes.one/crackme/5c2acb8933c5d46a3882b8d4 |
| 🪞 Mirror | [challenge/SimpleKeygen.zip](challenge/SimpleKeygen.zip) - Password: `crackmes.one` |
| 🎥 WriteUp | https://youtu.be/1KwFx8UL0lY |


## 📦 Recursos

### Enlaces

1. **Documentación técnica**
    - [FelixCloutier: x86 and amd64 instruction reference](https://www.felixcloutier.com/x86)
        - Referencia rápida para consultar instrucciones assembly.
        - Aunque para la resolución de los challenges de este repositorio es más que suficiente, es solo para tener una referencia.
        - Para cualquier proyecto serio, consultar documentación oficial como, por ejemplo, el [Intel® 64 and IA-32 Architectures Software Developer Manuals](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html).

    - [Libreria de Python PwnTools](https://docs.pwntools.com/en/stable)
        - Documentación oficial de la libreria PwnTools.
        - Muy utilizada para crear exploits ya nos simplifica muchos procesos comunes mientras creamos un exploit, en este caso llamar a un proceso con ciertos argumentos, en otros casos abrir una conexión con un server o realizar ciertas manipulaciones de bytes, etc.

2. **De apoyo**
    - Tamaños variables datos
        - [Microsoft Learn: Data Type Ranges](https://learn.microsoft.com/en-us/cpp/cpp/data-type-ranges?view=msvc-170)
        - [Stackoverflow: different size of c data type in 32 and 64 bit](https://stackoverflow.com/questions/41365987/different-size-of-c-data-type-in-32-and-64-bit)


3. **Para profundizar**
    - [Hex-Rays: Comments in IDA](https://hex-rays.com/blog/igor-tip-of-the-week-14-comments-in-ida)
        - Explicación sobre los diferentes comentarios que existen en IDA.
        - Mayoritariamente usaremos siempre los mismos, pero puede ser útil conocer los diferentes tipos.

    - [Hex-Rays: Patch core](https://docs.hex-rays.com/9.0/user-guide/user-interface/menu-bar/edit/patch-core)
        - Guia sobre el submenu de patching en IDA.
        - Nos permite ver los diferentes metodos de patching.

### Documentos

- [`resources/diagrama_argv.PNG`](resources/diagrama_argv.png) y [`resources/diagrama_argv.EXCALIDRAW`](resources/diagrama_argv.excalidraw)
    - Diagrama utilizado durante el video para entender como funciona `argv`.
    - Disclaimer: He modificado las direcciones en naranja ligeramente para que tenga más coherencia.
    
    <p align="center">
        <img src="resources/diagrama_argv.png" alt="Diagrama argv" width="800" />
    </p>


### Snippets

- Generar string con Perl
    ```sh
    perl -e 'print "A"x20 . "B"x30'
    ```
    ```sh
    ./SimpleKeyGen `perl -e 'print "A"x20 . "B"x30'`
    ```

- Creación entorno virtual Python
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```
    ```
    pip install pwntools
    ```

### Scripts

- [`scripts/exploit.py`](scripts/exploit.py)
    - Utilizado para automatizar la explotación del binario.