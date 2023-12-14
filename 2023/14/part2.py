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


def tilt(platform: Platform, reverse: bool = False) -> Iterable[str]:
    for line in platform:
        yield '#'.join([''.join(sorted(segment, reverse=reverse)) for segment in line.split('#')])


def tilt_east(platform: Platform) -> Platform:
    return list(tilt(platform))


def tilt_south(platform: Platform) -> Platform:
    return transpose(list(tilt(transpose(platform))))


def tilt_west(platform: Platform) -> Platform:
    return list(tilt(platform, reverse=True))


def tilt_north(platform: Platform) -> Platform:
    return transpose(list(tilt(transpose(platform), reverse=True)))


def spin_cycle(platform: Platform) -> Platform:
    return tilt_east(tilt_south(tilt_west(tilt_north(platform))))


def spin(platform: Platform, remaining_cycles: int) -> Platform:
    previous_platforms: Optional[list[Platform]] = []

    while remaining_cycles > 0:
        platform = spin_cycle(platform)
        remaining_cycles -= 1

        if previous_platforms is not None and platform in previous_platforms:
            repeat_length = len(previous_platforms) - previous_platforms.index(platform)
            print(f'Found a repeating pattern with {remaining_cycles} left, repeat length {repeat_length}')
            remaining_cycles %= repeat_length
            print(f'Fast forwarding to {remaining_cycles} left')
            previous_platforms = None

        if previous_platforms is not None:
            previous_platforms.append(platform)

    return platform


def answer(input: str) -> int:
    platform = parse_input(input)

    for row in platform:
        print(row)

    platform = spin(platform, 1000000000)

    for row in platform:
        print(row)

    return calculate_load(platform)


# print(answer(Path('test.txt').read_text()))
print(answer(Path('input.txt').read_text()))
