#  ⛑️ El secreto detrás de rand() % 100

[![YouTube](https://img.shields.io/badge/YouTube-@drovoh4k-DD0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/@drovoh4k)

![tipo](https://img.shields.io/badge/tipo-tutorial-111827?style=flat-square)
![tema](https://img.shields.io/badge/tema-assembly-0969da?style=flat-square)


## 📄 Resumen

**🎥 Tutorial:** https://youtu.be/lTQ3l8pWsa8

En C, generar un número pseudoaleatorio dentro de un rango es algo trivial, por ejemplo `rand() % 100`, devuelve un valor en [0..99]

El problema es que ese "módulo" no se implementa con un idiv directo (ya que es muy caro), sino con un patrón optimizado del compilador utilizando división por constante usando multiplicación.

En este tutorial entenderemos:
- La matemática mínima para entender por qué `x % d` se puede calcular como `x - q*d`
- Por qué IDIV es tan lento comparado con multiplicaciones y shifts
- El patrón optimizado en assembly
- Un mini script interactivo en Python para jugar con dividendos/divisores y ver el cálculo paso a paso

## 📦 Recursos

### Enlaces

1. **Documentación técnica**
    - [FelixCloutier: x86 and amd64 instruction reference](https://www.felixcloutier.com/x86)
        - Referencia rápida para consultar instrucciones assembly.
        - Aunque para la resolución de los challenges de este repositorio es más que suficiente, es solo para tener una referencia.
        - Para cualquier proyecto serio, consultar documentación oficial como, por ejemplo, el [Intel® 64 and IA-32 Architectures Software Developer Manuals](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html).

2. **De apoyo**
    - [diagrama.EXCALIDRAW](resources/material_clase/diagrama.excalidraw)
        - Diagrama útilizado durante la clase.

### Documentos

1. **Para profundizar**
    - [Division by Invariant Integers using Multiplication](resources/profundizar/Division%20by%20Invariant%20Integers%20using%20Multiplication.pdf) y [Improved division by invariant integers](resources/profundizar/Improved%20division%20by%20invariant%20integers.pdf)
        - Papers donde se entra al detalle matemático de la optimización.
    
    - [Intel Optimization Reference Manual](resources/profundizar/356477-Optimization-Reference-Manual-V2-002.pdf)
        - Documento de donde he obtenido los calculos de rendimiento de las instrucciones (concretamente página 151, tabla 7-17).


### Scripts
- [residuo_asm.py](resources/apoyo/residuo_asm.py)
        - Script interactivo para profundizar en como funciona la optimización.