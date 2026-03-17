# 🧑‍🏫 Calling Conventions

<!-- CHANNEL -->
[![YouTube](https://img.shields.io/badge/YouTube-@drovoh4k-DD0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/@drovoh4k)

<!-- VIDEO META -->
[![tipo](https://img.shields.io/badge/tipo-curso%3A%3Aclase-111827?style=flat-square)]()
[![duración](https://img.shields.io/badge/duración-22%20min-111827?style=flat-square)]()


## 📄 Resumen

**📺 Clase:** https://youtu.be/zbe5pUvjHGw?list=PLKYfwBIKMkXfVvUFICiRm-qYUkprfUAL0

En esta clase exploramos qué son las calling conventions y cómo determinan el paso de argumentos, el valor de retorno y la limpieza del stack, comparando las convenciones más comunes en x86 y AMD64 para aprender a identificarlas durante reversing.

## 📦 Recursos

### Enlaces

- **x86**
    - [cdecl](https://learn.microsoft.com/en-us/cpp/cpp/cdecl)
        - Convención de llamada típica en C para x86, donde los argumentos se pasan por el stack y el caller es quien limpia la pila tras la llamada.
    - [stdcall](https://learn.microsoft.com/en-us/cpp/cpp/stdcall)
        - Convención de llamada muy usada en Windows x86, donde los argumentos se pasan por el stack pero la limpieza la realiza la función llamada.
    - [fastcall](https://learn.microsoft.com/en-us/cpp/cpp/fastcall)
        - Convención de llamada en x86 que busca optimizar el rendimiento pasando los primeros argumentos en registros y dejando el resto en el stack.

- **AMD64**
    - [System V AMD64](https://refspecs.linuxfoundation.org/elf/x86_64-abi-0.99.pdf)
        Convención de llamada usada en sistemas Unix-like de 64 bits, donde los primeros argumentos se pasan en registros como `rdi`, `rsi`, `rdx`, `rcx`, `r8` y `r9`.
    - [Win64](https://learn.microsoft.com/en-us/cpp/build/x64-calling-convention)
        - Convención de llamada estándar en Windows de 64 bits, donde los primeros argumentos se pasan en `rcx`, `rdx`, `r8` y `r9`, y además se reserva shadow space en el stack.


### Documentos

- [diagrama_clase.EXCALIDRAW](resources/diagrama_clase.excalidraw) y [imagenes relacionadas](resources)

    - **Introducción**
    <p align="center">
        <img src="resources/0-intro/definicion.png" alt="Definición" width="500" />
    </p>
    <p align="center">
        <img src="resources/0-intro/que_determinan.png" alt="¿Que determinan?" width="400" />
        <img src="resources/0-intro/mapa_general.png" alt="Mapa general" width="400" />
    </p>
    
    - **x86 (32 bits)**
    <table align="center">
        <tr>
            <td valign="top">
                <img src="resources/1-x86/cdecl.png" alt="cdecl" width="300">
            </td>
            <td valign="top">
                <img src="resources/1-x86/stdcall.png" alt="stdcall" width="300">
            </td>
            <td valign="top">
                <img src="resources/1-x86/fastcall.png" alt="fastcall" width="300">
            </td>
        </tr>
    </table>

    - **AMD64 (64 bits)**
    <table align="center">
        <tr>
            <td valign="top">
                <img src="resources/2-amd64/SystemV_AMD64.png" width="300">
            </td>
            <td valign="top">
                <img src="resources/2-amd64/Win64.png" width="300">
            </td>
        </tr>
    </table>

    - **Árbol decisiones**
    <p align="center">
        <img src="resources/3-arbol/arbol_decision.png" alt="Arbol decisión" width="800" />
    </p>