# 🖥️ Virtual CPU Simulator

A simple virtual CPU built in Python that simulates a basic processor with registers, memory, a stack, and a custom assembly language. A fun from-scratch project to understand how CPUs work at a low level.

---

## Features

- **4 general-purpose registers** (R0–R3)
- **256 bytes of memory**
- **Stack** stored at the end of memory with a stack pointer
- **Custom assembler** that converts human-readable assembly code into machine code
- **Fetch-decode-execute loop** that runs programs instruction by instruction
- Support for arithmetic, memory access, control flow, stack operations, and function calls

---

## Instruction Set

| Opcode     | Syntax                    | Description                                      |
|------------|---------------------------|--------------------------------------------------|
| `HALT`     | `HALT`                    | Stop execution                                   |
| `LOAD`     | `LOAD Rx value`           | Load an immediate value into a register          |
| `ADD`      | `ADD Rx Ry Rz`            | `Rx = Ry + Rz`                                   |
| `SUB`      | `SUB Rx Ry Rz`            | `Rx = Ry - Rz`                                   |
| `MUL`      | `MUL Rx Ry Rz`            | `Rx = Ry * Rz`                                   |
| `STORE`    | `STORE Rx addr`           | Store register value into memory address         |
| `LOAD_MEM` | `LOAD_MEM Rx addr`        | Load value from memory address into register     |
| `JUMP`     | `JUMP line`               | Unconditionally jump to a line number            |
| `JNZ`      | `JNZ Rx line`             | Jump to line if register is **not zero**         |
| `PUSH`     | `PUSH Rx`                 | Push register value onto the stack               |
| `POP`      | `POP Rx`                  | Pop top of stack into a register                 |
| `CALL`     | `CALL line`               | Call a function at a line number                 |
| `RET`      | `RET`                     | Return from a function call                      |

---

## Example Programs

### Function Call
```
LOAD R2 10
CALL 3
HALT
LOAD R3 5
ADD R2 R2 R3
RET
```
Loads 10 into R2, calls a function that adds 5 to it, then returns. Result: `R2 = 15`.

### Loop
```
LOAD R0 0
LOAD R1 3
ADD R0 R0 1
SUB R2 R1 R0
JNZ R2 2
HALT
```
Counts from 0 to 3 using a loop.

---

## How to Run

**Requirements:** Python 3.x — no external libraries needed.

```bash
# Run the main CPU with the built-in example program
python cpu.py

# Run the loop test
python test_loop.py
```

---

## Project Structure

```
├── cpu.py          # Core virtual CPU — registers, memory, instructions, assembler, and run loop
├── test_loop.py    # Test program demonstrating a loop with JNZ
└── README.md
```

---

## How It Works

1. **Assembly code** is written as a multi-line string using the custom instruction set above.
2. The **assembler** (`assembler()`) parses each line, replaces mnemonics (`ADD`, `R0`, etc.) with their numeric opcodes, and returns a list of instructions.
3. The **fetch-decode-execute loop** reads one instruction at a time using the program counter (`pc`), decodes the opcode, and calls the appropriate function.
4. The **stack** grows downward from address 255 in memory, supporting `PUSH`, `POP`, `CALL`, and `RET`.
