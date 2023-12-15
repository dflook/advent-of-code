from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Union


def holiday_hash(s: str) -> int:
    value = 0
    for c in s:
        v = ord(c)
        value += v
        value *= 17
        value %= 256

    return value


assert holiday_hash('HASH') == 52


@dataclass
class Add:
    label: str
    focal_length: int

    def __str__(self):
        return f'Add [{self.label} {self.focal_length}] to Box {self.box}'

    @property
    def box(self) -> int:
        return holiday_hash(self.label)


@dataclass
class Remove:
    label: str

    def __str__(self):
        return f'Remove [{self.label}] from Box {self.box}'

    @property
    def box(self) -> int:
        return holiday_hash(self.label)


def read_initialization_sequence(input: str) -> Iterable[Union[Add, Remove]]:
    for op in input.strip().split(','):
        if '-' in op:
            yield Remove(op[:-1])
        elif '=' in op:
            label, focal_length = op.split('=')
            yield Add(label, int(focal_length))


def print_boxes(boxes: list[dict]):
    for i, box in enumerate(boxes):
        if box:
            print(f'Box {i}: {box}')


def focal_power(boxes: list[dict]) -> int:
    total_power = 0

    for i, box in enumerate(boxes):
        for lens_index, focal_length in enumerate(box.values()):
            total_power += (1 + i) * (lens_index + 1) * focal_length

    return total_power


def execute(initialization_sequence: Iterable[Union[Add, Remove]]) -> list[dict]:
    boxes = [{} for _ in range(256)]

    for op in initialization_sequence:
        if isinstance(op, Add):
            boxes[op.box][op.label] = op.focal_length
        elif isinstance(op, Remove):
            if op.label in boxes[op.box]:
                del boxes[op.box][op.label]

    return boxes


def answer(input: str) -> int:
    sequence = read_initialization_sequence(input)
    boxes = execute(sequence)
    return focal_power(boxes)


# print(answer(Path('test.txt').read_text()))
print(answer(Path('input.txt').read_text()))
