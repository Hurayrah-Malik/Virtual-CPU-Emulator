# cpu.py - Our Virtual CPU

# ===== CPU STATE =====
registers = [0, 0, 0, 0]  # R0, R1, R2, R3
pc = 0  # Program Counter - tracks which instruction to execute next


# ===== INSTRUCTIONS =====
def load(r_dest, value):
    """Put a value into a register"""
    registers[r_dest] = value


def add(r_dest, r_src1, r_src2):
    """Add two registers and store result in destination"""
    registers[r_dest] = registers[r_src1] + registers[r_src2]


# ===== PROGRAM =====
program = [
    ("LOAD", 0, 5),  # Load 5 into R0
    ("LOAD", 1, 3),  # Load 3 into R1
    ("ADD", 2, 0, 1),  # Add R0 + R1, store in R2
]


# ===== FETCH-DECODE-EXECUTE LOOP =====
while pc < len(program):
    instruction = program[pc]  # FETCH

    # DECODE and EXECUTE
    opcode = instruction[0]  # First element is the instruction name

    if opcode == "LOAD":
        r_dest_load = instruction[1]
        value_load = instruction[2]
        load(r_dest_load, value_load)

    elif opcode == "ADD":
        r_dest_add = instruction[1]
        r_src1_add = instruction[2]
        r_src2_add = instruction[3]
        add(r_dest_add, r_src1_add, r_src2_add)

    pc += 1  # Move to next instruction

    # print registers every iteration
    print(registers)
