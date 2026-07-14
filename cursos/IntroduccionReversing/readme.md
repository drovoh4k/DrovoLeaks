<!-- drovoleaks-banner:start -->
<a href="https://drovoleaks.re/">
  <picture>
    <source media="(max-width: 768px)" srcset="https://raw.githubusercontent.com/drovoh4k/DrovoLeaks/main/.github/banner-archivado-movil.svg">
    <img src="https://raw.githubusercontent.com/drovoh4k/DrovoLeaks/main/.github/banner-archivado.svg" alt="Este repositorio ya no se actualiza — contenido movido a drovoleaks.re" width="100%">
  </picture>
</a>
<!-- drovoleaks-banner:end -->

# 📘 Introducción al Reversing

[![YouTube](https://img.shields.io/badge/YouTube-@drovoh4k-DD0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/@drovoh4k)
[![Discord](https://img.shields.io/badge/Discord-DrovoHub-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.gg/kFrpheJkdN)

[![tipo](https://img.shields.io/badge/tipo-curso-111827?style=flat-square)]()
[![nivel](https://img.shields.io/badge/nivel-Principiante-2ea043?style=flat-square)]()
[![estado](https://img.shields.io/badge/estado-En%20proceso-d29922?style=flat-square)]()


## 🎯 Objetivo
El curso está enfocado a absolutos principiantes que quieren dar sus primeros pasos en reversing sin volverse locos (no más que de lo que ya estén).

Vamos a empezar desde lo más básico hasta desarrollar una metodología que, con trabajo y esfuerzo, podamos reversear cualquier crackme de dificultad media. La diferencia con alguien experimentado será el tiempo que tengamos que invertir, pero si nos ceñimos a la metodología, lo acabaremos entendiendo todo.

Durante el camino formaréis una base sólida que en el largo plazo os ayudará mucho a entender conceptos más complejos.


## 📝 Prerrequisitos
Realmente vamos a explicar todo desde cero y os daré material complementario por si no sabéis algo, tener donde buscar o investigar. Pero sí que es cierto que unos mínimos os lo pondrán más fácil, entre ellos:
- Conocimientos básicos de Linux (saber moverse por una terminal mínimamente).
- Conocimientos básicos de C/C++ (conocer los tipos de datos y estructuras básicas).


## 📖 Módulos

**📺 Playlist:** https://www.youtube.com/playlist?list=PLKYfwBIKMkXfVvUFICiRm-qYUkprfUAL0

### Módulo 1: Introducción

*¿Qué haremos aquí?*
- Presentar el curso, entender cómo va a funcionar y gestionar las expectativas.
- Preparar un entorno tanto Linux como Windows para poder trabajar de manera cómoda.

| # | Clase | Estado |  Duración |
|---|---|---|---|
| 01 | [Presentación](modulos/1-Introduccion/1.1-Presentacion/readme.md) | ✅ Publicado | 10 min |
| 02 | [Montando el entorno](modulos/1-Introduccion/1.2-Montando_Entorno/readme.md) | ✅ Publicado | 50 min |

### Módulo 2: Fundamentos comunes

*¿Qué haremos aquí?*
- Entender una serie de conceptos básicos de arquitectura de ordenadores.
- Ser capaces de trabajar con código assembly, tanto leerlo como crear programas básicos.
- Entender las diferencias entre las diferentes arquitecturas y tener las herramientas para afrontar cualquier arquitectura (aunque sea un MIPS o una ESP32).

| # | Clase | Estado |  Duración |
|---|---|---|---|
| 01 | [Assembly, Von Neumann y Endianness](modulos/2-Fundamentos/2.1-Assembly_VonNeumann_Endianness/readme.md) | ✅ Publicado | 33 min |
| 02 | [Instrucciones Assembly](modulos/2-Fundamentos/2.2-Instrucciones_Assembly/readme.md) | ✅ Publicado | 72 min |
| 03 | [Memoria y Stack](modulos/2-Fundamentos/2.3-Memoria_Stack/readme.md) | ✅ Publicado | 54 min |
| 04 | [Calling Conventions](modulos/2-Fundamentos/2.4-Calling_Conventions/readme.md) | ✅ Publicado | 22 min |

### Módulo 3: Ruta Linux

*¿Qué haremos aquí?*
- Entenderemos la estructura de los ficheros ELF.
- Aprenderemos a hacer un triage inicial, los primeros pasos para obtener información rápidamente sobre el binario objetivo.
- Aprenderemos a usar IDA desde 0 y reversearemos varios códigos para entender todo bien.

| # | Clase | Estado |  Duración |
|---|---|---|---|
| 01 | [Binarios ELF](modulos/3-Linux/3.1-Binarios_ELF/readme.md) | ✅ Publicado | 36 min |
| 02 | [Metodología análisis de binarios](modulos/3-Linux/3.2-Analisis_binarios/readme.md) | ✅ Publicado | 34 min |
| 03 | [IDA desde 0](modulos/3-Linux/3.3-IDA_desde_0/readme.md) | ✅ Publicado | 65 min |

### Módulo 4: Ruta Windows

> **⚠️ Disclaimer**: Los contenidos pueden verse modificados a lo largo de ejecución del curso (siempre para ampliar o mejorar).

*¿Qué haremos aquí?*

- Aprenderemos a hacer un triage inicial, los primeros pasos para obtener información rápidamente sobre el binario objetivo.
- Entenderemos la estructura de los ficheros PE.
- Adaptaremos los conocimientos que ya sabemos de IDA a los binarios Windows.
- Utilizaremos x64dbg para debuggear y de nuevo combinarlo con la información obtenida en IDA.
- Y por supuesto muchos truquitos y consejos.