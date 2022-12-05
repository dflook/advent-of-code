import re
import string
from pathlib import Path
from typing import Set, Tuple, Iterable

def read(p: str) -> Tuple[list[list[str]], list[Tuple[int, int, int]]]:

    stacks: list[list[str]] = []
    moves: list[Tuple[int, int, int]] = []

    for line in Path(p).read_text().splitlines():

        if match := re.match(r'move (\d+) from (\d+) to (\d+)', line):
            moves.append((int(match[1]), int(match[2]), int(match[3])))
        elif '[' not in line:
            continue
        else:
            for stack_num, crate in enumerate(line[1::4]):
                if len(stacks) <= stack_num:
                    stacks.append([])

                if crate == ' ':
                    continue

                stacks[stack_num].insert(0, crate)

    return stacks, moves

stacks, moves = read('input.txt')

print(stacks)
print(moves)

for quantity, source, dest in moves:
    for _ in range(quantity):
        stacks[dest-1].append(stacks[source-1].pop())
        print(stacks)

print(''.join(s.pop() for s in stacks))

