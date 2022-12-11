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
        self.cycle_number = 1
        self.strengths = []

        self.emit_strength = 20

    @property
    def signal_strength(self) -> int:
        return self.cycle_number * self.x

    def cycle(self):
        self.cycle_number += 1

        if self.cycle_number == self.emit_strength:
            self.emit_strength += 40
            self.strengths.append(self.signal_strength)

            print(f'At {self.cycle_number=} {self.x=} {self.signal_strength=}')

    def total_strength(self) -> int:
        return sum(self.strengths)

    def execute(self, instruction: Instruction):
        print(instruction)

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

print(cpu.strengths)
print(cpu.total_strength())
