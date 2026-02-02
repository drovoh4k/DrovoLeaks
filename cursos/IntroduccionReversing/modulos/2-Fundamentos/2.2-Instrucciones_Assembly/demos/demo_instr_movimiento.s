.intel_syntax noprefix
.text
.global main

main:
    push rbp
    mov  rbp, rsp
    sub  rsp, 16

    # mov: inmediato -> memoria (local 64-bit)
    mov  QWORD PTR [rbp-8], 0x2A # local = 42

    # lea: dirección (no dereferencia)
    lea  rax, [rbp-8]            # rax = &local

    # mov: memoria -> registro (aquí sí dereferencia)
    mov  rbx, QWORD PTR [rbp-8]  # rbx = local (valor)

    # push/pop: guardar/restaurar un registro
    push rbx
    xor  rbx, rbx                # rbx = 0
    pop  rbx                     # rbx vuelve a 42

    # devolver 42 como exit code (0..255, se queda con el byte bajo)
    mov  eax, ebx                # main retorna int (EAX)

    leave
    ret
