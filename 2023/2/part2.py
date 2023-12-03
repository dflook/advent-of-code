import re
from pathlib import Path

def read_game(line: str) -> list[int]:
    match = re.match(r'Game (?P<game_id>\d+): (?P<cubes>.*)', line)

    max_colours = {}

    for handful in match.group('cubes').split(';'):
        for colour in re.finditer(r'(?P<count>\d+) (?P<colour>\w+)', handful):
            colour_name = colour.group('colour')
            max_colours[colour_name] = max(max_colours.get(colour_name, 0), int(colour.group('count')))

    return list(max_colours.values())

def power(colours: list[int]) -> int:
    total = 1

    for colour in colours:
        total *= colour

    return total

def answer(input: str) -> int:

    total = 0

    for line in input.splitlines():
        colours = read_game(line)

        total += power(colours)

    return total

print(answer(Path('test.txt').read_text()))
print(answer(Path('input.txt').read_text()))
