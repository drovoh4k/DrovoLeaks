# 🧑‍🏫 Binarios ELF

<!-- CHANNEL -->
[![YouTube](https://img.shields.io/badge/YouTube-@drovoh4k-DD0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/@drovoh4k)
[![Discord](https://img.shields.io/badge/Discord-DrovoHub-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.gg/kFrpheJkdN)

<!-- VIDEO META -->
[![tipo](https://img.shields.io/badge/tipo-curso%3A%3Aclase-111827?style=flat-square)]()
[![duración](https://img.shields.io/badge/duración-36%20min-111827?style=flat-square)]()


## 📄 Resumen

**📺 Clase:** https://youtu.be/v6gtt4S2LGw?list=PLKYfwBIKMkXfVvUFICiRm-qYUkprfUAL0

En esta clase exploramos qué son los binarios ELF, cómo están estructurados internamente (header, secciones y segmentos), cómo se cargan y mapean en memoria, cómo funciona el enlazado dinámico con GOT y PLT, y cómo interactúa un proceso con el kernel a través de las syscalls.

## 📦 Recursos

### Enlaces

1. **Estructura y Formato ELF**
	- [`man elf`](https://man7.org/linux/man-pages/man5/elf.5.html)
		- Documentación técnica oficial que define el formato de archivos ejecutables, de objetos y librerías compartidas en sistemas tipo Unix.
	- [Medium: Basics of ELF (Executable and Linkable Format) file](https://medium.com/@ajmewal/basics-of-elf-executable-and-linkable-format-file-88a516877356)
		- Introducción a las secciones fundamentales del archivo (header, secciones y segmentos) para comprender cómo se almacena el código y los datos.
	- [dev.to: Understanding the Basics of ELF Files on Linux](https://dev.to/bytehackr/understanding-the-basics-of-elf-files-on-linux-61c)
		- Guía detallada sobre la estructura interna del formato ELF y su rol en el ecosistema de Linux.

2. **Ejecución y Gestión de Memoria**
	- [wxdublin.gitbooks.io: Programm in Memory](https://wxdublin.gitbooks.io/deep-into-linux-and-beyond/content/address_space.html)
		- Análisis de cómo se mapea un binario en la memoria RAM (stack, heap, data y text) durante su ejecución.

3. **Enlazado Dinámico (GOT y PLT)**
	- [Medium: GOT vs PLT in Binary Analysis](https://can-ozkan.medium.com/got-vs-plt-in-binary-analysis-888770f9cc5a)
		- Estudio sobre el redireccionamiento de funciones en tiempo de ejecución y cómo interactúan estas tablas para resolver símbolos externos.
	- [Stack Overflow: Why does the PLT exist in addition to the GOT, instead of just using the GOT?](https://stackoverflow.com/questions/43048932/why-does-the-plt-exist-in-addition-to-the-got-instead-of-just-using-the-got)
		- Discusión técnica sobre la necesidad de separar el código ejecutable (PLT) de los datos modificables (GOT) para permitir el lazy binding.

4. **Syscalls**
	- [W3challs: Systemcalls](https://syscalls.w3challs.com)
		- Tabla de referencia para identificar números de llamadas al sistema y sus argumentos según la arquitectura.
	- [System Calls in Linux](https://linuxhandbook.com/system-calls)
		- Explicación de la interfaz entre las aplicaciones de usuario y el kernel, detallando cómo se solicitan servicios de bajo nivel.


### Documentos

- [diagrama_clase.EXCALIDRAW](resources/diagrama_clase.excalidraw) y [imagenes relacionadas](resources)

    - **Introducción**
    <p align="center">
        <img src="resources/0-intro/Userland_VS_Kernel.png" alt="Definición" width="300" />
    </p>
    
    - **Formato ELF**
    <p align="center">
        <img src="resources/1-ELF/Definicion.png" alt="Definición ELF" width="300">
    </p>
    <p align="center">
        <img src="resources/1-ELF/Estructura_Interna.png" alt="Estructura Interna ELF" width="500">
    </p>
    <p align="center">
        <img src="resources/1-ELF/Program-Section_Header_Table.png" alt="Program/Section Header Table" width="500">
    </p>

    - **Carga y mapeo en memoria**
    <p align="center">
        <img src="resources/2-CargaMapeo/Contexto.png" alt="Contexto carga ELF" width="350">
    </p>
    <p align="center">
        <img src="resources/2-CargaMapeo/Secuencia_Carga.png" alt="Secuencia de carga" width="300">
    </p>
    <p align="center">
        <img src="resources/2-CargaMapeo/Memory_Layout.png" alt="Memory Layout" width="500">
    </p>
    <p align="center">
        <img src="resources/2-CargaMapeo/DynamicLinking_Contexto.png" alt="Dynamic Linking Contexto" width="600">
    </p>
    <p align="center">
        <img src="resources/2-CargaMapeo/DynamicLinking_LazyBinding.png" alt="Dynamic Linking Lazy Binding" width="600">
    </p>

    - **Syscall**
    <p align="center">
        <img src="resources/3-Syscalls/Contexto.png" alt="Syscalls Contexto" width="450">
    </p>
    <p align="center">
        <img src="resources/3-Syscalls/Mecanismo.png" alt="Syscalls Mecanismo" width="400">
    </p>