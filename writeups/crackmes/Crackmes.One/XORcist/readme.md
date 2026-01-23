# XORcist

[![YouTube](https://img.shields.io/badge/YouTube-@drovoh4k-DD0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/@drovoh4k)
[![tipo](https://img.shields.io/badge/tipo-writeup::crackme-111827?style=flat-square)]()

[![fuente](https://img.shields.io/badge/fuente-crackmes.one-111827?style=flat-square)]()
[![categoria](https://img.shields.io/badge/categoria-Reversing-0969da?style=flat-square)]()
[![dificultad](https://img.shields.io/badge/dificultad-Fácil-2ea043?style=flat-square)]()

[![arquitectura](https://img.shields.io/badge/arquitectura-x86--64-8250df?style=flat-square)]()
[![plataforma](https://img.shields.io/badge/plataforma-Unix%2FLinux%20etc.-8250df?style=flat-square)]()
[![lenguaje](https://img.shields.io/badge/lenguaje-C%2FC%2B%2B-8250df?style=flat-square)]()

| Links | |
|---|---|
| 🧩 CrackMe | https://crackmes.one/crackme/684f47bd2b84be7ea774390e |
| 🎥 WriteUp | https://youtu.be/8mgKEaVgMzQ |
| 🎥 Apoyo sobre binarios stripped | https://youtu.be/aR6MLN2pR0g |
| 🎥 Apoyo sobre `rand() % 100` | https://youtu.be/lTQ3l8pWsa8 |

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

    - Funciones C++
        - [`puts`](https://learn.microsoft.com/es-es/cpp/c-runtime-library/reference/puts-putws?view=msvc-180)(`man puts`)
            - Escribe una cadena en `stdout` y añade un salto de línea al final.
        - [`gets`](https://learn.microsoft.com/es-es/cpp/c-runtime-library/gets-getws?view=msvc-180)(`man gets`)
            - Lee una línea desde `stdin` en un buffer sin comprobar límites (función insegura; puede causar overflow).
        - [`strcspn`](https://learn.microsoft.com/es-es/cpp/c-runtime-library/reference/strcspn-wcscspn-mbscspn-mbscspn-l?view=msvc-180)(`man strcspn`)
            - Devuelve la longitud del prefijo inicial de `s` que no contiene ningún carácter del conjunto `reject`.

2. **De apoyo**
    - Tamaños variables datos
        - [Microsoft Learn: Data Type Ranges](https://learn.microsoft.com/en-us/cpp/cpp/data-type-ranges?view=msvc-170)
            - Artículo donde se muestra una tabla con los diferentes tipos de datos y sus correspondientes tamaños.
            - Por supuesto, NO hace falta memorizarlo, es algo que se va aprendiendo con el tiempo o simplemente se consulta.

        - [Stackoverflow: different size of c data type in 32 and 64 bit](https://stackoverflow.com/questions/41365987/different-size-of-c-data-type-in-32-and-64-bit)
            - Foro donde se planea si en el lenguaje C hay una diferencia entre el tamaño de los datos entre la arquitectura 32bits y 64bits.

    - [Linux Manual Page: proc_pid_status (5)](https://man7.org/linux/man-pages/man5/proc_pid_status.5.html)
        - Documentación sobre el fichero `/proc/_pid_/status`
        - Es el fichero que lee el binario para tratar de detectar si estamos haciendo uso de un debugger.

3. **Para profundizar**
    - [Hex-Rays: Patch core](https://docs.hex-rays.com/9.0/user-guide/user-interface/menu-bar/edit/patch-core)
        - Guia sobre el submenu de patching en IDA.
        - Nos permite ver los diferentes metodos de patching.
 
### Snippets
- Creación entorno virtual Python
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```
    ```
    pip install pwntools
    ```


### Scripts

- [`scripts/exploit.PY`](scripts/exploit.py)
    - Utilizado para automatizar la explotación del binario.