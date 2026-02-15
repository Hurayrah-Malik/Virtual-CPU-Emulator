from cpu import *

# Reset CPU state
registers = [0, 0, 0, 0]
pc = 0

# Test program: Loop 3 times
assembly_code = """
LOAD R0 0
LOAD R1 3
ADD R0 R0 1
SUB R2 R1 R0
JNZ R2 2
HALT
"""

program = assembler(assembly_code)
print("Test Program - Loop 3 times:")
print("Assembled:", program)
print("\nExecution:")

iteration = 0
while pc < len(program):
    instruction = program[pc]
    opcode = instruction[0]
    
    if opcode == 0:
        break
    elif opcode == 1:
        load(instruction[1], instruction[2])
    elif opcode == 2:
        add(instruction[1], instruction[2], instruction[3])
    elif opcode == 3:
        sub(instruction[1], instruction[2], instruction[3])
    elif opcode == 7:
        jump(instruction[1])
    elif opcode == 8:
        JNZ(instruction[1], instruction[2])
    
    pc += 1
    iteration += 1
    print(f"Step {iteration}: PC={pc}, Registers={registers}")
    
    if iteration > 20:  # Safety limit
        print("INFINITE LOOP DETECTED!")
        break

print("\nFinal state:", registers)
