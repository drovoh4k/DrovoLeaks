.section .data


.section .text

.global __start

__start:
    # Reservar stack
    addiu   $sp, $sp, -32

    # li: cargar inmediatos
    li      $t0, 0x1111
    li      $t1, 0x2222

    # move: mover entre registros
    move    $t2, $t0

    # sw/lw: guardar/cargar en stack
    sw      $t0, 0($sp)
    sw      $t1, 4($sp)
    sw      $t2, 8($sp)

    lw      $t3, 0($sp)
    lw      $t4, 4($sp)
    lw      $t5, 8($sp)

    # Liberar stack
    addiu   $sp, $sp, 32

    # exit(0)
    li      $v0, 4001
    li      $a0, 0
    syscall
