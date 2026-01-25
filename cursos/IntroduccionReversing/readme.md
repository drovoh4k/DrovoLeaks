# 📘 Introducción al Reversing

[![YouTube](https://img.shields.io/badge/YouTube-@drovoh4k-DD0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/@drovoh4k)

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

> **⚠️ Disclaimer**: Los contenidos pueden verse modificados a lo largo de ejecucción del curso (siempre para ampliar o mejorar).

*¿Qué haremos aquí?*
- Entender una serie de conceptos básicos de arquitectura de ordenadores.
- Ser capaces de trabajar con código assembly, tanto leerlo como crear programas básicos.
- Entender las diferencias entre las diferentes arquitecturas y tener las herramientas para afrontar cualquier arquitectura (aunque sea un MIPS o una ESP32).
- Presentar una serie de metodologías para analizar código, las cuales aplicaremos en posteriores módulos.

| # | Clase | Estado |  Duración |
|---|---|---|---|
| 01 | [Assembly, Von Neumann y Endianness](modulos/2-Fundamentos/2.1-Assembly_VonNeumann_Endianness/readme.md) | ✅ Publicado | 33 min |
| 02 | ... | ... | ... |

### Módulo 3: Ruta Linux

> **⚠️ Disclaimer**: Los contenidos pueden verse modificados a lo largo de ejecucción del curso (siempre para ampliar o mejorar).

*¿Qué haremos aquí?*
- Aprenderemos a hacer un triage inicial, los primeros pasos para obtener información rápidamente sobre el binario objetivo.
- Entenderemos la estructura de los ficheros ELF.
- Aprenderemos a usar IDA desde 0 y reversearemos varios códigos para entender todo bien.
- Utilizaremos GDB para debuggear y aprenderemos cómo combinarlo con la información obtenida en IDA.
- Os enseñaré muchos truquitos y consejos que me habría gustado saber en mis inicios.

### Módulo 4: Ruta Windows

> **⚠️ Disclaimer**: Los contenidos pueden verse modificados a lo largo de ejecucción del curso (siempre para ampliar o mejorar).

*¿Qué haremos aquí?*

- Aprenderemos a hacer un triage inicial, los primeros pasos para obtener información rápidamente sobre el binario objetivo.
- Entenderemos la estructura de los ficheros PE.
- Adaptaremos los conocimientos que ya sabemos de IDA a los binarios Windows.
- Utilizaremos x64dbg para debuggear y de nuevo combinarlo con la información obtenida en iDA.
- Y por supuesto muchos truquitos y consejos.