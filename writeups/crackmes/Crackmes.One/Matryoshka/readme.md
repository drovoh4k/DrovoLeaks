# 🧩 Matryoshka

[![YouTube](https://img.shields.io/badge/YouTube-@drovoh4k-DD0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/@drovoh4k)
[![Discord](https://img.shields.io/badge/Discord-DrovoHub-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.gg/kFrpheJkdN)

[![tipo](https://img.shields.io/badge/tipo-writeup::crackme-111827?style=flat-square)]()
[![fuente](https://img.shields.io/badge/fuente-crackmes.one-111827?style=flat-square)]()

[![categoria](https://img.shields.io/badge/categoria-Reversing-0969da?style=flat-square)]()
[![dificultad](https://img.shields.io/badge/dificultad-Media-de7d00?style=flat-square)]()

[![arquitectura](https://img.shields.io/badge/arquitectura-AMD64-8250df?style=flat-square)]()
[![plataforma](https://img.shields.io/badge/plataforma-Unix%2FLinux%20etc.-8250df?style=flat-square)]()
[![lenguaje](https://img.shields.io/badge/lenguaje-C%2FC%2B%2B-8250df?style=flat-square)]()

| Links | |
|---|---|
| 🧩 Source | https://crackmes.one/crackme/68ff42b82d267f28f69b78c8 |
| 🪞 Mirror | [challenge/Matryoshka.zip](challenge/Matryoshka.zip) - Password: `crackmes.one` |
| 🎥 WriteUp | https://youtu.be/hzmK41pv35E |


## 📄 Resumen

Matryoshka es un crackme de Linux que esconde un binario dentro de otro: cada nivel descifra con XOR un ELF nuevo, lo crea como fichero anónimo en memoria y lo ejecuta. El writeup resuelve las tres capas con IDA, pwndbg y CyberChef hasta llegar al binario final.


## 📦 Recursos

### Enlaces

- **Assembly**
    - [FelixCloutier: x86 and amd64 instruction reference](https://www.felixcloutier.com/x86)
        - Referencia rápida para consultar instrucciones assembly durante el desensamblado. Suficiente para resolver crackmes; para trabajo serio, consultar el manual oficial [Intel® 64 and IA-32 Architectures Software Developer Manuals](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html).

- **Ficheros / streams**
    - [`memfd_create`](https://man7.org/linux/man-pages/man2/memfd_create.2.html)
        - Crea un fichero anónimo en memoria y devuelve un file descriptor asociado. Útil para trabajar con un "fichero" temporal sin escribirlo en disco.

    - [`ftruncate`](https://man7.org/linux/man-pages/man3/ftruncate.3p.html)
        - Cambia el tamaño de un fichero asociado a un file descriptor. Aquí se usa para ajustar el tamaño del fichero creado con `memfd_create`.

    - [`fdopen`](https://man7.org/linux/man-pages/man3/fdopen.3p.html)
        - Asocia un `FILE*` de la libc a un file descriptor ya existente. Permite usar funciones de alto nivel como `fwrite`, `fgets` o `fprintf` sobre un descriptor abierto previamente.

    - [`fileno`](https://man7.org/linux/man-pages/man3/fileno.3.html)
        - Devuelve el file descriptor asociado a un stream `FILE*`. Es la operación inversa práctica de `fdopen`.

    - [`fwrite`](https://man7.org/linux/man-pages/man3/fwrite.3p.html)
        - Escribe datos binarios desde un buffer en un stream `FILE*`. Útil para escribir una cantidad concreta de bytes, no necesariamente una cadena terminada en `\0`.

    - [`rewind`](https://man7.org/linux/man-pages/man3/rewind.3p.html)
        - Coloca el indicador de posición de un stream al principio del fichero. Equivale a volver al offset inicial del stream.

- **Cadenas / formateo**
    - [`sprintf`](https://man7.org/linux/man-pages/man3/sprintf.3p.html)
        - Escribe texto formateado en un buffer en memoria. Funciona como `printf`, pero guarda el resultado en una cadena en lugar de imprimirlo por `stdout`.

- **Ejecución de programas**
    - [`execve`](https://man7.org/linux/man-pages/man3/exec.3.html)
        - Ejecuta un programa reemplazando la imagen del proceso actual mediante la familia `exec` (`execl`, `execle`, `execlp`, `execv`, `execvp`, `execvpe`). Relevante en explotación porque permite lanzar binarios o shells desde un proceso controlado.

- **GDB scripting**
    - [GDB Documentation: Command Files](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Command-Files.html)
        - Documentación oficial sobre scripts clásicos de GDB basados en comandos: automatizar breakpoints, ejecutar comandos al iniciar, examinar memoria o lanzar el programa con argumentos.

    - [GDB Documentation: Extending GDB using Python](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Python.html)
        - Documentación oficial sobre el uso de Python dentro de GDB: crear comandos personalizados, automatizar debugging y extender el comportamiento de GDB con scripts más complejos.

    - [GDB Documentation: Python API](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Python-API.html)
        - Referencia de la API de Python expuesta por GDB. Útil para scripts avanzados que interactúen con registros, memoria, símbolos, breakpoints o el estado del programa debuggeado.

### Documentos

- [diagrama_clase.pdf](resources/diagrama_clase.pdf)
    - PDF con las slides de la presentación utilizada en el vídeo.

### Scripts

- [`scripts/extractor.gdb`](scripts/extractor.gdb)
    - Script que automatiza la extracción de la key y el dumpeo del proceso hijo. Ejecutar con:
        ```
        gdb -x extractor.gdb ./matryoshka
        ```