# starting  flag

# cpu.py - Our Virtual CPU!

# Opcode definitions (at the top of your file)
# HALT = 0
# LOAD = 1
# ADD = 2
# SUB = 3
# MUL = 4
# STORE = 5
# LOAD_MEM = 6

# dictionary of the opcodes
assembly_dict = {
    "HALT": 0,
    "LOAD": 1,
    "ADD": 2,
    "SUB": 3,
    "MUL": 4,
    "STORE": 5,
    "LOAD_MEM": 6,
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
}


# ===== CPU STATE =====
registers = [0, 0, 0, 0]  # R0, R1, R2, R3

# create a memory
memory = [0] * 256
pc = 0  # Program Counter - trackss which instruction to execute next


# ===== INSTRUCTIONS =====
def load(r_dest, value):
    """Put a value into a register"""
    registers[r_dest] = value


def add(r_dest, r_src1, r_src2):
    """Add two registers and store result in destination"""
    registers[r_dest] = registers[r_src1] + registers[r_src2]


def sub(r_dest, r_src1, r_src2):
    registers[r_dest] = registers[r_src1] - registers[r_src2]


def mul(r_dest, r_src1, r_src2):
    registers[r_dest] = registers[r_src1] * registers[r_src2]


# === memory instructions ===
def store_mem(r_src, mem_dest):
    memory[mem_dest] = registers[r_src]


def load_mem(r_dest, mem_src):
    registers[r_dest] = memory[mem_src]


# convert the human readable assembly to machine code
def assembler(input: str) -> list:
    # make every line a list item
    input_list = input.strip().split("\n")

    fully_split_input = []
    # make every line , into a list
    for line in input_list:
        fully_split_input.append(line.split())

    # for every list of instructions inside of the list, change the opcode to a number
    for line in fully_split_input:
        for i in range(len(line)):
            if line[i] in assembly_dict:
                line[i] = assembly_dict[line[i]]
            else:
                line[i] = int(line[i])

    return fully_split_input


# ===== ASSEMBLE AND RUN PROGRAM =====
assembly_code = """
LOAD R0 10
LOAD R1 3
ADD R2 R0 R1
SUB R3 R0 R1
MUL R2 R1 R3
STORE R2 50
LOAD_MEM R0 50
HALT
"""

program = assembler(assembly_code)
print("Assembled program:", program)
print("\nRunning CPU:\n")

# ===== FETCH-DECODE-EXECUTE LOOP ======
while pc < len(program):
    instruction = program[pc]  # FETCH

    # DECODE and EXECUTE
    opcode = instruction[0]

    # Opcode 1: LOAD
    if opcode == 1:
        load(instruction[1], instruction[2])

    # Opcode 2: ADD
    elif opcode == 2:
        add(instruction[1], instruction[2], instruction[3])

    # Opcode 3: SUB
    elif opcode == 3:
        sub(instruction[1], instruction[2], instruction[3])

    # Opcode 4: MUL
    elif opcode == 4:
        mul(instruction[1], instruction[2], instruction[3])

    # Opcode 5: STORE
    elif opcode == 5:
        store_mem(instruction[1], instruction[2])

    # Opcode 6: LOAD_MEM
    elif opcode == 6:
        load_mem(instruction[1], instruction[2])

    # Opcode 0: HALT
    elif opcode == 0:
        break

    pc += 1  # Move to next instruction
    print(registers)  # Print after each instruction

# end flag
