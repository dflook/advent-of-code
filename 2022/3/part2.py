import string
from pathlib import Path
from typing import Set, Iterable


def read(p: str) -> Iterable[Iterable[Set]]:
    group = []

    for line in Path(p).read_text().splitlines():
        group.append(set(line))

        if len(group) == 3:
            yield group
            group = []

    assert not group

def find_badge(group: Iterable[Set]) -> str:
    return set.intersection(*group).pop()


def priority(item: str) -> int:
    return string.ascii_letters.index(item) + 1


sum = 0
for group in read('input.txt'):
    print(f'{group=}')

    badge = find_badge(group)
    print(f'{badge=}')
    print(f'{priority(badge)=}')
    sum += priority(badge)

print(sum)
