# cpu.py - Our Virtual CPU hi testing git hub

# Step 1: Create registers
registers = [0, 0, 0, 0]  # R0, R1, R2, R3

# Step 2: Accessing registers
# registers[0] is R0
# registers[1] is R1, etc.


# Step 3: The LOAD instruction
def load(register_num, value):
    """Put a value into a register"""
    registers[register_num] = value


# Step 4: Let's test it!
print("Registers at start:", registers)

load(0, 42)  # Load 42 into R0
load(1, 100)  # Load 100 into R1

print("Registers after LOAD:", registers)
