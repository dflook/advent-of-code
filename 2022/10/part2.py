from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Any

Instruction = list[Any]

def read(inp: str) -> Iterable[Instruction]:
    for line in inp.splitlines():
        yield line.split()
class Cpu:

    def __init__(self):
        self.x = 1
        self.cycle_number = 0

        self.crt = ''

    @property
    def signal_strength(self) -> int:
        return self.cycle_number * self.x

    def cycle(self):
        self.cycle_number += 1

        h_pos = self.cycle_number % 40
        if h_pos + 1 >= self.x >= h_pos - 1:
            self.crt += '#'
        else:
            self.crt += '.'


        if self.cycle_number % 40 == 0:
            self.crt += '\n'

    def execute(self, instruction: Instruction):
        self.cycle()

        match instruction:
            case ['noop']:
                pass
            case ['addx', operand]:
                self.x += int(operand)
                self.cycle()


def run_program(instructions: Iterable[Instruction]) -> Cpu:
    cpu = Cpu()

    for instruction in instructions:
        cpu.execute(instruction)

    return cpu

instructions = read(Path('input.txt').read_text())
cpu = run_program(instructions)
print(cpu.crt)