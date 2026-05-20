import sys
import pygame
import pyperclip

# ==========================================
# MAZE FIJO (10x10)
# A3 = camino
# A2 = pared
# ==========================================
maze = [
    0xA3, 0xA3, 0xA3, 0xA2, 0xA3, 0xA3, 0xA3, 0xA2, 0xA3, 0xA2,
    0xA3, 0xA3, 0xA3, 0xA3, 0xA2, 0xA3, 0xA2, 0xA3, 0xA3, 0xA2,
    0xA3, 0xA3, 0xA2, 0xA3, 0xA3, 0xA3, 0xA3, 0xA2, 0xA3, 0xA2,
    0xA3, 0xA3, 0xA3, 0xA3, 0xA2, 0xA3, 0xA3, 0xA2, 0xA3, 0xA2,
    0xA3, 0xA3, 0xA2, 0xA3, 0xA3, 0xA2, 0xA3, 0xA3, 0xA2, 0xA3,
    0xA3, 0xA2, 0xA3, 0xA3, 0xA3, 0xA3, 0xA3, 0xA2, 0xA2, 0xA3,
    0xA3, 0xA2, 0xA2, 0xA2, 0xA3, 0xA2, 0xA3, 0xA3, 0xA2, 0xA2,
    0xA3, 0xA2, 0xA2, 0xA3, 0xA3, 0xA3, 0xA3, 0xA3, 0xA2, 0xA2,
    0xA3, 0xA3, 0xA3, 0xA3, 0xA3, 0xA3, 0xA2, 0xA3, 0xA3, 0xA3,
    0xA2, 0xA2, 0xA3, 0xA3, 0xA2, 0xA2, 0xA3, 0xA3, 0xA3, 0xA3
]

# ==========================================
# CONFIGURACIÓN
# ==========================================
FILAS = 10
COLUMNAS = 10
TAM_CELDA = 150
MARGEN = 2
HEADER_ALTO = 90

INICIO = (0, 0)
FIN = (9, 9)

COLOR_FONDO = (30, 30, 30)
COLOR_HEADER = (15, 15, 15)
COLOR_PANEL = (20, 20, 20)
COLOR_A2 = (245, 214, 66)
COLOR_A3 = (40, 80, 180)
COLOR_REJILLA = (0, 0, 0)
COLOR_TEXTO = (255, 255, 255)
COLOR_RUTA = (220, 60, 60)
COLOR_INICIO = (60, 200, 60)
COLOR_FIN = (200, 60, 200)
COLOR_ERROR = (255, 120, 120)

MOSTRAR_TODO = 0
MOSTRAR_SOLO_A3 = 1

# ==========================================
# CONSTRUIR MATRIZ DESDE MAZE FIJO
# ==========================================
if len(maze) != FILAS * COLUMNAS:
    raise ValueError(
        f"Se esperaban {FILAS * COLUMNAS} celdas, pero hay {len(maze)}"
    )

def hex_a_etiqueta(valor):
    if valor == 0xA2:
        return "A2"
    if valor == 0xA3:
        return "A3"
    raise ValueError(f"Valor no válido en maze: {valor}")

matriz = []
for i in range(FILAS):
    fila = []
    for j in range(COLUMNAS):
        fila.append(hex_a_etiqueta(maze[i * COLUMNAS + j]))
    matriz.append(fila)

ancho = COLUMNAS * TAM_CELDA
alto_tablero = FILAS * TAM_CELDA
alto_panel = 140
alto_total = HEADER_ALTO + alto_tablero + alto_panel

modo = MOSTRAR_TODO

moves_usuario = []
path_usuario = [INICIO]
mensaje = "Escribe U D L R. Ctrl+V pega. BACKSPACE borra. C limpia."

# ==========================================
# FUNCIONES DE LÓGICA
# ==========================================
def dentro(r, c):
    return 0 <= r < FILAS and 0 <= c < COLUMNAS

def es_transitable(r, c):
    return dentro(r, c) and matriz[r][c] == "A3"

def aplicar_movimiento(pos, move):
    r, c = pos
    if move == "U":
        return (r - 1, c)
    if move == "D":
        return (r + 1, c)
    if move == "L":
        return (r, c - 1)
    if move == "R":
        return (r, c + 1)
    return pos

def reconstruir_ruta():
    global path_usuario, mensaje

    path = [INICIO]
    actual = INICIO

    if not es_transitable(*INICIO):
        mensaje = "Error: la casilla inicial no es A3"
        path_usuario = [INICIO]
        return

    for i, move in enumerate(moves_usuario):
        siguiente = aplicar_movimiento(actual, move)

        if not dentro(*siguiente):
            mensaje = f"Error: paso {i + 1} sale fuera del tablero"
            path_usuario = path
            return

        if not es_transitable(*siguiente):
            mensaje = f"Error: paso {i + 1} entra en una celda A2"
            path_usuario = path
            return

        path.append(siguiente)
        actual = siguiente

    if actual == FIN:
        mensaje = "Ruta válida: has llegado al final"
    else:
        mensaje = "Ruta parcial: sigue escribiendo U D L R"

    path_usuario = path

def limpiar_ruta():
    global moves_usuario
    moves_usuario = []
    reconstruir_ruta()

def borrar_ultimo():
    global moves_usuario
    if moves_usuario:
        moves_usuario.pop()
    reconstruir_ruta()

def agregar_movimiento(move):
    global moves_usuario, path_usuario, mensaje

    move = move.upper()

    if move not in ("U", "D", "L", "R"):
        return

    if path_usuario[-1] == FIN:
        mensaje = "Ya estás en el final. Pulsa C para reiniciar."
        return

    actual = path_usuario[-1]
    siguiente = aplicar_movimiento(actual, move)

    if not dentro(*siguiente):
        mensaje = f"Movimiento inválido: {move} sale fuera del tablero"
        return

    if not es_transitable(*siguiente):
        mensaje = f"Movimiento inválido: {move} entra en una celda A2"
        return

    moves_usuario.append(move)
    path_usuario.append(siguiente)

    if siguiente == FIN:
        mensaje = "Ruta válida: has llegado al final"
        ruta = "".join(moves_usuario)
        print("Ruta válida:", ruta)
    else:
        mensaje = "Ruta parcial: sigue escribiendo U D L R"

def pegar_desde_portapapeles():
    global mensaje

    try:
        texto_clipboard = pyperclip.paste()
    except Exception as e:
        mensaje = f"Error al pegar: {e}"
        return

    if not texto_clipboard:
        mensaje = "El portapapeles está vacío"
        return

    texto_clipboard = texto_clipboard.upper()

    filtrado = []
    for ch in texto_clipboard:
        if ch in ("U", "D", "L", "R"):
            filtrado.append(ch)

    if not filtrado:
        mensaje = "No se encontraron movimientos U/D/L/R en el texto pegado"
        return

    for ch in filtrado:
        agregar_movimiento(ch)

def se_muestra(valor, modo_actual):
    if modo_actual == MOSTRAR_TODO:
        return True
    return valor == "A3"

# ==========================================
# PYGAME
# ==========================================
pygame.init()
pantalla = pygame.display.set_mode((ancho, alto_total))
pygame.display.set_caption("Visor de laberinto - Ruta manual")

fuente_celda = pygame.font.SysFont(None, int(TAM_CELDA * 0.35))
fuente_header = pygame.font.SysFont(None, 34)
fuente_info = pygame.font.SysFont(None, 40)
fuente_moves = pygame.font.SysFont(None, 52)
clock = pygame.time.Clock()

def dibujar_texto_centrado(texto, rect, fuente, color):
    render = fuente.render(texto, True, color)
    texto_rect = render.get_rect(center=rect.center)
    pantalla.blit(render, texto_rect)

def dibujar():
    pantalla.fill(COLOR_FONDO)

    # ===== HEADER =====
    pygame.draw.rect(pantalla, COLOR_HEADER, (0, 0, ancho, HEADER_ALTO))

    texto_header_1 = "[U D L R] mover | [Ctrl+V] pegar | [Backspace] borrar | [C] limpiar"
    texto_header_2 = "[Click] alternar vista | Objetivo: llegar de S a E"

    render1 = fuente_header.render(texto_header_1, True, COLOR_TEXTO)
    render2 = fuente_header.render(texto_header_2, True, COLOR_TEXTO)

    pantalla.blit(render1, (20, 15))
    pantalla.blit(render2, (20, 50))

    # ===== Tablero =====
    for fila in range(FILAS):
        for col in range(COLUMNAS):
            valor = matriz[fila][col]

            if not se_muestra(valor, modo):
                continue

            x = col * TAM_CELDA
            y = HEADER_ALTO + fila * TAM_CELDA
            rect = pygame.Rect(x, y, TAM_CELDA, TAM_CELDA)

            color = COLOR_A3 if valor == "A3" else COLOR_A2

            if (fila, col) == INICIO and valor == "A3":
                color = COLOR_INICIO
            elif (fila, col) == FIN and valor == "A3":
                color = COLOR_FIN

            if (fila, col) in path_usuario:
                color = COLOR_RUTA
                if (fila, col) == INICIO:
                    color = COLOR_INICIO
                elif (fila, col) == FIN:
                    color = COLOR_FIN

            pygame.draw.rect(pantalla, color, rect)
            pygame.draw.rect(pantalla, COLOR_REJILLA, rect, MARGEN)

            etiqueta = valor
            if (fila, col) == INICIO:
                etiqueta = "S"
            elif (fila, col) == FIN:
                etiqueta = "E"

            dibujar_texto_centrado(etiqueta, rect, fuente_celda, COLOR_TEXTO)

    # ===== Línea de ruta =====
    if len(path_usuario) >= 2:
        puntos = []
        for fila, col in path_usuario:
            cx = col * TAM_CELDA + TAM_CELDA // 2
            cy = HEADER_ALTO + fila * TAM_CELDA + TAM_CELDA // 2
            puntos.append((cx, cy))
        pygame.draw.lines(pantalla, (255, 255, 255), False, puntos, 8)

    # ===== Panel inferior =====
    panel_y = HEADER_ALTO + alto_tablero
    pygame.draw.rect(pantalla, COLOR_PANEL, (0, panel_y, ancho, alto_panel))

    texto_moves = "Moves: " + "".join(moves_usuario)
    render_moves = fuente_moves.render(texto_moves, True, COLOR_TEXTO)
    pantalla.blit(render_moves, (20, panel_y + 15))

    color_msg = COLOR_ERROR if mensaje.startswith("Error") or "inválido" in mensaje else COLOR_TEXTO
    render_msg = fuente_info.render(mensaje, True, color_msg)
    pantalla.blit(render_msg, (20, panel_y + 80))

    pygame.display.flip()

# Estado inicial
reconstruir_ruta()

# ==========================================
# LOOP PRINCIPAL
# ==========================================
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            modo = (modo + 1) % 2

        elif event.type == pygame.KEYDOWN:
            mods = pygame.key.get_mods()

            if event.key == pygame.K_v and (mods & pygame.KMOD_CTRL):
                pegar_desde_portapapeles()

            elif event.key == pygame.K_u:
                agregar_movimiento("U")

            elif event.key == pygame.K_d:
                agregar_movimiento("D")

            elif event.key == pygame.K_l:
                agregar_movimiento("L")

            elif event.key == pygame.K_r:
                agregar_movimiento("R")

            elif event.key == pygame.K_BACKSPACE:
                borrar_ultimo()

            elif event.key == pygame.K_c:
                limpiar_ruta()

    dibujar()
    clock.tick(60)
