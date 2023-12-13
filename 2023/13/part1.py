from pathlib import Path
from typing import Iterable, Optional

Field = list[str]
def parse_fields(input: str) -> Iterable[Field]:
    field = []

    for line in input.splitlines():
        if not line and field:
            yield field
            field = []
            continue
        field.append(line)

    yield field

def is_reflection(field: Field, reflection_line: int) -> bool:

    print(f'Is there a reflection after line {reflection_line}')

    smudge_repaired = False

    for l_num, r_num in [(reflection_line - i, reflection_line + i + 1) for i in range(len(field))]:

        if r_num >= len(field):
            print('reflection')
            return True
        if l_num < 0:
            print('reflection')
            return True

        print(l_num, r_num)

        l = field[l_num]
        r = field[r_num]

        print(l)
        print(r)

        if l == r:
            continue

        if smudge_repaired:
            return False

        # Possibly a smudge

        if l != r:
            print('No reflection')
            return False

        print('-')

    print('reflection')
    return True

def transpose(field: Field) -> Field:
    return [''.join(column) for column in zip(*field)]

def find_reflection(field: Field) -> Optional[int]:
    for i in range(len(field) - 1):
        if is_reflection(field, i):
            return (i + 1) * 100

    field = transpose(field)

    for i in range(len(field) - 1):
        if is_reflection(field, i):
            return (i + 1)

    return None

def answer(input: str) -> int:
    s = 0

    for field in parse_fields(input):
        print(field)
        for line in field:
            print(line)

        if (i := find_reflection(field)) is not None:
            s += i
            continue

        print('transposed')
        for line in transpose(field):
            print(line)

        if (i := find_reflection(field)) is not None:
            s += i

    return s


print(answer(Path('test.txt').read_text()))
#print(answer(Path('input.txt').read_text()))