import string
from pathlib import Path
from typing import Set, Tuple, Iterable


def read(p: str) -> Iterable[Tuple[Set, Set]]:
    for line in Path(p).read_text().splitlines():
        compartment_size = len(line) // 2
        left, right = line[:compartment_size], line[compartment_size:]
        yield set(left), set(right)


def misplaced_item(rucksack: Tuple[set, set]) -> str:
    left, right = rucksack
    return (left & right).pop()


def priority(item: str) -> int:
    return string.ascii_letters.index(item) + 1


sum = 0
for rucksack in read('input.txt'):
    print(f'{rucksack=}')

    item = misplaced_item(rucksack)
    print(f'{item}')

    print(f'{priority(item)=}')
    sum += priority(item)

print(sum)
