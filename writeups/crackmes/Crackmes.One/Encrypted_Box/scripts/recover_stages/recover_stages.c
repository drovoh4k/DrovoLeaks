#include <immintrin.h>
#include <stdio.h>

// Invierte UN aesenc con clave de ronda k.
// aesenc hace: ShiftRows -> SubBytes -> MixColumns -> XOR k.
static __m128i inverse_aesenc(__m128i d, __m128i k) {
    __m128i cero = _mm_setzero_si128();
    d = _mm_xor_si128(d, k);            // deshace el XOR con la clave
    d = _mm_aesimc_si128(d);            // deshace MixColumns (InvMixColumns)
    d = _mm_aesdeclast_si128(d, cero);  // deshace SubBytes + ShiftRows
    return d;
}

// Invierte UN aesdec con clave de ronda k.
// aesdec hace: InvShiftRows -> InvSubBytes -> InvMixColumns -> XOR k.
// No hay instrucción de MixColumns "hacia adelante", así que se emula
// con la secuencia aesdeclast -> aesenc -> aesenclast (efecto neto: MC, SB, SR).
static __m128i inverse_aesdec(__m128i d, __m128i k) {
    __m128i cero = _mm_setzero_si128();
    d = _mm_xor_si128(d, k);            // deshace el XOR con la clave
    d = _mm_aesdeclast_si128(d, cero);
    d = _mm_aesenc_si128(d, cero);
    d = _mm_aesenclast_si128(d, cero);  // -> el input
    return d;
}

// Vacía el fichero de salida (lo elimina si existía) para empezar limpio.
static void reset_output(const char *nombre) {
    remove(nombre);
}

// Añade los 16 bytes crudos del valor al final del fichero indicado.
// Devuelve 0 si todo fue bien, distinto de 0 en caso de error.
static int append_output(const char *nombre, __m128i valor) {
    FILE *f = fopen(nombre, "ab");      // modo append binario
    if (!f) {
        perror(nombre);
        return 1;
    }
    size_t escritos = fwrite(&valor, 1, 16, f);
    fclose(f);
    if (escritos != 16) {
        fprintf(stderr, "Error: solo se escribieron %zu de 16 bytes en %s\n", escritos, nombre);
        return 1;
    }
    return 0;
}

int main(void) {
    const char *salida = "input.bin";
    reset_output(salida);

    // --- Stage 1 (invierte aesdec) ---
    __m128i clave1    = _mm_set_epi64x(0xa16f50c4d1bfe9d0, 0xa8d01d9776210139); // xmm1 = [r11:r10]
    __m128i objetivo1 = _mm_set_epi64x(0x6d65ed24c22914c9, 0x8e33d4cb8ec85c19); // xmm0 = [r9 :r8 ]

    if (append_output(salida, inverse_aesdec(objetivo1, clave1)) != 0)
        return 1;

    // --- Stage 2 (invierte aesenc) ---
    __m128i clave2    = _mm_set_epi64x(0x42244286f11c4d34, 0xe119759fa572a0ba); // xmm1 = [r11:r10]
    __m128i objetivo2 = _mm_set_epi64x(0x0dcc5395bbc56682, 0x428716fed8251b59); // xmm0 = [r9 :r8 ]

    if (append_output(salida, inverse_aesenc(objetivo2, clave2)) != 0)
        return 1;

    return 0;
}
