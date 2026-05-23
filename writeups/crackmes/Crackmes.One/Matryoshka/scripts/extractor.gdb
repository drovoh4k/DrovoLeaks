set pagination off
set confirm off

# Variables
set $BP_ADDR    = 0x0000555555555371
set $DUMP_ADDR  = 0x0000555555558080
set $DUMP_SIZE  = 0x0A9E0
set $KEY_SUM    = 0x57


# Fase 1: Extraer key (1 byte)
start

set $key = ({unsigned char}$DUMP_ADDR ^ 0x7f) + $KEY_SUM

printf "\n[+] KEY: %c (0x%02x)\n\n", $key, $key

# Fase 2: Dumpeo
delete breakpoints
break *$BP_ADDR

eval "run %c", $key

dump memory dump.bin $DUMP_ADDR ($DUMP_ADDR + $DUMP_SIZE)

printf "\n[+] Dump guardado en dump.bin (%d bytes)\n", $DUMP_SIZE

quit