import string
from pathlib import Path
from typing import Set, Tuple, Iterable

def get_assignment(assignment: str) -> set[str]:
    start, end = assignment.split('-')
    return set(range(int(start), int(end)+1))

def read(p: str) -> Iterable[Tuple[Set, Set]]:
    for line in Path(p).read_text().splitlines():
        left, right = line.split(',')
        yield get_assignment(left), get_assignment(right)

sum = 0
for left, right in read('input.txt'):
    if left.issubset(right) or right.issubset(left):
        sum += 1

print(sum)
