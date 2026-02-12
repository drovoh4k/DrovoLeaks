.section .data
banner:
    .ascii  "[syscalls] /etc/hostname => "
banner_end:
path:
    .asciiz "/etc/hostname"
nl:
    .asciiz "\n"


.section .text

.global __start

__start:
    # write(1, banner, banner_len)
    li      $v0, 4004
    li      $a0, 1
    la      $a1, banner
    la      $t0, banner_end
    subu    $a2, $t0, $a1
    syscall

    # fd = open("/etc/hostname", O_RDONLY=0, 0)
    li      $v0, 4005
    la      $a0, path
    li      $a1, 0
    li      $a2, 0
    syscall
    move    $s0, $v0

    # if (fd < 0) exit(1)
    slt     $t1, $s0, $zero
    bne     $t1, $zero, fail
    nop

    # reservar buffer en stack
    addiu   $sp, $sp, -160
    move    $s1, $sp

    # n = read(fd, buf, 128)
    li      $v0, 4003
    move    $a0, $s0
    move    $a1, $s1
    li      $a2, 128
    syscall
    move    $s2, $v0

    # write(1, buf, n)
    li      $v0, 4004
    li      $a0, 1
    move    $a1, $s1
    move    $a2, $s2
    syscall

    # write(1, "\n", 1)
    li      $v0, 4004
    li      $a0, 1
    la      $a1, nl
    li      $a2, 1
    syscall

    # close(fd)
    li      $v0, 4006
    move    $a0, $s0
    syscall

    # liberar buffer
    addiu   $sp, $sp, 160

    # exit(0)
    li      $v0, 4001
    li      $a0, 0
    syscall

fail:
    li      $v0, 4001
    li      $a0, 1
    syscall
