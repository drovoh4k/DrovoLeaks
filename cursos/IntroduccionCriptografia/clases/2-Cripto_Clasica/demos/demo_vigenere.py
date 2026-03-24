from collections import Counter
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.rule import Rule

console = Console()

# Frecuencias relativas de las letras en español (en porcentaje)
# https://en.wikipedia.org/w/index.php?title=Letter_frequency#Relative_frequencies_of_letters_in_other_languages
FREQ_ES = {
    "A": 11.525,
    "B": 2.215,
    "C": 4.019,
    "D": 5.010,
    "E": 13.702,
    "F": 0.692,
    "G": 1.768,
    "H": 1.973,
    "I": 6.247,
    "J": 0.493,
    "K": 0.026,
    "L": 4.967,
    "M": 3.157,
    "N": 6.712,
    "O": 8.683,
    "P": 2.510,
    "Q": 0.877,
    "R": 6.871,
    "S": 7.977,
    "T": 4.632,
    "U": 3.927,
    "V": 1.138,
    "W": 0.027,
    "X": 0.515,
    "Y": 1.433,
    "Z": 0.467,
}


def pausar(mensaje="\nPulsa ENTER para continuar..."):
    input(mensaje)


def normalizar_texto(texto):
    reemplazos = {
        "Á": "A",
        "É": "E",
        "Í": "I",
        "Ó": "O",
        "Ú": "U",
        "á": "A",
        "é": "E",
        "í": "I",
        "ó": "O",
        "ú": "U",
        "Ñ": "N",
        "ñ": "N",
        "Ü": "U",
        "ü": "U",
    }

    resultado = []
    for c in texto:
        resultado.append(reemplazos.get(c, c.upper()))
    return "".join(resultado)


def limpiar(texto):
    return "".join(c for c in normalizar_texto(texto) if c.isalpha())


def vigenere_encrypt(text, key):
    text = normalizar_texto(text)
    key = limpiar(key)

    resultado = ""
    key_index = 0

    for c in text:
        if c.isalpha():
            base = ord("A")
            k = ord(key[key_index % len(key)]) - base
            resultado += chr((ord(c) - base + k) % 26 + base)
            key_index += 1
        else:
            resultado += c

    return resultado


def vigenere_decrypt(text, key):
    text = normalizar_texto(text)
    key = limpiar(key)

    resultado = ""
    key_index = 0

    for c in text:
        if c.isalpha():
            base = ord("A")
            k = ord(key[key_index % len(key)]) - base
            resultado += chr((ord(c) - base - k) % 26 + base)
            key_index += 1
        else:
            resultado += c

    return resultado


def indice_coincidencia(texto):
    n = len(texto)
    if n < 2:
        return 0

    conteo = Counter(texto)
    return sum(f * (f - 1) for f in conteo.values()) / (n * (n - 1))


def estimar_longitud_clave(ciphertext, max_len=10):
    texto = limpiar(ciphertext)

    mejor_longitud = 1
    mejor_ic = 0
    resultados = []

    for longitud in range(1, max_len + 1):
        grupos = ["" for _ in range(longitud)]

        for i, c in enumerate(texto):
            grupos[i % longitud] += c

        ic_medio = sum(indice_coincidencia(g) for g in grupos) / longitud
        resultados.append((longitud, ic_medio))

        if ic_medio > mejor_ic:
            mejor_ic = ic_medio
            mejor_longitud = longitud

    return mejor_longitud, resultados


def descifrar_cesar(texto, desplazamiento):
    resultado = ""

    for c in texto:
        x = ord(c) - ord("A")
        resultado += chr((x - desplazamiento) % 26 + ord("A"))

    return resultado


def chi_cuadrado(texto):
    n = len(texto)
    conteo = Counter(texto)
    valor = 0

    for letra in FREQ_ES:
        observada = conteo.get(letra, 0)
        esperada = FREQ_ES[letra] * n / 100

        if esperada > 0:
            valor += (observada - esperada) ** 2 / esperada

    return valor


def recuperar_clave(ciphertext, longitud_clave):
    texto = limpiar(ciphertext)
    clave = ""
    detalles = []

    for i in range(longitud_clave):
        grupo = "".join(texto[j] for j in range(i, len(texto), longitud_clave))

        mejor_desplazamiento = 0
        mejor_valor = float("inf")

        for desplazamiento in range(26):
            posible = descifrar_cesar(grupo, desplazamiento)
            valor = chi_cuadrado(posible)

            if valor < mejor_valor:
                mejor_valor = valor
                mejor_desplazamiento = desplazamiento

        letra_clave = chr(mejor_desplazamiento + ord("A"))
        clave += letra_clave
        detalles.append((i, grupo, mejor_desplazamiento, letra_clave, mejor_valor))

    return clave, detalles


def mostrar_intro():
    console.print(
        Panel.fit(
            "[bold magenta]Vigenere Cipher Suite[/bold magenta]\n\n"
            "[cyan]Demostracion completa de cifrado y criptoanalisis del cifrado de Vigenere[/cyan]\n\n"
            "[white]"
            "En esta demo veremos:\n"
            "1) Como funciona el cifrado de Vigenere\n"
            "2) Que informacion tiene un atacante\n"
            "3) Como estimar la longitud de la clave\n"
            "4) Como recuperar la clave usando frecuencias\n"
            "5) Como descifrar el mensaje sin conocer la clave\n"
            "[/white]",
            border_style="bright_blue",
        )
    )
    pausar()


def mostrar_demo_basica(texto, clave):
    console.print()
    console.print(Rule("[bold yellow]1. DEMO BASICA DE VIGENERE[/bold yellow]"))
    console.print(
        "[white]"
        "El cifrado de Vigenere usa una clave formada por varias letras.\n"
        "Cada letra de la clave indica cuanto se desplaza la letra del texto plano.\n\n"
        "Es como aplicar muchos cifrados Cesar distintos alternandose.\n"
        "[/white]"
    )
    pausar()

    cipher = vigenere_encrypt(texto, clave)
    plain = vigenere_decrypt(cipher, clave)

    table_enc = Table(title="Cifrado")
    table_enc.add_column("Texto plano", style="yellow")
    table_enc.add_column("Clave", style="cyan")
    table_enc.add_column("Texto cifrado", style="green")
    table_enc.add_row(normalizar_texto(texto), limpiar(clave), cipher)

    console.print()
    console.print(table_enc)
    console.print(
        "[white]"
        "Observa que el mismo texto plano puede producir distintos resultados\n"
        "dependiendo de la clave usada.\n"
        "[/white]"
    )
    pausar()

    table_dec = Table(title="Descifrado")
    table_dec.add_column("Texto cifrado", style="yellow")
    table_dec.add_column("Clave", style="cyan")
    table_dec.add_column("Texto recuperado", style="green")
    table_dec.add_row(cipher, limpiar(clave), plain)

    console.print()
    console.print(table_dec)
    console.print(
        "[white]"
        "Si conocemos la clave, descifrar es facil.\n"
        "El problema interesante es cuando NO conocemos la clave.\n"
        "[/white]"
    )
    pausar()


def mostrar_tabla_frecuencias_es():
    table = Table(title="Frecuencias esperadas del espanol")
    table.add_column("Letra", justify="center", style="cyan")
    table.add_column("Frecuencia (%)", justify="right", style="magenta")

    for letra, frecuencia in FREQ_ES.items():
        table.add_row(letra, f"{frecuencia:.3f}")

    console.print()
    console.print(table)
    pausar()


def mostrar_tabla_frecuencias_texto(texto):
    conteo = Counter(texto)
    total = len(texto)

    table = Table(title="Frecuencias del texto cifrado")
    table.add_column("Letra", style="cyan")
    table.add_column("Conteo", justify="right", style="yellow")
    table.add_column("Frecuencia (%)", justify="right", style="green")

    for letra in sorted(conteo):
        frecuencia = conteo[letra] / total * 100
        table.add_row(letra, str(conteo[letra]), f"{frecuencia:.2f}")

    console.print()
    console.print(table)
    pausar()


def mostrar_tabla_ic(resultados, mejor_longitud):
    table = Table(title="Indice de coincidencia por longitud de clave")
    table.add_column("Longitud", justify="right", style="cyan")
    table.add_column("IC medio", justify="right", style="magenta")
    table.add_column("Observacion", style="green")

    for longitud, ic in resultados:
        marca = (
            "[bold green]<- mejor candidata[/bold green]"
            if longitud == mejor_longitud
            else ""
        )
        table.add_row(str(longitud), f"{ic:.4f}", marca)

    console.print()
    console.print(table)
    pausar()


def mostrar_detalles_clave_paso_a_paso(detalles):
    table = Table(
        title="Recuperacion de la clave, posicion a posicion", show_lines=True
    )
    table.add_column("Posicion", justify="right", style="cyan")
    table.add_column("Grupo analizado", style="yellow")
    table.add_column("Shift", justify="right", style="magenta")
    table.add_column("Letra", justify="center", style="green")
    table.add_column("Chi^2", justify="right", style="white")

    for pos, grupo, shift, letra, chi2 in detalles:
        table.add_row(str(pos), grupo, str(shift), letra, f"{chi2:.4f}")
        console.clear()
        mostrar_cabecera_mini()
        console.print()
        console.print(Rule("[bold yellow]5. RECUPERACION DE LA CLAVE[/bold yellow]"))
        console.print(
            "[white]"
            "Cada fila representa una posicion de la clave.\n"
            "Para esa posicion tomamos todas las letras del ciphertext\n"
            "que fueron cifradas con la misma letra de la clave.\n\n"
            "Ese grupo se comporta como un Cesar.\n"
            "Probamos 26 shifts y nos quedamos con el que da el menor chi^2.\n"
            "[/white]"
        )
        console.print()
        console.print(table)
        pausar()


def mostrar_cabecera_mini():
    console.print(
        Panel.fit(
            "[bold magenta]Vigenere Cipher Suite[/bold magenta]\n"
            "[cyan]Demo de cifrado/descifrado + criptoanalisis por frecuencias[/cyan]",
            border_style="bright_blue",
        )
    )


if __name__ == "__main__":
    mostrar_intro()

    texto_plano = (
        "SOL MONTE CAMINO VIENTO LUZ SOMBRA MAR TIERRA FUEGO NUBE RIO BOSQUE "
        "ESTRELLA CIELO TRUENO LLUVIA ARENA ROCA VALLE HORIZONTE BRISA TORMENTA "
        "AURORA CREPUSCULO RELAMPAGO PRADERA CASCADA ISLA DESIERTO LAGUNA"
    )

    clave_real = "CASA"

    texto_plano = normalizar_texto(texto_plano)
    clave_real = limpiar(clave_real)

    # ---------------- DEMO SIMPLE ----------------
    mostrar_demo_basica(texto_plano, clave_real)

    # ---------------- DEMO DE ATAQUE ----------------
    console.print()
    console.print(Rule("[bold yellow]2. PREPARACION DEL ATAQUE[/bold yellow]"))
    console.print(
        "[white]"
        "Ahora simulamos un escenario real de criptoanalisis.\n\n"
        "Tenemos:\n"
        "- El texto cifrado\n"
        "- Sabemos que es Vigenere\n"
        "- NO sabemos la clave\n\n"
        "Nuestro objetivo es recuperar la clave solo analizando el texto cifrado."
        "[/white]"
    )
    pausar()

    texto_cifrado = vigenere_encrypt(texto_plano, clave_real)

    tabla_resumen = Table(title="Resumen del escenario")
    tabla_resumen.add_column("Campo", style="cyan", no_wrap=True)
    tabla_resumen.add_column("Valor", style="white")

    tabla_resumen.add_row("Texto plano", texto_plano)
    tabla_resumen.add_row("Clave real", f"[bold green]{clave_real}[/bold green]")
    tabla_resumen.add_row("Texto cifrado", f"[yellow]{texto_cifrado}[/yellow]")

    console.print()
    console.print(tabla_resumen)
    pausar()

    console.print()
    console.print(Rule("[bold yellow]3. TABLA DE FRECUENCIAS[/bold yellow]"))
    console.print(
        "[white]"
        "Los idiomas no usan todas las letras con la misma frecuencia.\n\n"
        "Por ejemplo, en espanol la E aparece mucho mas que la Z.\n\n"
        "Si conseguimos que un texto descifrado se parezca al espanol,\n"
        "probablemente hemos encontrado una buena hipotesis de descifrado.\n\n"
        "Por eso usaremos analisis de frecuencias."
        "[/white]"
    )
    pausar()

    mostrar_tabla_frecuencias_es()
    mostrar_tabla_frecuencias_texto(limpiar(texto_cifrado))

    console.print()
    console.print(
        Rule("[bold yellow]4. ESTIMACION DE LA LONGITUD DE LA CLAVE[/bold yellow]")
    )
    console.print(
        "[white]"
        "El indice de coincidencia mide cuanto se parece un texto\n"
        "a un lenguaje natural.\n\n"
        "Un texto aleatorio suele tener un IC bajo.\n"
        "Un texto en espanol suele tener un IC mas alto.\n\n"
        "Si usamos la longitud correcta de clave, cada grupo recoge letras\n"
        "cifradas con la misma posicion de la clave y empieza a parecerse mas\n"
        "a un texto natural. Por eso el IC medio suele subir.\n\n"
        "Probamos varias longitudes y comparamos sus resultados."
        "[/white]"
    )
    pausar()

    longitud_estimada, resultados_ic = estimar_longitud_clave(texto_cifrado, 8)
    mostrar_tabla_ic(resultados_ic, longitud_estimada)

    console.print()
    console.print(
        Panel.fit(
            f"[bold white]Longitud estimada:[/bold white] [bold green]{longitud_estimada}[/bold green]",
            border_style="green",
        )
    )
    pausar()

    console.print()
    console.print(Rule("[bold yellow]5. RECUPERACION DE LA CLAVE[/bold yellow]"))
    console.print(
        "[white]"
        "Ya sabemos la longitud de la clave.\n\n"
        "Ahora dividimos el texto cifrado en grupos.\n\n"
        "Si la clave tiene longitud 4, entonces:\n"
        "- posicion 0 -> letras 0, 4, 8, 12...\n"
        "- posicion 1 -> letras 1, 5, 9, 13...\n"
        "- posicion 2 -> letras 2, 6, 10...\n"
        "- posicion 3 -> letras 3, 7, 11...\n\n"
        "Cada grupo fue cifrado siempre con la misma letra de la clave.\n"
        "Eso convierte cada grupo en un problema de Cesar.\n\n"
        "Para resolver cada grupo, probamos los 26 desplazamientos posibles\n"
        "y elegimos el que mejor se parezca al espanol."
        "[/white]"
    )
    pausar()

    console.print(
        "[white]"
        "Ahora usamos chi^2.\n\n"
        "Chi^2 mide la diferencia entre:\n"
        "- las frecuencias del texto que obtenemos al probar un shift\n"
        "- las frecuencias esperadas del espanol\n\n"
        "Cuanto menor sea chi^2, mejor encaja ese resultado con el espanol\n"
        "y mas probable es que ese desplazamiento sea el correcto."
        "[/white]"
    )
    pausar()

    clave_recuperada, detalles_clave = recuperar_clave(texto_cifrado, longitud_estimada)
    mostrar_detalles_clave_paso_a_paso(detalles_clave)

    tabla_clave = Table(title="Resultado de la recuperacion de clave")
    tabla_clave.add_column("Dato", style="cyan")
    tabla_clave.add_column("Valor", style="white")

    tabla_clave.add_row("Clave real", f"[green]{clave_real}[/green]")
    tabla_clave.add_row(
        "Clave recuperada", f"[bold green]{clave_recuperada}[/bold green]"
    )
    tabla_clave.add_row(
        "Coinciden?",
        "[bold green]Si[/bold green]"
        if clave_real == clave_recuperada
        else "[bold red]No[/bold red]",
    )

    console.print()
    console.print(tabla_clave)
    pausar()

    console.print()
    console.print(Rule("[bold yellow]6. DESCIFRADO FINAL[/bold yellow]"))
    console.print(
        "[white]"
        "Si la clave recuperada es correcta, al descifrar el mensaje completo\n"
        "deberiamos obtener el texto original o uno muy parecido.\n\n"
        "Este es el ultimo paso del ataque: comprobar si la clave encontrada\n"
        "realmente explica todo el ciphertext."
        "[/white]"
    )
    pausar()

    texto_descifrado = vigenere_decrypt(texto_cifrado, clave_recuperada)

    tabla_final = Table(title="Resultado final", show_lines=True)
    tabla_final.add_column("Campo", style="cyan", no_wrap=True)
    tabla_final.add_column("Contenido", style="white")

    tabla_final.add_row("Texto cifrado", f"[yellow]{texto_cifrado}[/yellow]")
    tabla_final.add_row(
        "Texto descifrado", f"[bold green]{texto_descifrado}[/bold green]"
    )

    console.print()
    console.print(tabla_final)
    pausar("\nFin de la demo. Pulsa ENTER para salir...")
