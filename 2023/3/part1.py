import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Tuple, Union

@dataclass
class Item:
    value: int
    x: int
    y: int
    width: int

@dataclass
class Symbol:
    value: str
    x: int
    y: int

def read_schematic_line(line: str) -> Iterable[Tuple[int, Union[str]]]:
    value = None

    for x, char in enumerate(line):
        if char.isdigit():
            if value is None:
                value = char
            else:
                value += char
        else:
            if value is not None:
                yield x, value
                value = None

        if not char.isdigit() and char != '.':
            yield x, char

    if value is not None:
        yield x, value

def read_schematic(input: str) -> Tuple[Iterable[Item], Iterable[Symbol]]:

    items = []
    symbols = []

    for y, line in enumerate(input.splitlines()):
        for x, value in read_schematic_line(line):

            if value[0].isdigit():
                items.append(Item(int(value), x-len(value), y, len(value)))
            else:
                symbols.append(Symbol(value, x, y))

    return items, symbols

def is_part(item: Item, symbols: Iterable[Symbol]) -> bool:

    for symbol in symbols:
        if symbol.x >= item.x - 1 and symbol.x <= item.x + item.width and symbol.y >= item.y - 1 and symbol.y <= item.y + 1:
            return True

    return False

def answer(input: str) -> str:

    items, symbols = read_schematic(input)

    sum = 0

    for symbol in symbols:
        print(f'Found {symbol=}')

    for item in items:
        print(f'Found {item=}')

        if is_part(item, symbols):
            sum += item.value
            print('It\'s a part!')

    return sum

#print(answer(Path('test.txt').read_text()))
print(answer(Path('input.txt').read_text()))
