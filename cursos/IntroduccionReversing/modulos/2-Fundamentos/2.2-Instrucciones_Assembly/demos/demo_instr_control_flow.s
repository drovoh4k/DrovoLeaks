.intel_syntax noprefix
.text
.global main

main:
    push rbp
    mov  rbp, rsp
    sub  rsp, 16

    # x = 6 (local 64-bit)
    mov  QWORD PTR [rbp-8], 6

    # if (x == 6) flag=1 else flag=0
    mov  rax, QWORD PTR [rbp-8]
    cmp  rax, 6
    jne  .not_equal
.equal:
    mov  rbx, 1
    jmp  .after_if
.not_equal:
    xor  rbx, rbx              # rbx = 0
.after_if:

    # test + jcc (¿x == 0?)
    mov  rax, QWORD PTR [rbp-8]
    test rax, rax
    jz   .x_was_zero

    # loop: sum = 0+1+2+3+4
    xor  rcx, rcx              # i = 0
    xor  rdx, rdx              # sum = 0
.loop:
    add  rdx, rcx
    inc  rcx
    cmp  rcx, 5
    jl   .loop
    jmp  .after_test

.x_was_zero:
    xor  rdx, rdx

.after_test:
    # helper(x, sum)
    mov  rdi, QWORD PTR [rbp-8] # arg1 = x
    mov  rsi, rdx               # arg2 = sum
    call helper                 # rax = helper(x, sum)

    # mezcla con flag del if
    add  rax, rbx

    # return int
    mov  eax, eax
    leave
    ret

# long helper(long a, long b) { return a + b + 3; }
helper:
    push rbp
    mov  rbp, rsp

    mov  rax, rdi
    add  rax, rsi
    add  rax, 3

    leave
    ret
