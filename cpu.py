# starting  flag

# cpu.py  Virtual CPU!

# Opcode definitions (at the top of your file)
# HALT = 0
# LOAD = 1
# ADD = 2
# SUB = 3
# MUL = 4
# STORE = 5
# LOAD_MEM = 6
# JUMP = 7

# dictionary of the opcodes
assembly_dict = {
    "HALT": 0,
    "LOAD": 1,
    "ADD": 2,
    "SUB": 3,
    "MUL": 4,
    "STORE": 5,
    "LOAD_MEM": 6,
    "JUMP": 7,
    "JNZ": 8,
    "PUSH": 9,
    "POP": 10,
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
}


# ===== CPU STATE =====
registers = [0, 0, 0, 0]  # R0, R1, R2, R3

# create a memory
memory = [0] * 256
# stack pointer that starts at the end of memory, becasue the stack is stored at the end of memory
stack_pointer = 255


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


# jump to a given line
def jump(target_line: int):
    # tell python to modify the global pc
    global pc
    # becasue pc += 1 will run after this
    pc = target_line - 1


# jump to a given line if the given register is not 0
def JNZ(register_num, line):
    if registers[register_num] != 0:
        jump(line)


# === memory instructions ===
def store_mem(r_src, mem_dest):
    memory[mem_dest] = registers[r_src]


def load_mem(r_dest, mem_src):
    registers[r_dest] = memory[mem_src]


# push a given register value onto the stack
def push(r_src):
    global stack_pointer
    memory[stack_pointer] = registers[r_src]
    stack_pointer -= 1


# pop a value from the stack and store it in specified register
def pop(r_dest):
    global stack_pointer
    stack_pointer += 1
    registers[r_dest] = memory[stack_pointer]


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
LOAD R0 42
LOAD R1 99
PUSH R0
PUSH R1
LOAD R0 0
LOAD R1 0
POP R1
POP R0
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

    # Opcode 0: HALT
    if opcode == 0:
        break

    # Opcode 1: LOAD
    elif opcode == 1:
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

    # opcode 7: JUMP
    elif opcode == 7:
        jump(instruction[1])

    # opcode 8: JNZ
    elif opcode == 8:
        JNZ(instruction[1], instruction[2])
    # opcode 9: PUSH
    elif opcode == 9:
        push(instruction[1])

    # opcode 10: POP
    elif opcode == 10:
        pop(instruction[1])

    pc += 1  # Move to next instruction
    print(registers)  # Print after each instructionn

#  end flag
