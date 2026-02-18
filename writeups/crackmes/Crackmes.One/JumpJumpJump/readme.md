# JumpJumpJump

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
| 🧩 Source | https://crackmes.one/crackme/5c1a939633c5d41e58e005d1 |
| 🪞 Mirror | [challenge/JumpJumpJump.zip](challenge/JumpJumpJump.zip) - Password: `crackmes.one` |
| 🎥 WriteUp | https://youtu.be/ccpKL1ffWss |


## 📦 Recursos

### Enlaces

1. **Documentación técnica**
    - [FelixCloutier: x86 and amd64 instruction reference](https://www.felixcloutier.com/x86)
        - Referencia rápida para consultar instrucciones assembly.
        - Aunque para la resolución de challenges de HTB es más que suficiente, es solo para tener una referencia.
        - Para cualquier proyecto serio, consultar documentación oficial como, por ejemplo, el [Intel® 64 and IA-32 Architectures Software Developer Manuals](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html).

    - Funciones operaciones fichero
        - Función [`fgets`](https://learn.microsoft.com/es-es/cpp/c-runtime-library/reference/fgets-fgetws) (`man fgets`)
            - Lee una línea (o hasta `n-1` caracteres) desde un `FILE*` y la guarda en un buffer, incluyendo el `\n` si aparece antes del límite.
        - Función [`puts`](https://learn.microsoft.com/es-es/cpp/c-runtime-library/reference/puts-putws) (`man puts`)
            - Escribe una cadena en `stdout` seguida automáticamente de un salto de línea (`\n`).
        - Función [`putchar`](https://learn.microsoft.com/es-es/cpp/c-runtime-library/reference/putchar-putwchar) (`man putchar`)
            - Escribe un único carácter en `stdout` (equivalente práctico a `fputc(c, stdout)`).

    - Funciones strings
        - Función [`strlen`](https://learn.microsoft.com/es-es/cpp/c-runtime-library/reference/strlen-wcslen-mbslen-mbslen-l-mbstrlen-mbstrlen-l) (`man strlen`)
            - Devuelve la longitud de una cadena terminada en `\0` (sin contar el byte nulo final).
        - Función [`printf`](https://learn.microsoft.com/es-es/cpp/c-runtime-library/reference/printf-printf-l-wprintf-wprintf-l) (`man printf`)
            - Imprime texto formateado en `stdout` según una cadena de formato, sustituyendo especificadores (`%d`, `%s`, `%x`, etc.) por valores de argumentos.

    - [Libreria de Python PwnTools](https://docs.pwntools.com/en/stable)
        - Documentación oficial de la libreria PwnTools.
        - Muy utilizada para crear exploits ya nos simplifica muchos procesos comunes mientras creamos un exploit, en este caso llamar a un proceso con ciertos argumentos, en otros casos abrir una conexión con un server o realizar ciertas manipulaciones de bytes, etc.

### Snippets

- Prueba rápida sobre la generación del flag con Python
    ```
    nums = [33] # empieza en '!'

    for i in range(1, 10):
        nums.append(nums[-1] + i + 1)

    print(nums)
    ```
    ```
    help(chr)
    ```
    ```
    print(''.join(chr(n) for n in nums))
    ```

- Creación entorno virtual Python
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```
    ```sh
    pip install pwntools
    ```

### Scripts

- [`scripts/exploit.PY`](scripts/exploit.py)
    - Utilizado para automatizar la explotación del binario.