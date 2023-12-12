import itertools
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Iterable


@dataclass
class Galaxy:
    id: int
    x: int
    y: int

def find_sparse_columns(input: str) -> Iterable[int]:
    galaxy_columns: Optional[list[bool]] = None

    for line in input.splitlines():
        if galaxy_columns is None:
            galaxy_columns = [False for _ in range(len(line))]

        for i, c in enumerate(line):
            if c == '#':
                galaxy_columns[i] = True

    for i, column in enumerate(galaxy_columns):
        if column is False:
            yield i

def parse(input: str) -> Iterable[Galaxy]:

    sparse_columns = list(find_sparse_columns(input))

    galaxy_id = 1
    vertical = 0
    for line in input.splitlines():
        if '#' in line:
            vertical += 1
        else:
            vertical += 2
            continue

        horizontal = 0
        for i, c in enumerate(line):
            if i not in sparse_columns:
                horizontal += 1
            else:
                horizontal += 2
                continue

            if c == '#':
                yield Galaxy(galaxy_id, horizontal, vertical)
                galaxy_id += 1

def shortest_path(a: Galaxy, b: Galaxy) -> int:
    return abs(a.x - b.x) + abs(a.y - b.y)

def answer(input:str) -> int:

    galaxies = list(parse(input))
    for galaxy in galaxies:
        print(galaxy)

    cumulative_distance = 0
    for a, b in itertools.combinations(galaxies, 2):
        distance = shortest_path(a, b)
        print(a, b, distance)
        cumulative_distance += distance

    return cumulative_distance

print(answer(Path('test.txt').read_text()))