<!-- drovoleaks-banner:start -->
<a href="https://drovoleaks.re/">
  <picture>
    <source media="(max-width: 768px)" srcset="https://raw.githubusercontent.com/drovoh4k/DrovoLeaks/main/.github/banner-archivado-movil.svg">
    <img src="https://raw.githubusercontent.com/drovoh4k/DrovoLeaks/main/.github/banner-archivado.svg" alt="Este repositorio ya no se actualiza — contenido movido a drovoleaks.re" width="100%">
  </picture>
</a>
<!-- drovoleaks-banner:end -->

# 🧑‍🏫 IDA desde 0

<!-- CHANNEL -->
[![YouTube](https://img.shields.io/badge/YouTube-@drovoh4k-DD0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/@drovoh4k)
[![Discord](https://img.shields.io/badge/Discord-DrovoHub-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.gg/kFrpheJkdN)

<!-- VIDEO META -->
[![tipo](https://img.shields.io/badge/tipo-curso%3A%3Aclase-111827?style=flat-square)]()
[![duración](https://img.shields.io/badge/duración-65%20min-111827?style=flat-square)]()


## 📄 Resumen

**📺 Clase:** https://youtu.be/EYas4FT7S0k?list=PLKYfwBIKMkXfVvUFICiRm-qYUkprfUAL0

En esta clase aprenderás a usar IDA desde cero analizando un binario real paso a paso: desde la primera carga y la orientación con strings y xrefs, hasta el renombrado, los tipos, el decompilador y el patching con GDB. Una clase completa que recorre todo el flujo de trabajo de la ingeniería inversa.


## 📦 Recursos

### Enlaces

- **Bloque 1: Entorno y primera carga**
    - [Basic Usage — Hex-Rays Docs](https://docs.hex-rays.com/getting-started/basic-usage)
        - Primeros pasos oficiales: cómo IDA detecta solo el formato y la arquitectura al cargar, y qué es la base de datos `.i64` (IDB) donde se guarda tu trabajo.
        - Aclara un punto clave para toda la clase: tras la carga, IDA no toca el binario original; todos tus cambios viven en la IDB hasta que decidas lo contrario.

    - [Igor's Tip #22: IDA desktop layouts](https://hex-rays.com/blog/igors-tip-of-the-week-22-ida-desktop-layouts)
        - Acoplar, flotar y reorganizar ventanas, y guardar la distribución como un Desktop reutilizable; `Windows > Reset desktop` para volver al estado inicial.
        - Justo lo necesario para dejar el espacio de trabajo cómodo antes de empezar a analizar.

    - [Open subviews — Hex-Rays Docs](https://docs.hex-rays.com/user-guide/user-interface/menu-bar/view/open-subviews)
        - El catálogo de todas las ventanas de IDA (Strings, Functions, Imports, Hex View, Pseudocode,...) y cómo abrirlas desde `View > Open subviews`.
        - Complementa la distribución de ventanas: primero sabes qué vistas existen, luego las colocas a tu gusto en el desktop.

- **Bloque 2: Configuración de visualización**
    - [Igor's Tip #25: Disassembly options](https://hex-rays.com/blog/igors-tip-of-the-week-25-disassembly-options)
        - Configuración del listado desde `Options → General`: line prefixes (columna de direcciones), offsets relativos a función y demás info contextual.
        - Detalle útil: IDA mantiene dos juegos de opciones independientes (modo grafo y modo texto), algo que confunde a mucha gente al principio.

    - [Igor's Tip #23: Graph view](https://hex-rays.com/blog/igors-tip-of-the-week-23-graph-view)
        - A fondo sobre la vista de grafo: colores de las aristas (verde = salto tomado, rojo = no tomado), aristas gruesas para bucles, mover nodos y `Layout graph` para reordenar.
        - Cubre el agrupado de nodos, muy práctico para simplificar grafos grandes y marcar rutas de interés.

- **Bloque 3 - Orientación: strings, imports y xrefs**
    - [Igor's Tip #128: String list](https://hex-rays.com/blog/igors-tip-of-the-week-128-strings-list)
        - La ventana de Strings (`Shift+F12`) como punto de entrada en un binario desconocido: filtros por tipo, longitud mínima y ASCII estricto para reducir ruido.
        - Explica por qué la primera apertura tarda (IDA escanea toda la base de datos) y cómo limitar el escaneo en binarios grandes.

    - [Igor's Tip #16: Cross-references](https://hex-rays.com/blog/igor-tip-of-the-week-16-cross-references)
        - El concepto que sostiene toda la navegación en IDA: tipos de xref (jump, call, flow) y cómo IDA rastrea quién usa qué y desde dónde.
        - Base para llegar a un string o un import y descubrir de inmediato qué función lo referencia.

    - [Igor's Tip #80: Bookmarks](https://hex-rays.com/blog/igors-tip-of-the-week-80-bookmarks)
        - Marcar direcciones con `Alt+M` y la vista de Bookmarks (`Ctrl+Shift+M`), con carpetas para organizarlas.
        - La "libreta de campo" del análisis: deja marcas en lo interesante para no tener que redescubrirlo después.

- **Bloque 4 - Análisis: renombrado y documentación**
    - [Igor's Tip #42: Renaming and retyping](https://hex-rays.com/blog/igors-tip-of-the-week-42-renaming-and-retyping-in-the-decompiler)
        - Renombrar con `N` (mismo atajo en desensamblado y pseudocódigo) y cómo un buen nombre transforma la legibilidad de una función.
        - Incluye el auto-renombrado, que propaga nombres a lo largo del pseudocódigo según vas analizando.

    - [Igor's Tip #14: Comments in IDA](https://hex-rays.com/blog/igor-tip-of-the-week-14-comments-in-ida)
        - Tipos de comentarios: de línea, repetibles (se muestran en cada referencia al elemento) y de función, cada uno con su atajo.
        - Truco interesante: los comentarios repetibles sobre una variable global aparecen en todos los sitios donde se usa.

- **Bloque 5 - Interpretación de datos en memoria**
    - [Igor's Tip #46: Disassembly operand representation](https://hex-rays.com/blog/igors-tip-of-the-week-46-disassembly-operand-representation)
        - Por qué el mismo byte puede mostrarse como hex, decimal, char, offset… sin que cambien los bytes reales del binario.
        - Clave para interpretar correctamente los valores de `.data` y no confundir representación con contenido.

    - [Igor's Tip #94: Variable-sized structures](https://hex-rays.com/blog/igors-tip-of-the-week-94-variable-sized-structures)
        - Definir structs en Local Types con sintaxis C, importarlas a la IDB y aplicarlas a una dirección; cómo redimensionar arrays/campos con `*`.
        - Es justo el flujo del ejercicio de clase: pasar de offsets anónimos a los campos con nombre de la struct `Config`.

    - [Igor's Tip #45: Decompiler types](https://hex-rays.com/blog/igors-tip-of-the-week-45-decompiler-types)
        - Qué significan los tipos que el decompilador inventa cuando no conoce el real: `_BYTE`, `_WORD`, `_DWORD`, `_QWORD`, etc.
        - Ayuda a leer el pseudocódigo sin asustarse cuando aún no has definido los tipos correctos.

- **Bloque 6 - Decompilador y vistas sincronizadas**
    - [Igor's Tip #40: Decompiler basics](https://hex-rays.com/blog/igors-tip-of-the-week-40-decompiler-basics)
        - Cómo invocar el decompilador (`F5` para una vista nueva, `Tab` para alternar) y cómo saltar entre pseudocódigo y desensamblado.
        - Advierte de un fallo típico: el decompilador de 32/64 bits debe coincidir con la versión de IDA usada.

    - [Igor's Tip #38: Hex view](https://hex-rays.com/blog/igors-tip-of-the-week-38-hex-view)
        - La vista Hex con los bytes crudos y cómo sincronizarla con IDA View o el pseudocódigo ("Synchronize with").
        - Permite localizar literales como `r3v3rs3_m3` y los campos de `cfg` directamente sobre los bytes.

- **Bloque 7 - Rebase, GDB y patching**
    - [Igor's Tip #168: Rebasing](https://hex-rays.com/blog/igors-tip-of-the-week-168-rebasing)
        - Qué es el imagebase y por qué las direcciones de IDA pueden no coincidir con las del proceso en memoria (ASLR), y cómo ajustarlo con `Edit > Segments > Rebase program`.
        - Imprescindible para que `0x1258` cuadre con la dirección real del proceso antes de poner el breakpoint.

    - [Igor's Tip #37: Patching](https://hex-rays.com/blog/igors-tip-of-the-week-37-patching)
        - Parchear con `Edit > Patch program > Change byte` y, lo crucial, volcar los cambios al fichero con `Apply patches to input file`.
        - Recalca que por defecto los parches solo afectan a la IDB; el binario en disco no cambia hasta que lo aplicas explícitamente.

    - [Documentación oficial de GDB](https://sourceware.org/gdb/documentation)
        - Referencia del depurador: breakpoints (`break *0x1258`), `run`, e inspección de registros y memoria.
        - Base para verificar en ejecución que el binario se comporta como esperas tras el parche.

    - [PwnDbg (extensión de GDB)](https://pwndbg.re)
        - Mejora GDB para reversing/explotación: registros, pila, memoria y desensamblado en tiempo real en cada parada.
        - Hace el análisis dinámico mucho más cómodo que GDB a secas.

### Binarios
- [`resources/target.c`](resources/target.c)
    - Binario utilizado durante la clase
    - Proceso compilación:
        ```
        gcc -O0 -m64 -o target target.c
        ```