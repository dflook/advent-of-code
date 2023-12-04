import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Tuple, Union, Optional


@dataclass
class Item:
    value: int
    x: int
    y: int
    width: int

@dataclass
class Gear:
    x: int
    y: int
    _items: list[Item] = field(default_factory=list)

    def connect(self, item: Item):
        self._items.append(item)

    def ratio(self) -> int:
        if len(self._items) != 2:
            return 0

        return self._items[0].value * self._items[1].value

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

def read_schematic(input: str) -> Tuple[Iterable[Item], Iterable[Gear]]:

    items = []
    symbols = []

    for y, line in enumerate(input.splitlines()):
        for x, value in read_schematic_line(line):

            if value[0].isdigit():
                items.append(Item(int(value), x-len(value), y, len(value)))
            elif value == '*':
                symbols.append(Gear(x, y))

    return items, symbols

def is_part(item: Item, symbols: Iterable[Gear]) -> Optional[Gear]:

    for symbol in symbols:
        if symbol.x >= item.x - 1 and symbol.x <= item.x + item.width and symbol.y >= item.y - 1 and symbol.y <= item.y + 1:
            return symbol

    return None

def answer(input: str) -> str:

    items, gears = read_schematic(input)

    for symbol in gears:
        print(f'Found {symbol=}')

    for item in items:
        print(f'Found {item=}')

        if gear := is_part(item, gears):
            gear.connect(item)

    sum = 0
    for gear in gears:
        print(f'Gear {gear=}')
        sum += gear.ratio()
    return sum

#print(answer(Path('test.txt').read_text()))
print(answer(Path('input.txt').read_text()))
