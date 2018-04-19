#!/usr/bin/env python

import tomasulo
import sys

from tomasulo import InstructionCreator

# file = open('a.asm', 'r')


def main():
    args = sys.argv[1]
    index = args.find(' ')
    maxcycle = int(args[:index])
    asmcode = args[index:].split('\n')
    tomCall(maxcycle, asmcode)


memo = {}


def memoize(f):
    global memo

    def helper(x):
        global memo
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


@memoize
def tomCall(arg):
    maxcycle, asmcode = arg
    maxcycle = int(maxcycle)
    instructions = [
        InstructionCreator(line.split('\n')[0]) for line in asmcode.split('\n')
        # InstructionCreator('L.D F0 R1'),
        # InstructionCreator('ADD.D F2 F0 F4'),
        # # instructions = [tomasulo.Instruction('L.D', 'F0', ('R1',)),
        # tomasulo.Instruction('ADD.D', 'F2', ('F0', 'F4')),
        # tomasulo.Instruction('MUL.D', 'F4', ('F2', 'F6')),
        # tomasulo.Instruction('ADD.D', 'F6', ('F8', 'F10')),
        # tomasulo.Instruction('DADDI', 'R1', ('R1',)),
        # tomasulo.Instruction('L.D', 'F1', ('R2',)),
        # tomasulo.Instruction('MUL.D', 'F1', ('F1', 'F8')),
        # tomasulo.Instruction('ADD.D', 'F6', ('F3', 'F5')),
        # tomasulo.Instruction('DADDI', 'R2', ('R2',)),
        # tomasulo.Instruction('DADDI', 'R3', ('R3',)),
        # tomasulo.Instruction('DADDI', 'R4', ('R4',)),
        # tomasulo.Instruction('DADDI', 'R5', ('R5',)),
    ]

    return (tomasulo.run(instructions, maxcycle))


@memoize
def tomMax(arg):
    asmcode = arg
    instructions = [
        InstructionCreator(line.split('\n')[0]) for line in asmcode.split('\n')
        # InstructionCreator('L.D F0 R1'),
        # InstructionCreator('ADD.D F2 F0 F4'),
        # # instructions = [tomasulo.Instruction('L.D', 'F0', ('R1',)),
        # tomasulo.Instruction('ADD.D', 'F2', ('F0', 'F4')),
        # tomasulo.Instruction('MUL.D', 'F4', ('F2', 'F6')),
        # tomasulo.Instruction('ADD.D', 'F6', ('F8', 'F10')),
        # tomasulo.Instruction('DADDI', 'R1', ('R1',)),
        # tomasulo.Instruction('L.D', 'F1', ('R2',)),
        # tomasulo.Instruction('MUL.D', 'F1', ('F1', 'F8')),
        # tomasulo.Instruction('ADD.D', 'F6', ('F3', 'F5')),
        # tomasulo.Instruction('DADDI', 'R2', ('R2',)),
        # tomasulo.Instruction('DADDI', 'R3', ('R3',)),
        # tomasulo.Instruction('DADDI', 'R4', ('R4',)),
        # tomasulo.Instruction('DADDI', 'R5', ('R5',)),
    ]

    return (tomasulo.getMax(instructions))


if __name__ == '__main__':
    main()
