from pathlib import Path
from typing import Iterable, Optional

Platform = list[str]
def parse_input(input: str) -> Platform:
    return list(input.splitlines())

def calculate_load(platform: Platform) -> int:
    total_load = 0

    for load, row in enumerate(reversed(platform), start=1):
        for col in row:
            if col == 'O':
               total_load += load

    return total_load

def transpose(platform: Platform) -> Platform:
    return [''.join(column) for column in zip(*platform)]

def tilt_north(platform: Platform) -> Platform:

    print('transpose')
    switcharoo = transpose(platform)
    for row in switcharoo:
        print(row)

    tilted_platform = []
    for column_num, column in enumerate(switcharoo):
        print('column', column_num, column)
        tilted_column_parts = []
        for segment in column.split('#'):
            print('segment', segment)
            tilted_column_parts.append(''.join(sorted(segment, reverse=True)))
        tilted_column = '#'.join(tilted_column_parts)
        print('tilted_column', tilted_column)
        tilted_platform.append(tilted_column)

    print('tilted')
    for row in tilted_platform:
        print(row)

    print('transpose back')
    switcharoo = transpose(tilted_platform)
    for row in switcharoo:
        print(row)

    return switcharoo


def answer(input: str) -> int:
    platform = parse_input(input)

    for row in platform:
        print(row)

    platform = tilt_north(platform)

    for row in platform:
        print(row)

    return calculate_load(platform)

#print(answer(Path('test.txt').read_text()))
print(answer(Path('input.txt').read_text()))