.section .data


.section .text

.global __start

__start:
    # Base
    li      $t0, 10
    li      $t1, 3

    # add/addu + addiu
    addu    $t2, $t0, $t1       # 13
    addiu   $t3, $t2, 7         # 20

    # subu
    subu    $t4, $t0, $t1       # 7

    # and/or/xor
    li      $t5, 0x0F0F
    li      $t6, 0x00FF
    and     $t7, $t5, $t6       # 0x000F
    or      $s0, $t5, $t6       # 0x0FFF
    xor     $s1, $t5, $t6       # 0x0FF0

    # shifts
    sll     $s2, $t1, 2         # 12
    srl     $s3, $t5, 4         # 0x00F0

    li      $s4, -8
    sra     $s5, $s4, 1         # -4

    # exit(0)
    li      $v0, 4001
    li      $a0, 0
    syscall
