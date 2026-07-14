<!-- drovoleaks-banner:start -->
<a href="https://drovoleaks.re/">
  <picture>
    <source media="(max-width: 768px)" srcset="https://raw.githubusercontent.com/drovoh4k/DrovoLeaks/main/.github/banner-archivado-movil.svg">
    <img src="https://raw.githubusercontent.com/drovoh4k/DrovoLeaks/main/.github/banner-archivado.svg" alt="Este repositorio ya no se actualiza — contenido movido a drovoleaks.re" width="100%">
  </picture>
</a>
<!-- drovoleaks-banner:end -->

# 🧩 Branchless Branching

[![YouTube](https://img.shields.io/badge/YouTube-@drovoh4k-DD0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/@drovoh4k)
[![Discord](https://img.shields.io/badge/Discord-DrovoHub-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.gg/kFrpheJkdN)

[![tipo](https://img.shields.io/badge/tipo-writeup::crackme-111827?style=flat-square)]()
[![fuente](https://img.shields.io/badge/fuente-crackmes.one-111827?style=flat-square)]()

[![categoria](https://img.shields.io/badge/categoria-Reversing-0969da?style=flat-square)]()
[![dificultad](https://img.shields.io/badge/dificultad-Media-de7d00?style=flat-square)]()

[![arquitectura](https://img.shields.io/badge/arquitectura-AMD64-8250df?style=flat-square)]()
[![plataforma](https://img.shields.io/badge/plataforma-Unix%2FLinux%20etc.-8250df?style=flat-square)]()
[![lenguaje](https://img.shields.io/badge/lenguaje-Assembly-8250df?style=flat-square)]()

| Links | |
|---|---|
| 🧩 Source | https://crackmes.one/crackme/68692679aadb6eeafb398fdf |
| 🪞 Mirror | [challenge/BranchlessBranching.zip](challenge/BranchlessBranching.zip) - Password: `crackmes.one` |
| 🎥 WriteUp | https://youtu.be/d5vR14x-qN8


## 📄 Resumen

Branchless es un crackme de Linux escrito a mano en ensamblador que elimina por completo los saltos condicionales: en lugar de je o jne, todo el flujo de control se construye guardando punteros a función en la pila y eligiendo el siguiente bloque en tiempo de ejecución mediante cmov + jmp rax. El reto pide un username y un password, deriva una clave a partir del primero usando una tabla de sustitución de 32 caracteres, y la compara contra el segundo sin cortar el bucle aunque falle un byte — el veredicto se acumula y se difiere hasta el final.


## 📦 Recursos

### Enlaces

- **Assembly**
    - [FelixCloutier: x86 and amd64 instruction reference](https://www.felixcloutier.com/x86)
        - Referencia rápida para consultar instrucciones assembly durante el desensamblado. Suficiente para resolver crackmes; para trabajo serio, consultar el manual oficial [Intel® 64 and IA-32 Architectures Software Developer Manuals](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html).

- **Syscalls**
    - [`execve`](https://man7.org/linux/man-pages/man2/execve.2.html)
        - Ejecuta un nuevo programa, reemplazando la imagen del proceso actual por la del ejecutable indicado. Recibe la ruta del programa, sus argumentos y las variables de entorno.

    - [`read`](https://man7.org/linux/man-pages/man2/read.2.html)
        - Lee datos desde un file descriptor y los copia en un buffer proporcionado por el programa. Devuelve el número de bytes leídos, `0` si se ha llegado al final del fichero, o `-1` si ocurre un error.

    - [`write`](https://man7.org/linux/man-pages/man2/write.2.html)
        - Escribe datos desde un buffer en un file descriptor. Devuelve el número de bytes escritos o `-1` si ocurre un error. Es la alternativa de bajo nivel a funciones como `fwrite` o `fprintf`.

    - [`exit`](https://man7.org/linux/man-pages/man3/exit.3.html)
        - Termina el proceso de forma normal y devuelve un código de salida al sistema operativo. Antes de finalizar, ejecuta las funciones registradas con `atexit` y vacía/cierra los streams abiertos de la libc.

### Scripts

- [`scripts/keygen.py`](scripts/keygen.py)
    - Script que genera keys válidas para cierto username.