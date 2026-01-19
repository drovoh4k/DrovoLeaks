#  ⛑️ Debuggear binarios stripped con GDB

[![YouTube](https://img.shields.io/badge/YouTube-@drovoh4k-DD0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/@drovoh4k)

![tipo](https://img.shields.io/badge/tipo-tutorial-111827?style=flat-square)
![tema](https://img.shields.io/badge/tema-debugging-0969da?style=flat-square)


## 📄 Resumen

**🎥 Tutorial:** https://youtu.be/aR6MLN2pR0g

¿Te ha pasado que haces el típico `breakpoint main` con GDB y un día, con "un binario aparentemente normal", te suelta un `Function not defined`? No es culpa tuya, sino que lo más probable es que estés delante de un ELF stripped.

En este vídeo te enseño a:
- Cómo identificar un ELF stripped sin ejecutarlo (file, nm, readelf)
- Qué cambia realmente al strippear (la .symtab desaparece; la .dynsym suele quedarse).
- 3 formas de debugear un stripped:
    - Ir al Entry Point y reconocer el arranque hasta `__libc_start_main`
    - Breakpoint pending en `__libc_start_main` y saltar a main vía RDI
    - El workflow recomendado: IDA + base address para poner breakpoints por dirección de forma rápida


## 📦 Recursos

### Enlaces

1. **Documentación técnica**
    - Manuales de las herramientas utilizadas
        - `man gdb`
            - Manual oficial de GDB: ejecución, breakpoints y control del debugging.
            - Útil para consultar sintaxis/opciones y qué se puede inspeccionar (registros, memoria, stack, etc.).
            - `pwndbg` es una capa de abstracción; la gran mayoría de comandos funcionan exactamente igual que en `gdb`.
        - `man nm`
            - Útil para ver símbolos del binario (cuando existen).
            - Te ayuda a confirmar rápidamente si un binario "tiene nombres" (como main) o si está stripped / no exporta lo que esperas.
        - `man readelf`
            - Permite inspeccionar la estructura interna de un ELF de manera estática.
    - Articulos sobre `__libc_start_main`
        - [Linux Standard Base Core Specification: __libc_start_main](https://refspecs.linuxbase.org/LSB_5.0.0/LSB-Core-generic/LSB-Core-generic/baselib---libc-start-main-.html)
            - Referencia "formal" (tipo especificación) sobre la función y su rol en el arranque
            - Buen recurso si quieres una explicación más normativa/estándar.
        - [Stackoverflow: What is __libc_start_main and _start?](https://stackoverflow.com/questions/62709030/what-is-libc-start-main-and-start)
            - Respuesta del foro Stackoverflow con una explicación más práctica

2. **De apoyo**
    - [Curso Introducción al Reversing GRATUITO - Clase 2: Montando el entorno](../../../cursos/IntroduccionReversing/modulos/1-Introduccion/1.2-Montando_Entorno/readme.md)
        - Si no tienes un entorno Linux listo, en esta clase te explico cómo tener tu entorno preparado, tanto un entorno Linux como uno Windows.

3. **Para profundizar**
    - [The 101 of ELF files on Linux: Understanding and Analysis](https://linux-audit.com/elf-binaries-on-linux-understanding-and-analysis)
        - Buen punto de partida para aprender/repasar secciones típicas, headers y el modelo mental de ELF.
        - Útil para comprender mejor las secciones `.symtab` y `.dynsym`.
 
### Snippets

- Compilación con símbolos
    ```
    gcc -O0 -g -fno-omit-frame-pointer -o demo demo.c
    ```

- Strip
    ```
    strip --strip-all demo -o demo_stripped
    ```

### Scripts
- [demo.c](resources/demo.c)
    - Código fuente utilizado durante el video.