# 🧩 Encrypted Box

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
| 🧩 Source | https://crackmes.one/crackme/64f1f7dbd931496abf90952d |
| 🪞 Mirror | [challenge/encrypted_box.zip](challenge/encrypted_box.zip) - Password: `crackmes.one` |
| 🎥 WriteUp | https://youtu.be/TwRw_Vc8frw |


## 📄 Resumen

`encrypted_box` es un crackme de Linux que pide una contraseña de 16 bytes y la valida con rondas de AES por hardware (AES-NI: `aesenc` / `aesdec`). Lo curioso es que cada ronda usa tu entrada como clave para descifrar en memoria la siguiente etapa, así que el binario es una cebolla de ~1000 stages que se van desempaquetando solos. En el vídeo recuperamos la contraseña invirtiendo cada ronda de AES y, para no repetirlo mil veces a mano, lo automatizamos con Intel Pin (instrumentación binaria dinámica): falseamos el `read()`, interceptamos cada comprobación e inyectamos el bloque que el binario espera.


## 📦 Recursos

### Enlaces

- **Assembly**
    - [FelixCloutier: x86 and amd64 instruction reference](https://www.felixcloutier.com/x86)
        - Referencia rápida para consultar instrucciones assembly durante el desensamblado. Suficiente para resolver crackmes; para trabajo serio, consultar el manual oficial [Intel® 64 and IA-32 Architectures Software Developer Manuals](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html).

    - [Wikipedia: AES instruction set (AES-NI)](https://en.wikipedia.org/wiki/AES_instruction_set)
        - Listado de las instrucciones hardware de AES (`aesenc`, `aesenclast`, `aesdec`, `aesdeclast`, `aesimc`) y a qué transformación equivale cada una. Es la base para invertir cada ronda y recuperar la entrada que el binario espera.

- **Syscalls**
    - [Linux Syscall Table x86_64](https://syscalls.w3challs.com/?arch=x86_64)
        - Tabla de syscalls de Linux para x86-64 con sus números y argumentos. Aquí se usa para identificar el `sys_read` (nº 0) que lee la contraseña, que luego falseamos tanto en GDB como en el pintool.

- **Entropía**
    - [Wikipedia: Entropía de Shannon](https://es.wikipedia.org/wiki/Entrop%C3%ADa_(informaci%C3%B3n))
        - Mide la incertidumbre (bits por byte) de una región de datos.
        - Sobre bytes, el máximo es `8.0`: cuanto más se acerca, más uniforme/aleatoria es la distribución.
        Datos cifrados o comprimidos rozan ese tope, mientras que código y texto se quedan bastante por debajo, así que es la forma rápida de detectar a ojo qué partes del binario están encriptadas.


- **Automatización**
    - [Intel Pin - A Dynamic Binary Instrumentation Tool](https://www.intel.com/content/www/us/en/developer/articles/tool/pin-a-dynamic-binary-instrumentation-tool.html)
        - Framework de instrumentación binaria dinámica de Intel. Permite inyectar código propio en cualquier punto del flujo del binario sin recompilarlo, que es como automatizamos la resolución de las ~1000 stages.

### Scripts

- `scripts/recover_stages`
    - [`scripts/recover_stages/recover_stages.c`](scripts/recover_stages/recover_stages.c)
        - Resolución manual de las primeras stages.
        - Invierte una ronda AES a partir del valor esperado (`xmm0`) y la clave (`xmm1`) leídos en GDB, y escribe el bloque recuperado en `input.bin`.
        - Trae dos inversores:
            - `inverse_aesdec`: stage 1, emula el `MixColumns` que no existe suelto con la terna `aesdeclast` → `aesenc` → `aesenclast`
            - `inverse_aesenc`: stage 2, con `aesimc` + `aesdeclast`
        - Compilar con:
            ```
            gcc -maes -msse4.1 recover_stages.c -o recover_stages
            ```

- `scripts/solver_pintool`
    - [`install_deps.sh`](scripts/solver_pintool/install_deps.sh)
        - Instala las dependencias en Linux x86-64: herramientas de compilación (`g++`, `make`) vía el gestor de paquetes y el kit de Intel Pin 4.2 (descarga + extracción en `/opt`), y exporta `PIN_ROOT` en los rc del shell.
    - [`Makefile`](scripts/solver_pintool/Makefile)
        - Compila el pintool delegando en la infraestructura de Pin (`makefile.config` + reglas), lo lanza sobre el binario y genera la password.
        - `make` construye el `.so`; `make run` instrumenta y resuelve; `make clean` limpia.
    - [`solver_pintool.cpp`](scripts/solver_pintool/solver_pintool.cpp)
        - El pintool resolutor. Neutraliza el `sys_read` (finge que leyó el bloque, sin teclado), intercepta cada ronda de comparación (solo las `aesenc`/`aesdec` con destino `XMM2`), invierte la ronda para deducir la entrada que produce el valor esperado y la inyecta en `[rsp]`.
        - La concatenación de los bloques recuperados es la contraseña.

