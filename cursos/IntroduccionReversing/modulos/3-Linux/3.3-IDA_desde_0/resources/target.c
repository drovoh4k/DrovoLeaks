#include <stdio.h>
#include <string.h>
#include <unistd.h>

/* Variable global simple — la contraseña, visible en .data y en strings */
char secret[] = "r3v3rs3_m3";

/* Struct con metadatos — participa en la lógica: main consulta max_attempts */
struct Config {
    int  max_attempts;
    int  attempt_count;
    char app_name[32];
};

struct Config cfg = {
    .max_attempts  = 3,
    .attempt_count = 0,
    .app_name      = "SecureVault",
};

/* ---------------------------------------------------------------
 * Función auxiliar 1: validación
 * Usa strcmp (visible en imports) — fácil de reconstruir
 * Salto condicional parcheable: jne → je
 * --------------------------------------------------------------- */
int check_password(const char *input)
{
    int i;
    int score = 0;

    /* Bucle con contador: patrón claro en el grafo */
    for (i = 0; i < (int)strlen(input); i++) {
        if (input[i] == secret[i]) {
            score++;
        }
    }

    /* jne parcheable aquí */
    if (score == (int)strlen(secret)) {
        return 1;
    }
    return 0;
}

/* ---------------------------------------------------------------
 * Función auxiliar 2: imprimir resultado
 * Usa syscall directa write() — aparece en imports junto a libc
 * Los alumnos ven write + fd + buffer y reconstruyen el propósito
 * --------------------------------------------------------------- */
void print_result(int success)
{
    if (success) {
        write(STDOUT_FILENO, "Access granted. Welcome!\n", 25);
    } else {
        write(STDOUT_FILENO, "Wrong password.\n", 16);
    }
}

/* ---------------------------------------------------------------
 * main: bucle de intentos
 * Consulta cfg.max_attempts (la struct participa aquí)
 * Usa printf + fgets de libc
 * --------------------------------------------------------------- */
int main(void)
{
    char input[64];

    printf("[%s] Password required\n", cfg.app_name);

    /* Bucle que consume cfg.max_attempts — struct visible en grafo */
    while (cfg.attempt_count < cfg.max_attempts) {
        printf("Attempt %d/%d: ",
               cfg.attempt_count + 1,
               cfg.max_attempts);

        if (fgets(input, sizeof(input), stdin) == NULL) {
            break;
        }

        input[strcspn(input, "\n")] = '\0';
        cfg.attempt_count++;

        if (check_password(input)) {
            print_result(1);
            return 0;
        }

        print_result(0);
    }

    /* syscall write para el mensaje de bloqueo */
    write(STDOUT_FILENO, "Too many attempts. Locked.\n", 27);
    return 1;
}
