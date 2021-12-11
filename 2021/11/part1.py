from __future__ import annotations

from dataclasses import dataclass, field
from pprint import pprint
from typing import List


@dataclass
class Octopus:
    energy: int
    flashed: bool = False
    adjacent: List[Octopus] = field(default_factory=list)

    def __repr__(self):
        return '!' if self.flashed else str(self.energy)


def read_octopi(path):
    octopi = []
    with open(path) as f:
        for line in f.readlines():
            octopi.append([Octopus(int(energy)) for energy in line.strip()])

    def try_append(octopus: Octopus, octopi: List[List[Octopus]], r: int, c: int):
        if r < 0 or c < 0:
            return
        try:
            octopus.adjacent.append(octopi[r][c])
        except IndexError:
            pass

    for row_num in range(len(octopi)):
        for col_num in range(len(octopi[row_num])):
            octopus = octopi[row_num][col_num]
            try_append(octopus, octopi, row_num - 1, col_num - 1)  # top left
            try_append(octopus, octopi, row_num - 1, col_num)  # top above
            try_append(octopus, octopi, row_num - 1, col_num + 1)  # top right
            try_append(octopus, octopi, row_num, col_num - 1)  # left
            try_append(octopus, octopi, row_num, col_num + 1)  # right
            try_append(octopus, octopi, row_num + 1, col_num - 1)  # bottom left
            try_append(octopus, octopi, row_num + 1, col_num)  # bottom below
            try_append(octopus, octopi, row_num + 1, col_num + 1)  # bottom right

    return octopi


def step(octopi: List[List[Octopus]]) -> int:
    flash_count = 0
    flashing = []

    for row in octopi:
        for octopus in row:
            octopus.energy += 1
            if octopus.energy > 9:
                flashing.append(octopus)

    while flashing:
        flash_count += 1
        flasher = flashing.pop()
        for adjacent_octo in flasher.adjacent:
            if not adjacent_octo.flashed and adjacent_octo not in flashing:
                adjacent_octo.energy += 1
                if adjacent_octo.energy > 9:
                    print('cascading flash')
                    flashing.append(adjacent_octo)
            flasher.flashed = True

    for row in octopi:
        for octopus in row:
            if octopus.flashed:
                octopus.energy = 0
                octopus.flashed = False

    return flash_count


octopi = read_octopi('input.txt')
print('Before any steps')
pprint(octopi)

total_flashes = 0
for i in range(1, 101):
    total_flashes += step(octopi)
    print(f'After step {i}')
    pprint(octopi)

print(f'{total_flashes=}')
# 1729
