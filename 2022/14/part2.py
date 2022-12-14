import re
from dataclasses import dataclass
from pathlib import Path

AIR = '.'
ROCK = '#'
SAND = 'o'


@dataclass
class Point:
    x: int
    y: int

    def __hash__(self):
        return hash(f'{self.x},{self.y}')


class Cave:
    def __init__(self, slice=None):
        self.slice = slice or {}

        self.floor = 0
        self.abyss = 0

    def draw_rock(self, start, end):

        x_start = min(start.x, end.x)
        x_end = max(start.x, end.x)

        y_start = min(start.y, end.y)
        y_end = max(start.y, end.y)

        for x in range(x_start, x_end + 1):
            for y in range(y_start, y_end + 1):
                self.slice[Point(x, y)] = ROCK

                self.floor = max(y + 2, self.floor)
                self.abyss = max(y + 1, self.abyss)

    def draw_floor(self):

        min_x = min(point.x for point in self.slice) - 1000
        max_x = max(point.x for point in self.slice) + 1000

        self.draw_rock(Point(min_x, self.floor), Point(max_x, self.floor))

    def sand_count(self) -> int:
        count = 0
        for point in self.slice.values():
            if point == SAND:
                count += 1
        return count

    def get_point(self, point: Point) -> str:
        return self.slice.get(point, AIR)

    def set_point(self, point: Point, value):
        self.slice[point] = value

    def pour_sand(self) -> bool:
        sand_point = Point(500, 0)

        while True:
            if sand_point.y > self.abyss:
                raise AssertionError('This sand has fallen into the abyss')

            down = Point(sand_point.x, sand_point.y + 1)
            if self.get_point(down) == AIR:
                sand_point = down
                continue

            # Directly down is blocked

            down_left = Point(sand_point.x - 1, sand_point.y + 1)
            if self.get_point(down_left) == AIR:
                sand_point = down_left
                continue

            # Down left is blocked

            down_right = Point(sand_point.x + 1, sand_point.y + 1)
            if self.get_point(down_right) == AIR:
                sand_point = down_right
                continue

            # Down right is blocked also
            self.set_point(sand_point, SAND)
            if sand_point == Point(500, 0):
                # Full of sand
                return False

            return True

    def __repr__(self):
        return f'Cave(slice={self.slice})'

    def __str__(self):
        min_x = min(point.x for point in self.slice) - 1
        max_x = max(point.x for point in self.slice) + 1

        min_y = min(point.y for point in self.slice) - 1
        max_y = max(point.y for point in self.slice) + 1

        s = ''

        for y in range(min_y, max_y):
            for x in range(min_x, max_x):
                s += self.get_point(Point(x, y))
            s += '\n'

        return s


def read_cave(inp: str) -> Cave:
    cave = Cave()

    for input_line in inp.splitlines():
        start_point = None
        for point in re.split(r'->', input_line):
            x, y = point.strip().split(',')
            point = Point(int(x), int(y))

            if start_point:
                cave.draw_rock(start_point, point)
            start_point = point

    cave.draw_floor()
    return cave


cave = read_cave(Path('input.txt').read_text())

# print(repr(cave))
print(cave)

for point in cave.slice:
    print(point)
print(cave.slice)

while cave.pour_sand():
    pass
print(cave)
print(f'{cave.sand_count()=}')
