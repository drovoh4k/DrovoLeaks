# The Legend of Shiitakoin

[![YouTube](https://img.shields.io/badge/YouTube-@drovoh4k-DD0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/@drovoh4k)
[![tipo](https://img.shields.io/badge/tipo-writeup::ctf-111827?style=flat-square)]()

[![fuente](https://img.shields.io/badge/fuente-Northsec2022-111827?style=flat-square)]()
[![categoria](https://img.shields.io/badge/categoria-Reversing-0969da?style=flat-square)]()
[![dificultad](https://img.shields.io/badge/dificultad-Fácil-2ea043?style=flat-square)]()

[![arquitectura](https://img.shields.io/badge/arquitectura-MIPS-8250df?style=flat-square)]()
[![plataforma](https://img.shields.io/badge/plataforma-Nintendo64-8250df?style=flat-square)]()
[![lenguaje](https://img.shields.io/badge/lenguaje-C%2FC%2B%2B-8250df?style=flat-square)]()

| Links | |
|---|---|
| 🧩 Source | https://github.com/fresh-eggs/n64-northsec-2022 |
| 🪞 Mirror | [challenge/legend_of_shiitakoin.zip](challenge/legend_of_shiitakoin.zip) |
| 🎥 WriteUp | https://youtu.be/8qLSEwAOrdU |


## 📦 Recursos

### Enlaces

1. **Documentación técnica**
    - [ultra64: `nuContDataGetEx`](https://ultra64.ca/files/documentation/online-manuals/functions_reference_manual_2.0i/nusys/nuContDataGetEx.html)
        - Función encargada de leer los datos del mando y guardarlos en una estructura `NUContData`.

	- [Github n64sdkmod: nusys/nusys.h - `NUContData`](https://github.com/ModernN64SDKArchives/n64sdkmod/blob/master/packages/libnusys/usr/include/n64/nusys/nusys.h#L522)
        - Estructura que almacena el estado del mando, incluyendo la trigger data.

    - [Github n64sdkmod - PR/os_cont.h - `Buttons`](https://github.com/ModernN64SDKArchives/n64sdkmod/blob/d27d200a34b5b4f6dcde092153fdc67157b8a8ae/packages/n64sdk/usr/include/n64/PR/os_cont.h#L121)
        - Defines de las máscaras de bits de los diferentes botones.

2. **De apoyo**
    - [Project64](https://www.pj64-emu.com)
        - Emulador gratuito y opensource para ejecutar las ROMs de Nintendo64 en PC.


    - [GeeksforGeeks: Structure Member Alignment, Padding and Data Packing](https://www.geeksforgeeks.org/c/structure-member-alignment-padding-and-data-packing)
        - Explicación sobre como el compilador de C organiza los miembros de una estructura mediante alineación y relleno para que cada dato quede en direcciones óptimas para la CPU.

3. **Para profundizar**
    - [Plugin Ghidra: N64LoaderWV](https://github.com/zeroKilo/N64LoaderWV)
        - Plugin para Ghidra que permite cargar ROMs de Nintendo 64 (.z64, .n64, .v64) correctamente, ajustando la endianness y mapeando secciones de RAM/ROM/boot.

    - [Arquitectura de la Nintendo 64](https://www.copetti.org/es/writings/consoles/nintendo-64)
        - Análisis técnico y detallado de la arquitectura interna de la consola Nintendo 64.
        - Explica cómo están diseñados y funcionan su CPU, memoria, gráficos, audio, sistema operativo y otros subsistemas.
        - También incluye decisiones de diseño y limitaciones que la hacen única dentro de las consolas de su generación.



### Diagramas

- [resources/diagrama_button.PNG](resources/diagrama_button.png) y [resources/diagrama_trigger.PNG](resources/diagrama_trigger.png)
    - Diagramas utilizados durante el video para entender la diferencia entre button y trigger

    <p align="center">
        <img src="resources/diagrama_button.png" alt="Diagrama Button" width="500" />
    </p>
    <p align="center">
        <img src="resources/diagrama_trigger.png" alt="Diagrama Trigger" width="500" />
    </p>