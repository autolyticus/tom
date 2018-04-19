#!/usr/bin/env python

import tomasulo

instructions = [tomasulo.Instruction('L.D', 'F0', ('R1',)),
                tomasulo.Instruction('ADD.D', 'F2', ('F0', 'F4')),
                tomasulo.Instruction('MUL.D', 'F4', ('F2', 'F6')),
                tomasulo.Instruction('ADD.D', 'F6', ('F8', 'F10')),
                tomasulo.Instruction('DADDI', 'R1', ('R1',)),
                tomasulo.Instruction('L.D', 'F1', ('R2',)),
                tomasulo.Instruction('MUL.D', 'F1', ('F1', 'F8')),
                tomasulo.Instruction('ADD.D', 'F6', ('F3', 'F5')),
                tomasulo.Instruction('DADDI', 'R2', ('R2',)),
                tomasulo.Instruction('DADDI', 'R3', ('R3',)),
                tomasulo.Instruction('DADDI', 'R4', ('R4',)),
                tomasulo.Instruction('DADDI', 'R5', ('R5',))]

tomasulo.run(instructions)
