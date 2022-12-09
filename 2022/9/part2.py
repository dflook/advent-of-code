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
    def __init__(self, knots: int):
        self.knots = [Point(0, 0) for _ in range(knots)]

    @property
    def head(self) -> Point:
        return self.knots[0]

    @head.setter
    def head(self, point: Point):
        self.knots[0] = point

    @property
    def tail(self) -> Point:
        return self.knots[-1]

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

    def move_knots(self):
        for leading, trailing in zip(self.knots, self.knots[1:]):
            self.move_knot(leading, trailing)

    def move_knot(self, leading: Point, trailing: Point):

        if abs(leading.x - trailing.x) == 2 and leading.y == trailing.y:
            trailing.x += 1 if leading.x > trailing.x else -1
        elif abs(leading.y - trailing.y) == 2 and leading.x == trailing.x:
            trailing.y += 1 if leading.y > trailing.y else -1
        else:
            if abs(leading.x - trailing.x) == 2:
                trailing.x += 1 if leading.x > trailing.x else -1
                trailing.y += 1 if leading.y > trailing.y else -1
            if abs(leading.y - trailing.y) == 2:
                trailing.y += 1 if leading.y > trailing.y else -1
                trailing.x += 1 if leading.x > trailing.x else -1

    def __str__(self):
        s = ''

        for y in range(21, -1, -1):
            for x in range(0, 26):
                if Point(x, y) in self.knots:
                    knot_number = self.knots.index(Point(x, y))
                    s += 'H' if knot_number == 0 else str(knot_number)
                elif x == 0 and y == 0:
                    s += 's'
                else:
                    s += '.'

            s += '\n'

        return s


bridge = Bridge(knots=10)
print('== Initial State ==')
print(bridge)

tail_positions = set()

for movement in instructions:
    print(f'== {movement.direction} {movement.distance} ==')
    for _ in range(movement.distance):
        bridge.move_head(movement.direction)
        bridge.move_knots()
        tail_positions.add(bridge.tail)
        #print(bridge)

print(len(tail_positions))
