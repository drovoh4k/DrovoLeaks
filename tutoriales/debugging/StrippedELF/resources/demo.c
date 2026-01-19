#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int add(int a, int b) {
    return a + b;
}

static void greet(const char *name) {
    printf("Hola, %s!\n", name);
}

int main(int argc, char **argv) {
    const char *name = (argc > 1) ? argv[1] : "mundo";

    greet(name);

    int x = 7;
    int y = 35;
    int z = add(x, y);

    printf("add(%d, %d) = %d\n", x, y, z);

    char *buf = malloc(64);
    if (!buf) return 1;

    snprintf(buf, 64, "len(%s)=%zu", name, strlen(name));
    puts(buf);

    free(buf);
    return 0;
}