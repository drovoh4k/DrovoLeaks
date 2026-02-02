.intel_syntax noprefix
.text
.global main

main:
    push rbp
    mov  rbp, rsp

    # rax = 10
    mov  rax, 10

    # add/sub (64-bit)
    add  rax, 7       # rax = 17
    sub  rax, 3       # rax = 14

    # xor/and/or (bitwise 64-bit)
    xor  rax, 0x55    # rax ^= 0x55
    and  rax, 0xFF    # rax &= 0xFF
    or   rax, 0x10    # rax |= 0x10

    # inc/dec
    inc  rax
    dec  rax

    # return (int)
    mov  eax, eax
    leave
    ret
