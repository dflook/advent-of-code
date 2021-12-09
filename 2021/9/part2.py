import sys
from dataclasses import dataclass
from typing import List

@dataclass
class Point:
    height: int
    basin: int = None

    def __str__(self):
        return str(self.height)

    def __repr__(self):
        return str(self.height)


def read():
    map: List[List[Point]] = []

    with open('input.txt') as f:
        for line in f.readlines():
            map.append([Point(int(x)) for x in line.strip()])

    return map


def seed_basins(map):
    basin_count = 0
    for row in range(len(map)):
        for col in range(len(map[row])):

            this = map[row][col].height

            # next
            if col > 0 and this >= map[row][col - 1].height:
                continue

            # prev
            if col < len(map[row]) - 1 and this >= map[row][col + 1].height:
                continue

            # up
            if row > 0 and this >= map[row - 1][col].height:
                continue

            if row < len(map) - 1 and this >= map[row + 1][col].height:
                continue

            map[row][col].basin = basin_count
            basin_count += 1


def print_basins(map):
    print('Map')
    for row in range(len(map)):
        for col in range(len(map[row])):
            sys.stdout.write(str(map[row][col].basin) if map[row][col].basin is not None else '-')
        sys.stdout.write('\n')


def flow_until_full():
    flowed = True

    while flowed:
        flowed = False
        for row in range(len(map)):
            for col in range(len(map[row])):

                this = map[row][col].basin
                if this is None or map[row][col].height == 9:
                    continue

                # next
                if col > 0 and map[row][col - 1].height != 9:
                    if map[row][col - 1].basin is None or map[row][col - 1].basin > this:
                        map[row][col - 1].basin = this
                        flowed = True

                    # prev
                if col < len(map[row]) - 1 and map[row][col + 1].height != 9:
                    if map[row][col + 1].basin is None or map[row][col + 1].basin > this:
                        map[row][col + 1].basin = this
                        flowed = True

                # up
                if row > 0 and map[row - 1][col].height != 9:
                    if map[row - 1][col].basin is None or map[row - 1][col].basin > this:
                        map[row - 1][col].basin = this
                        flowed = True

                if row < len(map) - 1 and map[row + 1][col].height != 9:
                    if map[row + 1][col].basin is None or map[row + 1][col].basin > this:
                        map[row + 1][col].basin = this
                        flowed = True
        print_basins(map)


def count_basins(map):
    basins = {}
    for row in map:
        for col in row:
            if col.basin is None:
                continue
            basins[col.basin] = basins.get(col.basin, 0) + 1
    return basins


map = read()
seed_basins(map)
print_basins(map)
flow_until_full()

largest = sorted(count_basins(map).values())[-3:]
print(f'{largest[0] * largest[1] * largest[2]}')
# 1023660
