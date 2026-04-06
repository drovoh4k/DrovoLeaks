#!/usr/bin/env python3

def parse_bytecode(hex_string):
    bytecode = bytes.fromhex(hex_string)
    i = 0
    program = []

    while i < len(bytecode):
        opcode = bytecode[i]

        if opcode == 0x01:  # LOAD
            program.append({
                "op": "LOAD",
                "args": [bytecode[i + 1], bytecode[i + 2]]
            })
            i += 3

        elif opcode == 0x02:  # XOR
            program.append({
                "op": "XOR",
                "args": [bytecode[i + 1], bytecode[i + 2]]
            })
            i += 3

        elif opcode == 0x03:  # CMP
            program.append({
                "op": "CMP",
                "args": [bytecode[i + 1], bytecode[i + 2]]
            })
            i += 3

        elif opcode == 0x04:  # JNE
            program.append({
                "op": "JNE",
                "args": []
            })
            i += 1

        elif opcode == 0x05:  # SUCCESS
            program.append({
                "op": "SUCCESS",
                "args": []
            })
            i += 1

        elif opcode == 0x06:  # INPUT
            program.append({
                "op": "INPUT",
                "args": [bytecode[i + 1]]
            })
            i += 2

        elif opcode == 0xFF:  # HALT
            program.append({
                "op": "HALT",
                "args": []
            })
            i += 1

        else:
            program.append({
                "op": "DB",
                "args": [opcode]
            })
            i += 1

    return program


def print_program(program):
    for i, instr in enumerate(program):
        args = ", ".join(map(str, instr["args"]))
        print(f"{i:04d}: {instr['op']} {args}".rstrip())


def recover_flag(program):
    flag_chars = []

    for instr in program:
        if instr["op"] != "LOAD":
            continue

        reg = instr["args"][0]
        value = instr["args"][1]

        if reg == 1:
            decoded_char = chr(value ^ 0xAA)
            flag_chars.append(decoded_char)

    return "".join(flag_chars)


if __name__ == "__main__":

    hex_input = """
06 00 02 00 aa 01 01 e2 03 00 01 04 06 00 02 00
aa 01 01 9e 03 00 01 04 06 00 02 00 aa 01 01 ff
03 00 01 04 06 00 02 00 aa 01 01 d1 03 00 01 04
06 00 02 00 aa 01 01 dc 03 00 01 04 06 00 02 00
aa 01 01 c7 03 00 01 04 06 00 02 00 aa 01 01 f5
03 00 01 04 06 00 02 00 aa 01 01 d8 03 00 01 04
06 00 02 00 aa 01 01 99 03 00 01 04 06 00 02 00
aa 01 01 dc 03 00 01 04 06 00 02 00 aa 01 01 99
03 00 01 04 06 00 02 00 aa 01 01 d8 03 00 01 04
06 00 02 00 aa 01 01 d9 03 00 01 04 06 00 02 00
aa 01 01 99 03 00 01 04 06 00 02 00 aa 01 01 f5
03 00 01 04 06 00 02 00 aa 01 01 99 03 00 01 04
06 00 02 00 aa 01 01 c4 03 00 01 04 06 00 02 00
aa 01 01 cd 03 00 01 04 06 00 02 00 aa 01 01 9b
03 00 01 04 06 00 02 00 aa 01 01 c4 03 00 01 04
06 00 02 00 aa 01 01 99 03 00 01 04 06 00 02 00
aa 01 01 99 03 00 01 04 06 00 02 00 aa 01 01 d8
03 00 01 04 06 00 02 00 aa 01 01 d7 03 00 01 04
05 ff
    """
    hex_input = " ".join(hex_input.strip().split())

    # Parse
    program = parse_bytecode(hex_input)
    print_program(program)

    # Get Flag
    flag = recover_flag(program)
    print("\nFLAG:", flag)
