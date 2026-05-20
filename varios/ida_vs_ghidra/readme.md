#  ⛑️ IDA vs Ghidra

[![YouTube](https://img.shields.io/badge/YouTube-@drovoh4k-DD0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/@drovoh4k)
[![Discord](https://img.shields.io/badge/Discord-DrovoHub-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.gg/kFrpheJkdN)

[![tipo](https://img.shields.io/badge/tipo-varios-111827?style=flat-square)]()
[![tema](https://img.shields.io/badge/tema-Disassembler-0969da?style=flat-square)]()


## 📄 Resumen

**🎥 Video:** https://youtu.be/rVIAyQZNFKc

Si estás empezando en reversing, una de las preguntas más frecuentes es "¿IDA o Ghidra?". Es por ello que en este vídeo analizaremos ambas herramientas en aspectos clave para que elijas con criterio.

En este video compararemos:
- **Calidad del decompilador**: ¿Cuál tiene mejor decompilación y por qué a veces uno te da pseudocódigo usable con menos pelea?

- **Funciones, librerías y tipos**: Cuánto te ahorra cada herramienta reconociendo cosas por ti.

- **Scripting y automatización**: ¿Qué opciones tienes para automatizar procesos en cada tarea?

- **Colaboración**: Qué opciones reales tienes para trabajar en equipo sobre la misma base de análisis.

- **Debugging**: Qué tan buena es la integración del debugger dentro de ambas herramientas.

- **Arquitecturas**: Qué esperar en x86/x64 y qué pasa cuando te sales de lo típico y entras en ISAs menos comunes.

Y al final te haré unas recomendaciones claras según tu caso (principiante, empresa, malware, presupuesto cero, etc.).

## 📦 Recursos

 ### Calidad del decompilador
- [Manual oficial de SLEIGH](https://ghidra.re/ghidra_docs/languages/html/sleigh.html)  
  - Explica el lenguaje SLEIGH, que Ghidra usa para describir una ISA y "levantar" instrucciones hacia su pipeline de análisis.
  - Te sirve para entender por qué a veces el decompiler mejora mucho cuando ajustas definiciones/semántica de instrucciones.

- [Referencia oficial de p-code operations](https://ghidra.re/ghidra_docs/languages/html/pcodedescription.html)  
  - Referencia del p-code, la IR de Ghidra (las "operaciones" con las que representa el comportamiento).
  - Útil si quieres razonar sobre decompilación/transformaciones y entender de dónde sale el pseudocódigo.

- [Decompiler internals / análisis con p-code (NCC Group)](https://www.nccgroup.com/research-blog/earlyremoval-in-the-conservatory-with-the-wrench-exploring-ghidra-s-decompiler-internals-to-make-automatic-p-code-analysis-scripts)  
  - Artículo técnico de los internals del decompiler y como hace un análisis automático sobre p-code.

- [p-code injection (ejemplo práctico)](https://swarm.ptsecurity.com/guide-to-p-code-injection)  
  - Guía práctica para inyectar p-code y corregir/forzar comportamientos del decompiler.
  - Muy útil para binarios raros que rompen heurísticas y te obligan a "intervenir".

- [Material oficial de Ghidra: Improving disassembly/decompilation (PDF)](https://ghidra.re/ghidra_docs/GhidraClass/Advanced/improvingDisassemblyAndDecompilation.pdf)  
  - PDF oficial con técnicas concretas para reducir fricción: tipos, funciones, data, referencias, etc.
  - Si el pseudocódigo "casi está", esto suele ser lo que lo convierte en algo usable.


### Funciones, librerías y tipos
- [Hex-Rays Docs: FLIRT (signatures)](https://docs.hex-rays.com/user-guide/signatures/flirt)  
  - Documentación oficial sobre firmas de librerías en IDA.


- [Hex-Rays: Lumina](https://hex-rays.com/lumina)  
  - Add-on para compartir/recuperar metadata (nombres, protos, tipos…) basada en hashes.
  - Muy útil para acelerar análisis cuando el binario se parece a otros o trabajas en equipo.

- [Ghidra: Function ID (FID) docs (fid.xml)](https://github.com/NationalSecurityAgency/ghidra/blob/master/Ghidra/Features/FunctionID/src/main/doc/fid.xml)  
  - Documentación del sistema FID/FIDB para identificar funciones de librerías.
  - Es el "camino Ghidra" para reconocimiento por bases, parecido al rol que juega FLIRT en IDA.

- [Repositorio de FIDBs (threatrack/ghidra-fidb-repo)](https://github.com/threatrack/ghidra-fidb-repo)  
  - Repo comunitario con FIDBs ya hechas para usarlas directamente.
  - Buen atajo para que Ghidra identifique librerías sin tener que montarte tú toda la base.

- [Tarlogic: ESP32 firmware usando Ghidra FIDB](https://www.tarlogic.com/blog/esp32-firmware-using-ghidra-fidb)  
  - Caso real aplicando FIDB en firmware/IoT (ESP32).
  - Te da una idea clara de cuándo FID "marca la diferencia" en entornos menos triviales.


### Scripting y automatización
- [Hex-Rays: IDAPython (Getting Started)](https://docs.hex-rays.com/developer-guide/idapython/idapython-getting-started)  
  - Entrada oficial a IDAPython para automatizar IDA.
  - Perfecto para renombrados masivos, helpers de reversing, extracción de info y tooling repetible.

- [PyGhidra (PyPI)](https://pypi.org/project/pyghidra)  
  - Acceso a la API de Ghidra desde Python.

### Colaboración
- [Hex-Rays: IDA Teams](https://hex-rays.com/teams)  
  - Solución oficial para **colaboración** en IDA con arquitectura cliente-servidor y control de cambios.
  - Encaja especialmente bien en entorno empresa donde ya hay licencias y procesos montados.

- [Ghidra shared projects / colaboración (byte.how)](https://byte.how/posts/collaborative-reverse-engineering)  
  - Explica el flujo típico de proyecto en servidor + analistas compartiendo cambios/anotaciones.
  - Alternativa sólida "sin coste extra" si lo que quieres es trabajo en equipo con Ghidra.


### Debugging
- [Hex-Rays Docs: Debugger tutorials (IDA)](https://docs.hex-rays.com/user-guide/debugger/debugger-tutorials)  
  - Tutoriales oficiales para aprender sobre el debugger integrado de IDA.
  - Útil para montar un flujo "todo en uno" (estático + dinámico) sin salir de la herramienta.

- [Tour oficial del Debugger Tool (Ghidra)](https://ghidra.re/ghidra_docs/GhidraClass/Debugger/A2-UITour.html)  
  - Recorrido oficial por el debugger de Ghidra (UI y componentes).
  - Te orienta rápido si quieres debugear dentro de Ghidra en vez de irte a herramientas externas.


### Arquitecturas
- [Hex-Rays: Decompiler (arquitecturas soportadas)](https://hex-rays.com/decompiler)  
  - Página oficial que lista/describe el soporte del decompilador de Hex-Rays según arquitectura.
  - Importante para no confundirse: una cosa es que IDA desensamble una ISA y otra que exista decompiler "de verdad" para ella.


- [Ghidra (Wiki): Frequently asked questions — "What processors are currently supported?"](https://github.com/NationalSecurityAgency/ghidra/wiki/Frequently-asked-questions#what-processors-are-currently-supported)
  - En la FAQ oficial del repo de Ghidra tienes un listado resumido de los procesadores/arquitecturas soportados (x86 16/32/64, ARM/AArch64, PowerPC, MIPS, 68xxx, Java/DEX, PA-RISC, PIC, SPARC, Z80, 6502, 8051, MSP430, AVR, etc.).
