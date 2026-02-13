# cpu.py - Our Virtual CPU!

# Opcode definitions (at the top of your file)
# HALT = 0
# LOAD = 1
# ADD = 2
# SUB = 3
# MUL = 4
# STORE = 5
# LOAD_MEM = 6


# ===== CPU STATE =====
registers = [0, 0, 0, 0]  # R0, R1, R2, R3

# create a memory
memory = [0] * 256
pc = 0  # Program Counter - tracks which instruction to execute next


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


# ===== PROGRAM =====
program = [
    (1, 0, 10),      # LOAD R0, 10      → [10, 0, 0, 0]
    (1, 1, 3),       # LOAD R1, 3       → [10, 3, 0, 0]
    (2, 2, 0, 1),    # ADD R2, R0, R1   → [10, 3, 13, 0]  (10 + 3 = 13)
    (3, 3, 0, 1),    # SUB R3, R0, R1   → [10, 3, 13, 7]  (10 - 3 = 7)
    (4, 2, 1, 3),    # MUL R2, R1, R3   → [10, 3, 21, 7]  (3 * 7 = 21)
    (5, 2, 50),      # STORE R2, [50]   → [10, 3, 21, 7]  MEM[50] = 21
    (6, 0, 50),      # LOAD_MEM R0, [50]→ [21, 3, 21, 7]  R0 = MEM[50]
    (0,),            # HALT             → Stop!
]


# ===== FETCH-DECODE-EXECUTE LOOP ======
while pc < len(program):
    instruction = program[pc]  # FETCH

    # DECODE and EXECUTE
    opcode = instruction[0]  # First element is the instruction name

    # Opcode 1: LOAD
    if opcode == 1:
        r_dest_load = instruction[1]
        value_load = instruction[2]
        load(r_dest_load, value_load)

    # Opcode 2: ADD
    elif opcode == 2:
        r_dest_add = instruction[1]
        r_src1_add = instruction[2]
        r_src2_add = instruction[3]
        add(r_dest_add, r_src1_add, r_src2_add)

    # Opcode 3: SUB
    elif opcode == 3:
        r_dest_sub = instruction[1]
        r_src1_sub = instruction[2]
        r_src2_sub = instruction[3]
        sub(r_dest_sub, r_src1_sub, r_src2_sub)

    # Opcode 4: MUL
    elif opcode == 4:
        r_dest_mul = instruction[1]
        r_src1_mul = instruction[2]
        r_src2_mul = instruction[3]
        mul(r_dest_mul, r_src1_mul, r_src2_mul)

    # Opcode 5: STORE
    elif opcode == 5:
        r_src_store = instruction[1]
        memory_dest_store = instruction[2]
        store_mem(r_src_store, memory_dest_store)

    # Opcode 6: LOAD_MEM
    elif opcode == 6:
        r_dest_load_memory = instruction[1]
        memory_src_load = instruction[2]
        load_mem(r_dest_load_memory, memory_src_load)

    # Opcode 0: HALT
    elif opcode == 0:
        break

    pc += 1  # Move to next instruction

    # print registers every iteration
    print(registers)
