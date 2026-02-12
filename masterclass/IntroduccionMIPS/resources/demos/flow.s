.section .data


.section .text

.global __start

__start:
    # a=7, b=12
    li      $a0, 7
    li      $a1, 12

    # if (a0 < a1) t0=1 else 0
    slt     $t0, $a0, $a1

    # si NO (a0 < a1) => a0 es el mayor
    beq     $t0, $zero, a_is_max
    nop

b_is_max:
    move    $s0, $a1
    j       call_sum
    nop

a_is_max:
    move    $s0, $a0

call_sum:
    # sum(a0,a1)
    jal     sum
    addiu   $t9, $zero, 0x1234  # delay slot: SIEMPRE se ejecuta

    move    $s1, $v0            # s1 = a0+a1

    # demo bne
    bne     $s0, $s1, not_equal
    nop

equal:
    j       done
    nop

not_equal:
    nop

done:
    # exit(0)
    li      $v0, 4001
    li      $a0, 0
    syscall

# int sum(int a0, int a1) { return a0+a1; }
sum:
    addu    $v0, $a0, $a1
    jr      $ra
    nop
