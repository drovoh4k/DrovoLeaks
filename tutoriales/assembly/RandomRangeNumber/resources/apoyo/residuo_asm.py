#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import random
import sys
from typing import Optional, Tuple, List, Dict

MASK32 = (1 << 32) - 1
MASK64 = (1 << 64) - 1

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
MAGENTA = "\033[35m"
CIAN = "\033[36m"


ANCHO_ASM_DEFAULT = 42
INDENT_SIGNIFICADO = 2 + ANCHO_ASM_DEFAULT + 2

def _soporta_color() -> bool:
    return sys.stdout.isatty()


if not _soporta_color():
    RESET = BOLD = DIM = ROJO = VERDE = AMARILLO = AZUL = MAGENTA = CIAN = ""


def a_uint32(x: int) -> int:
    return x & MASK32


def a_int32(u: int) -> int:
    u &= MASK32
    return u if u < 0x80000000 else u - 0x100000000


def parsear_entero(texto: str) -> int:
    t = texto.strip().lower()
    return int(t, 16) if t.startswith("0x") else int(t, 10)


def _fmt_hex32(x: int) -> str:
    return f"0x{x & MASK32:08X}"


def caja(titulo: str, color: str = CIAN) -> None:
    linea = "─" * (len(titulo) + 2)
    print(f"\n{color}{BOLD}┌{linea}┐{RESET}")
    print(f"{color}{BOLD}│ {titulo} │{RESET}")
    print(f"{color}{BOLD}└{linea}┘{RESET}")


def pausa(msg: str = "ENTER para continuar...") -> None:
    input(f"{AMARILLO}{msg}{RESET}")


def pausa_siguiente_ronda() -> None:
    """
    Pausa entre rondas: evita que aparezca un nuevo dividendo inmediatamente
    después de mostrar el resultado.
    """
    pausa("ENTER para generar un nuevo dividendo...")


def imprimir_dos_columnas(asm: str, significado: str, ancho_asm: int = ANCHO_ASM_DEFAULT) -> None:
    izquierda = f"{MAGENTA}{asm:<{ancho_asm}}{RESET}"
    derecha = f"{CIAN}{significado}{RESET}"
    print(f"  {izquierda}  {derecha}")


def snapshot_registros(
    *,
    eax: Optional[int] = None,
    edx: Optional[int] = None,
    ecx: Optional[int] = None,
    rdx: Optional[int] = None,
    extra: Optional[str] = None,
    indent: int = INDENT_SIGNIFICADO,
) -> None:
    """Imprime un snapshot de registros alineado con la columna de significado."""
    partes: List[str] = []
    if eax is not None:
        v = eax & MASK32
        partes.append(f"EAX={v} ({_fmt_hex32(v)})")
    if edx is not None:
        v = edx & MASK32
        partes.append(f"EDX={v} ({_fmt_hex32(v)})")
    if ecx is not None:
        v = ecx & MASK32
        partes.append(f"ECX={v} ({_fmt_hex32(v)})")
    if rdx is not None:
        v = rdx & MASK64
        partes.append(f"RDX={v} (0x{v:016X})")

    pref = " " * indent
    if partes:
        print(f"{DIM}{pref}" + " | ".join(partes) + f"{RESET}")
    if extra:
        print(f"{DIM}{pref}{extra}{RESET}")


def imprimir_nota_alineada(texto: str, indent: int = INDENT_SIGNIFICADO) -> None:
    pref = " " * indent
    print(f"{DIM}{pref}{texto}{RESET}")


def _puntos_prueba(divisor: int) -> List[int]:
    return [
        0, 1, max(0, divisor - 1), divisor, divisor + 1,
        2 * divisor - 1, 2 * divisor,
        1234,
        (1 << 32) - 1, (1 << 32) - 123,
        (1 << 31), (1 << 31) - 1,
    ]


def buscar_k_m_u32_con_traza(divisor: int, max_s: int = 32) -> Tuple[Optional[int], Optional[int], Optional[int], List[Dict]]:
    if divisor <= 1:
        return None, None, None, []

    traza: List[Dict] = []
    pruebas = _puntos_prueba(divisor)

    for s in range(max_s + 1):
        k = 32 + s
        m = math.ceil((1 << k) / divisor)
        cabe_32 = (m < (1 << 32))

        fila = {
            "s": s, "k": k, "m": m, "cabe_32": cabe_32,
            "ok": False, "falla_en": None, "real": None, "magic": None,
        }

        if not cabe_32:
            traza.append(fila)
            continue

        ok = True
        for dividendo in pruebas:
            x = a_uint32(dividendo)
            q_real = x // divisor
            q_magic = (x * m) >> k
            if q_real != q_magic:
                ok = False
                fila["falla_en"] = x
                fila["real"] = q_real
                fila["magic"] = q_magic
                break

        fila["ok"] = ok
        traza.append(fila)

        if ok:
            return k, m, s, traza

    return None, None, None, traza


def imprimir_traza_k(divisor: int, traza: List[Dict]) -> None:
    caja(f"BÚSQUEDA DE k PARA DIVISOR={divisor}", color=CIAN)
    print(
        f"{DIM}"
        "Probamos s=0,1,2... y como k=32+s, cada fila prueba un k distinto.\n"
        "Para cada k calculamos m=ceil(2^k/divisor) y comprobamos si el cociente coincide en puntos de prueba."
        f"{RESET}"
    )
    print()
    print(f"{BOLD}{'s':>3} {'k':>4} {'m (hex)':>12} {'m cabe 32b':>11} {'resultado':>10} detalle{RESET}")

    for fila in traza:
        s = fila["s"]
        k = fila["k"]
        m = fila["m"]
        cabe = "sí" if fila["cabe_32"] else "no"

        if fila["ok"]:
            resultado = f"{VERDE}OK{RESET}"
            detalle = f"elegido (k={k}, s={s}, m={_fmt_hex32(m)})"
        else:
            resultado = f"{ROJO}FAIL{RESET}"
            if not fila["cabe_32"]:
                detalle = "m no cabe en 32 bits"
            else:
                x = fila["falla_en"]
                detalle = f"falla en x={x} (real={fila['real']}, magic={fila['magic']})"

        print(f"{s:>3} {k:>4} {_fmt_hex32(m):>12} {cabe:>11} {resultado:>10} {detalle}")


def explicar_paso_a_paso(dividendo_in: int, divisor: int) -> None:
    divisor = int(divisor)
    dividendo_u = a_uint32(dividendo_in)
    dividendo_s = a_int32(dividendo_u)

    k, m, s, traza = buscar_k_m_u32_con_traza(divisor)
    if k is None:
        caja("ERROR", color=ROJO)
        print("No se pudo encontrar un par (k, m) didáctico para este divisor con este patrón.")
        print("Prueba con divisores típicos: 3, 5, 7, 10, 60, 100.")
        return

    caja("OBJETIVO: ALEATORIO EN UN RANGO CON %", color=AZUL)
    print(f"{AMARILLO}DIVIDENDO (simula rand()):{RESET} {dividendo_u} ({_fmt_hex32(dividendo_u)})")
    print(f"{AMARILLO}DIVISOR (tamaño del rango):{RESET} {divisor}")
    print()
    print(f"{CIAN}RESTO = DIVIDENDO % DIVISOR{RESET}")
    print(f"{CIAN}Propiedad:{RESET} 0 <= RESTO < DIVISOR  -> rango [0..{divisor-1}]")
    print(f"{DIM}Si quieres rango [1..{divisor}]: (DIVIDENDO % DIVISOR) + 1{RESET}")
    pausa()

    imprimir_traza_k(divisor, traza)
    pausa()

    caja("CÁLCULO SIN idiv: MUL + SHIFTS + RESTA", color=AZUL)
    print(f"{AMARILLO}Parámetros elegidos:{RESET} k={k}, s={s}, m={_fmt_hex32(m)}")
    print(f"{DIM}Aquí verás también la 'signed correction' (mov/sar/sub) tal cual aparece en tu asm.{RESET}")
    pausa()

    eax = dividendo_u
    edx = 0
    ecx = 0
    rdx = 0

    caja("PASO 0", color=CIAN)
    imprimir_dos_columnas("call rand", "obtenemos un DIVIDENDO (aquí ya lo tenemos)")
    imprimir_dos_columnas("mov eax, DIVIDENDO", "EAX contiene el dividendo")
    snapshot_registros(eax=eax, extra=f"Interpretación signed: int32(DIVIDENDO) = {dividendo_s}")
    pausa()

    caja("PASO 1", color=CIAN)
    imprimir_dos_columnas("movsxd rdx, eax", "RDX se usa como contenedor 64-bit")
    rdx = eax
    snapshot_registros(eax=eax, rdx=rdx)
    imprimir_dos_columnas(f"imul rdx, {_fmt_hex32(m)}", "P = DIVIDENDO * m (producto 64-bit)")
    rdx = (rdx * m) & MASK64
    snapshot_registros(rdx=rdx, extra=f"P = {rdx} (0x{rdx:016X})")
    pausa()

    caja("PASO 2", color=CIAN)
    imprimir_dos_columnas("shr rdx, 32", "ALTA32 = P >> 32")
    alta32_u = (rdx >> 32) & MASK32
    snapshot_registros(rdx=rdx, extra=f"ALTA32 = {alta32_u} ({_fmt_hex32(alta32_u)})")
    pausa()

    caja("PASO 3", color=CIAN)
    imprimir_dos_columnas(f"sar edx, {s}", "q0 = int32(ALTA32) >> s  (shift aritmético)")
    alta32_s = a_int32(alta32_u)
    q0 = (alta32_s >> s)
    edx = a_uint32(q0)
    snapshot_registros(edx=edx, extra=f"q0 (signed) = {q0}, q0 (en EDX uint32) = {edx}")
    pausa()

    caja("PASO 3b  |  CORRECCIÓN SIGNED", color=MAGENTA)
    imprimir_dos_columnas("mov ecx, eax", "ECX = DIVIDENDO")
    ecx = eax
    snapshot_registros(eax=eax, ecx=ecx)

    imprimir_dos_columnas("sar ecx, 31", "ECX = máscara de signo: 0 si >=0, -1 si <0")
    ecx_s = a_int32(ecx) >> 31
    ecx = a_uint32(ecx_s)
    snapshot_registros(ecx=ecx, extra=f"máscara (signed) = {ecx_s}")

    imprimir_dos_columnas("sub edx, ecx", "ajusta el cociente: EDX = q0 - máscara")
    edx_s = a_int32(edx) - a_int32(ecx)
    edx = a_uint32(edx_s)
    snapshot_registros(edx=edx, ecx=ecx, extra=f"cociente ajustado (signed) = {edx_s}")
    imprimir_nota_alineada("Nota: con rand() normalmente DIVIDENDO >= 0, por tanto máscara=0 y este ajuste no cambia nada.")
    pausa()

    caja("PASO 4", color=CIAN)
    imprimir_dos_columnas(f"imul ecx, edx, {divisor}", "ECX = COCIENTE * DIVISOR")
    cociente_s = a_int32(edx)
    ecx = a_uint32(cociente_s * divisor)
    snapshot_registros(edx=edx, ecx=ecx, extra=f"COCIENTE (signed) = {cociente_s}")
    pausa()

    caja("PASO 5", color=CIAN)
    imprimir_dos_columnas("sub eax, ecx", "RESTO = DIVIDENDO - (COCIENTE*DIVISOR)")
    resto_s = a_int32(eax) - a_int32(ecx)
    eax = a_uint32(resto_s)
    snapshot_registros(eax=eax, extra=f"RESTO (signed) = {resto_s}")
    pausa()

    caja("RESULTADO: ALEATORIO EN RANGO", color=VERDE)
    resto_u = eax
    print(f"{VERDE}RESTO{RESET} = {resto_u}  -> rango [0..{divisor-1}]")
    print(f"{DIM}Rango [1..{divisor}] sería RESTO+1 = {resto_u + 1}{RESET}")

    cociente_real = dividendo_u // divisor
    resto_real = dividendo_u % divisor
    cociente_calc = a_int32(edx)

    ok_cociente = (a_uint32(cociente_real) == a_uint32(cociente_calc))
    ok_resto = (resto_u == resto_real)

    print()
    print(f"{BOLD}Validación:{RESET}")
    print(f"  COCIENTE_calculado = {cociente_calc}  | COCIENTE_real = {cociente_real}  -> {VERDE+'OK'+RESET if ok_cociente else ROJO+'FAIL'+RESET}")
    print(f"  RESTO_calculado    = {resto_u}        | RESTO_real    = {resto_real}    -> {VERDE+'OK'+RESET if ok_resto else ROJO+'FAIL'+RESET}")


def mostrar_ejemplos_divisor() -> None:
    caja("EJEMPLOS DE DIVISOR (TAMAÑO DEL RANGO)", color=CIAN)
    ejemplos = [
        ("10",  "genera un valor en [0..9]"),
        ("60",  "genera un valor en [0..59]"),
        ("100", "genera un valor en [0..99]"),
        ("7",   "genera un valor en [0..6]"),
    ]
    print(f"{BOLD}{'DIVISOR':<10} EFECTO{RESET}")
    print(f"{'-'*10} {'-'*40}")
    for d, desc in ejemplos:
        print(f"{d:<10} {desc}")
    print(f"\n{DIM}Nota: si quieres [1..DIVISOR], usa (DIVIDENDO % DIVISOR) + 1{RESET}")


def bucle_interactivo() -> None:
    while True:
        dividendo = random.getrandbits(31)

        caja("NUEVO DIVIDENDO ALEATORIO", color=AZUL)
        print(f"{AMARILLO}DIVIDENDO (simula rand()):{RESET} {dividendo} ({_fmt_hex32(dividendo)})")

        mostrar_ejemplos_divisor()
        texto_divisor = input(f"\n{CIAN}Introduce el DIVISOR (entero > 1): {RESET}").strip()

        try:
            divisor = parsear_entero(texto_divisor)
        except ValueError:
            print(f"{ROJO}Entrada inválida.{RESET}")
            continue

        if divisor <= 1:
            print(f"{ROJO}DIVISOR inválido: debe ser > 1.{RESET}")
            continue

        explicar_paso_a_paso(dividendo, divisor)

        pausa_siguiente_ronda()


def main() -> None:
    try:
        bucle_interactivo()
    except (KeyboardInterrupt, EOFError):
        print(f"\n{AMARILLO}Interrumpido por el usuario.{RESET}")


if __name__ == "__main__":
    main()