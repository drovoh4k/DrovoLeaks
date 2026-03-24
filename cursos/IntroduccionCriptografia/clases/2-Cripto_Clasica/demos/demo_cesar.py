from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.rule import Rule

console = Console()


def wait(message="\nPulsa ENTER para continuar..."):
    input(message)


def normalize_text(text):
    replacements = {
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
    return "".join(replacements.get(c, c.upper()) for c in text)


def caesar_encrypt(text, k):
    text = normalize_text(text)
    result = ""

    for c in text:
        if c.isalpha():
            base = ord("A")
            result += chr((ord(c) - base + k) % 26 + base)
        else:
            result += c

    return result


def caesar_decrypt(text, k):
    return caesar_encrypt(text, -k)


def show_intro():
    console.print(
        Panel.fit(
            "[bold cyan]Caesar Cipher Demo[/bold cyan]\n\n"
            "[white]"
            "En esta demo veremos paso a paso:\n"
            "1) Como funciona el cifrado Cesar\n"
            "2) Como se descifra cuando conocemos la clave\n"
            "3) Como puede atacarse por fuerza bruta\n"
            "4) Como reconocer la clave correcta entre todos los intentos\n"
            "[/white]",
            border_style="cyan",
        )
    )
    wait()


if __name__ == "__main__":
    text = "HOLA"
    k = 3

    KEY_STYLE = "cyan"
    TEXT_STYLE = "yellow"
    RESULT_STYLE = "green"

    show_intro()

    console.print(Rule("[bold yellow]1. IDEA BASICA DEL CIFRADO CESAR[/bold yellow]"))
    console.print(
        "[white]"
        "El cifrado Cesar desplaza cada letra un numero fijo de posiciones\n"
        "dentro del alfabeto.\n\n"
        "Si la clave es 3:\n"
        "- A pasa a D\n"
        "- B pasa a E\n"
        "- C pasa a F\n\n"
        "Todas las letras se mueven exactamente lo mismo.\n"
        "Esa es la idea central del metodo."
        "[/white]"
    )
    wait()

    cipher = caesar_encrypt(text, k)

    table_enc = Table(title="Cifrado")
    table_enc.add_column("Texto plano", style=TEXT_STYLE)
    table_enc.add_column("Clave", style=KEY_STYLE)
    table_enc.add_column("Texto cifrado", style=RESULT_STYLE)
    table_enc.add_row(normalize_text(text), str(k), cipher)
    console.print(table_enc)

    console.print(
        "[white]"
        "Aqui partimos del texto plano y aplicamos el mismo desplazamiento\n"
        "a todas sus letras.\n\n"
        "Como la clave es 3, el resultado final es el texto cifrado mostrado arriba."
        "[/white]"
    )
    wait()

    console.print(
        Rule("[bold yellow]2. DESCIFRADO CUANDO CONOCEMOS LA CLAVE[/bold yellow]")
    )
    console.print(
        "[white]"
        "Si conocemos la clave, descifrar es muy facil.\n\n"
        "Solo hay que deshacer el desplazamiento:\n"
        "en lugar de mover 3 posiciones hacia delante,\n"
        "movemos 3 posiciones hacia atras."
        "[/white]"
    )
    wait()

    plain = caesar_decrypt(cipher, k)

    table_dec = Table(title="Descifrado")
    table_dec.add_column("Texto cifrado", style=TEXT_STYLE)
    table_dec.add_column("Clave", style=KEY_STYLE)
    table_dec.add_column("Texto recuperado", style=RESULT_STYLE)
    table_dec.add_row(cipher, str(k), plain)
    console.print(table_dec)

    console.print(
        "[white]"
        "Como usamos la clave correcta, recuperamos exactamente el mensaje original.\n\n"
        "El problema interesante aparece cuando el atacante no conoce esa clave."
        "[/white]"
    )
    wait()

    console.print(Rule("[bold yellow]3. ATAQUE POR FUERZA BRUTA[/bold yellow]"))
    console.print(
        "[white]"
        "En el cifrado Cesar solo existen 26 desplazamientos posibles\n"
        "si trabajamos con el alfabeto A-Z.\n\n"
        "Eso significa que un atacante puede probar todas las claves,\n"
        "una por una, hasta encontrar una salida con sentido.\n\n"
        "A esto se le llama ataque por fuerza bruta."
        "[/white]"
    )
    wait()

    table_brute = Table(title="Ataque por fuerza bruta")
    table_brute.add_column("Clave probada", justify="right", style=KEY_STYLE)
    table_brute.add_column("Resultado obtenido", style="white")

    console.print(
        "[white]"
        "Ahora iremos probando cada clave posible.\n"
        "En cada paso se intenta un desplazamiento distinto\n"
        "y se observa el texto que produce.\n\n"
        "Cuando aparezca una palabra legible y coherente,\n"
        "probablemente habremos encontrado la clave correcta."
        "[/white]"
    )
    wait()

    for i in range(26):
        attempt = caesar_decrypt(cipher, i)

        if attempt == normalize_text(text):
            table_brute.add_row(str(i), f"[bold green]{attempt} <-- correcta[/]")
        else:
            table_brute.add_row(str(i), attempt)

        console.clear()
        console.print(
            Panel.fit(
                "[bold cyan]Caesar Cipher Demo[/bold cyan]\n"
                "[white]Probando todas las claves posibles paso a paso[/white]",
                border_style="cyan",
            )
        )
        console.print()
        console.print(Rule("[bold yellow]4. OBSERVACION DE LOS INTENTOS[/bold yellow]"))
        console.print(
            "[white]"
            "Cada fila nueva representa un intento de descifrado.\n"
            "La clave probada aparece a la izquierda y el texto resultante a la derecha.\n\n"
            "La clave correcta es la que reconstruye un mensaje comprensible."
            "[/white]"
        )
        console.print()
        console.print(table_brute)
        wait()

    console.print(Rule("[bold yellow]5. CONCLUSION[/bold yellow]"))
    console.print(
        "[white]"
        "El cifrado Cesar es facil de entender, pero tambien muy debil.\n\n"
        "Como solo hay unas pocas claves posibles, se puede romper\n"
        "probando todas en muy poco tiempo.\n\n"
        "Por eso tiene valor historico y didactico,\n"
        "pero no ofrece seguridad real frente a un atacante."
        "[/white]"
    )
    wait("\nFin de la demo. Pulsa ENTER para salir...")
