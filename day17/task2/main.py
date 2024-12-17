"""
Author: GoldenKoopa
Puzzle: Advent of Code (year=2024 ; day=17 ; task=1)
https://adventofcode.com/2024/day/17
"""

import sys
import pathlib
from icecream import ic
sys.path.append(pathlib.Path(
    __file__).parent.parent.parent.absolute().as_posix())
from utils import measure
import re
import time
import copy

"""
Registers:
    A, B, C hold ints
    
Opcode:
    3 bit int (8 instructions, first int)

    0   adv division (combo)        A/(2^O) => write to A as int
    1   bxl bitwiseXOR (literal)    BxO     => write to B
    2   bst mod 8 (combo)           O%8     => write 3 lowest bits to B
    3   jnz jump if (lteral)                => IP = O if A == 0 
    4   bxz bitwiseXOR              BxC     => write to B
    5   out output mod 8 (combo)    O%8     => write to sys.out (separated by comma if multiple)
    6   bdv division (combo)        A/(2^O) => write to B
    7   cdv division (combo)        A/(2^O) => write to C
    

Operand:
    input, second int
    - literal operand: is the number itself
    - combo operand: 0-3 are 0-3, 4 = A, 5 = B, 6 = C, 7 = undefined (will not occur in valid programs)

Instruction Pointer:
    points at current instruction
    + 2 except when jump
    when out of bounds stops programm

"""

def parseInput(inp):
    registers, program = inp.split('\n\n')
    registers = list(map(int, re.findall(r'\d+', registers)))
    program = list(map(int, re.findall(r'\d+', program)))
    return registers, program

def getComboOperand(operand, registers):
    if operand < 4:
        return operand
    if operand == 7:
        return None
    return registers[operand-4]

def executeOperation(opcode, operand, registers, out):
    match opcode:
        case 0:
            operand = getComboOperand(operand, registers)
            registers[0] = registers[0]//(2**operand)
            return False
        case 1:
            registers[1] = registers[1] ^ operand
            return False
        case 2:
            operand = getComboOperand(operand, registers)
            registers[1] = operand % 8
            return False
        case 3:
            return registers[0] != 0
        case 4:
            registers[1] = registers[1] ^ registers[2]
            return False
        case 5:
            operand = getComboOperand(operand, registers)
            out.append(operand % 8)
            return False
        case 6:
            operand = getComboOperand(operand, registers)
            registers[1] = registers[0]//(2**operand)
            return False
        case 7:
            operand = getComboOperand(operand, registers)
            registers[2] = registers[0]//(2**operand)
            return False

def run(registers, program):
    global ip
    ip = 0
    program_length = len(program)
    out = []
    while True:
        opcode, operand = program[ip:ip+2]
        jump = executeOperation(opcode, operand, registers, out)
        if jump:
            ip = getComboOperand(operand, registers)
            continue
        ip += 2
        if ip >= program_length:
            break
    return out         

def search(num, program, REGISTERS, level):
    if level > 16:
        print(num)
        exit()
    
    for i in range(8):
        registers = copy.deepcopy(REGISTERS)
        a = num * 8 + i
        registers[0] = a
        out = run(registers, program)
        
        if out[-level:] == program[-level:]:
            search(a, program, REGISTERS, level + 1)
        


@measure
def main():
    REGISTERS, program = parseInput(sys.stdin.read())
    search(0, program, REGISTERS, 1)
    


        
   
        


if __name__ == "__main__":
    main()
