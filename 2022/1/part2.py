from pathlib import Path
from typing import Iterable


def count_elf_calories(input) -> Iterable[int]:
    return [sum(int(x) for x in e.splitlines()) for e in input.split('\n\n')]


input = Path('input.txt').read_text()
elf_calories = list(count_elf_calories(input))
print(sum(sorted(elf_calories)[-3:]))
