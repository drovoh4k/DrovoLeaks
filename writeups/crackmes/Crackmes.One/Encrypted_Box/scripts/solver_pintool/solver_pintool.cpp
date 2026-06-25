/*
 * solver_pintool.cpp - Resolutor dinamico del reto AES (Intel Pin)
 * ================================================================
 *
 * En vez de extraer las claves de ronda a mano, deja correr el binario bajo
 * Pin y reconstruye la entrada sobre la marcha:
 *
 *   - sys_read se neutraliza: fingimos que leyo el bloque y seguimos, asi el
 *     programa no se bloquea esperando entrada del teclado.
 *
 *   - Cada vez que el binario esta a punto de comprobar una ronda AES contra
 *     un valor esperado, calculamos que entrada produce ese valor (invirtiendo
 *     la ronda) y la inyectamos. El binario se "convence" y avanza solo hasta
 *     la siguiente comprobacion. Encadenando todas se obtiene la contrasena.
 *
 * Solo se instrumentan las aesenc/aesdec cuyo destino es XMM2, que son las de
 * las comparaciones; las de los bucles de cifrado se ignoran.
 *
 * Compilar con el toolkit de Intel Pin (no con gcc).
 */
#include <stdio.h>
#include <stdint.h>
#include <string>

#include "pin.H"
#include <wmmintrin.h>          /* intrinsecos AES-NI */

static const UINT32 BLOCK = 16; /* AES trabaja en bloques de 128 bits */

/* =====================================================================
 *  Inversion de una ronda
 *
 *  Una ronda AES termina con un XOR contra la clave; ese paso es comun a
 *  aesenc y aesdec, asi que lo hacemos primero y luego nos desviamos segun
 *  el tipo de ronda. 'enc' = true si la instruccion original fue aesenc.
 *
 *  El atributo 'target' habilita AES-NI solo para esta funcion, de modo que
 *  compila aunque el build de Pin no pase -maes en los flags globales.
 * ===================================================================== */
__attribute__((target("aes,sse4.1")))
static void invert_round(uint8_t *block, const uint8_t *round_key, bool enc)
{
    const __m128i zero = _mm_setzero_si128();

    __m128i x = _mm_loadu_si128((const __m128i *)block);
    x = _mm_xor_si128(x, _mm_loadu_si128((const __m128i *)round_key));

    if (enc)
    {
        /* aesenc aplico ...MixColumns, SubBytes, ShiftRows: lo deshacemos. */
        x = _mm_aesimc_si128(x);            /* InvMixColumns                 */
        x = _mm_aesdeclast_si128(x, zero);  /* InvSubBytes + InvShiftRows    */
    }
    else
    {
        /* aesdec no tiene inverso directo en una sola instruccion; esta
         * terna reconstruye la transformacion que habia deshecho.          */
        x = _mm_aesdeclast_si128(x, zero);
        x = _mm_aesenc_si128(x, zero);
        x = _mm_aesenclast_si128(x, zero);
    }

    _mm_storeu_si128((__m128i *)block, x);
}

/* =====================================================================
 *  Estado global y argumentos
 * ===================================================================== */
KNOB<std::string> pwfile_name(KNOB_MODE_WRITEONCE, "pintool", "o",
                              "password.txt", "Fichero donde guardar la contrasena");
static FILE *pwfile = NULL;

/* =====================================================================
 *  Callbacks de analisis
 * ===================================================================== */

/* Antes de cada syscall. Solo nos interesa sys_read (numero 0). */
VOID on_syscall(ADDRINT pc, ADDRINT number, CONTEXT *ctxt)
{
    if (number != 0)
        return;

    /* Saltamos el read real: devolvemos "16 bytes leidos" y avanzamos el RIP
     * mas alla de la instruccion syscall, que ocupa 2 bytes (0F 05). */
    PIN_SetContextReg(ctxt, REG_GAX, BLOCK);
    PIN_SetContextReg(ctxt, REG_INST_PTR, pc + 2);
    PIN_ExecuteAt(ctxt);
}

/* Antes de una aesenc/aesdec de comparacion.
 *   target    = XMM0, el valor que el binario espera obtener.
 *   round_key = XMM1, la clave de esta ronda.
 *   scratch   = XMM2, registro de trabajo (destino de la instruccion).
 * Reutilizamos scratch como buffer del bloque recuperado. */
VOID recover_block(ADDRINT pc, VOID *rsp,
                   UINT8 *target, UINT8 *round_key, UINT8 *scratch, bool enc)
{
    /* Partimos del valor esperado y calculamos la entrada que lo genera. */
    if (PIN_SafeCopy(scratch, target, BLOCK) != BLOCK)
    {
        fprintf(stderr, "[%lx] no se pudo leer XMM0\n", (unsigned long)pc);
        PIN_ExitApplication(-1);
    }

    invert_round(scratch, round_key, enc);

    /* Inyectamos el bloque recuperado donde el binario lo va a leer. */
    if (PIN_SafeCopy(rsp, scratch, BLOCK) != BLOCK)
    {
        fprintf(stderr, "[%lx] no se pudo escribir en [rsp]\n", (unsigned long)pc);
        PIN_ExitApplication(-1);
    }

    /* Log y guardado, serializados por si el objetivo tiene varios hilos. */
    PIN_LockClient();
    printf("[%lx] \"", (unsigned long)pc);
    for (UINT32 i = 0; i < BLOCK; i++)
        printf("\\x%02x", scratch[i]);
    printf("\"\n");
    fwrite(scratch, 1, BLOCK, pwfile);
    PIN_UnlockClient();
}

/* =====================================================================
 *  Instrumentacion
 * ===================================================================== */
VOID instrument(INS ins, VOID *v)
{
    OPCODE op = INS_Opcode(ins);

    if (op == XED_ICLASS_SYSCALL)
    {
        INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)on_syscall,
            IARG_INST_PTR,
            IARG_REG_VALUE, REG_GAX,
            IARG_CONTEXT,
            IARG_END);
        return;
    }

    /* aesenc y aesdec comparten toda la instrumentacion salvo el flag 'enc',
     * asi que las tratamos juntas en vez de duplicar el bloque. */
    bool is_enc = (op == XED_ICLASS_AESENC);
    bool is_dec = (op == XED_ICLASS_AESDEC);
    if ((is_enc || is_dec) && INS_OperandReg(ins, 0) == REG_XMM2)
    {
        INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)recover_block,
            IARG_INST_PTR,
            IARG_REG_VALUE, REG_STACK_PTR,
            IARG_REG_REFERENCE, REG_XMM0,    /* target    */
            IARG_REG_REFERENCE, REG_XMM1,    /* round_key */
            IARG_REG_REFERENCE, REG_XMM2,    /* scratch   */
            IARG_BOOL, is_enc,
            IARG_END);
    }
}

/* =====================================================================
 *  Arranque y cierre
 * ===================================================================== */
VOID on_finish(INT32 code, VOID *v)
{
    if (pwfile)
        fclose(pwfile);
    printf("\n[+] Hecho.\n");
}

int main(int argc, char *argv[])
{
    PIN_InitSymbols();
    if (PIN_Init(argc, argv))
        return -1;

    pwfile = fopen(pwfile_name.Value().c_str(), "wb");
    if (!pwfile)
    {
        fprintf(stderr, "No se pudo abrir %s\n", pwfile_name.Value().c_str());
        return -1;
    }

    INS_AddInstrumentFunction(instrument, 0);
    PIN_AddFiniFunction(on_finish, 0);

    PIN_StartProgram();
    return 0;
}
