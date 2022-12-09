from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


def read(inp: str) -> Iterable[Movement]:
    for line in inp.splitlines():
        direction, distance = line.split(' ')
        yield Movement(direction, int(distance))


instructions = read(Path('input.txt').read_text())


@dataclass
class Point:
    x: int
    y: int

    def __hash__(self):
        return hash(f'{self.x},{self.y}')


@dataclass
class Movement:
    direction: str
    distance: int


class Bridge:
    def __init__(self):
        self.head = Point(0, 0)
        self.tail = Point(0, 0)

    def move_head(self, direction: str):
        match direction:
            case 'U':
                self.head = Point(self.head.x, self.head.y + 1)
            case 'D':
                self.head = Point(self.head.x, self.head.y - 1)
            case 'L':
                self.head = Point(self.head.x - 1, self.head.y)
            case 'R':
                self.head = Point(self.head.x + 1, self.head.y)

    def move_tail(self):

        if abs(self.head.x - self.tail.x) == 2 and self.head.y == self.tail.y:
            self.tail.x += 1 if self.head.x > self.tail.x else -1
        elif abs(self.head.y - self.tail.y) == 2 and self.head.x == self.tail.x:
            self.tail.y += 1 if self.head.y > self.tail.y else -1
        else:
            if abs(self.head.x - self.tail.x) == 2:
                self.tail.x += 1 if self.head.x > self.tail.x else -1
                self.tail.y += 1 if self.head.y > self.tail.y else -1
            if abs(self.head.y - self.tail.y) == 2:
                self.tail.y += 1 if self.head.y > self.tail.y else -1
                self.tail.x += 1 if self.head.x > self.tail.x else -1

    def __str__(self):
        s = ''

        for y in range(4, -1, -1):
            for x in range(0, 6):
                if self.head.x == x and self.head.y == y:
                    s += 'H'
                elif self.tail.x == x and self.tail.y == y:
                    s += 'T'
                elif x == 0 and y == 0:
                    s += 's'
                else:
                    s += '.'
            s += '\n'

        return s


bridge = Bridge()
print('== Initial State ==')
print(bridge)

tail_positions = set()

for movement in instructions:
    print(f'== {movement.direction} {movement.distance} ==')
    for _ in range(movement.distance):
        bridge.move_head(movement.direction)
        bridge.move_tail()
        tail_positions.add(bridge.tail)
        print(bridge)

print(len(tail_positions))
