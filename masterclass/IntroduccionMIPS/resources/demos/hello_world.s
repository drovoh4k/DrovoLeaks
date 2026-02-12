.section .data
msg:
    .ascii  "Hello world!\n"
    len = . - msg

.section .text

.global __start

__start:
main:
    # v0 = __NR_write = 4004 (o32)
    li      $v0, 4004
    li      $a0, 1          # fd = 1 (stdout)
    la      $a1, msg        # buf
    li      $a2, len        # count
    syscall

    # v0 = __NR_exit = 4001 (o32)
    li      $v0, 4001
    li      $a0, 0          # status = 0
    syscall
