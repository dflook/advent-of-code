import re
from pathlib import Path

bag = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

def read_game(line: str) -> tuple[int, dict[str, int]]:
    match = re.match(r'Game (?P<game_id>\d+): (?P<cubes>.*)', line)

    game_id = int(match.group('game_id'))

    max_colours = {}

    for handful in match.group('cubes').split(';'):
        for colour in re.finditer(r'(?P<count>\d+) (?P<colour>\w+)', handful):
            colour_name = colour.group('colour')
            max_colours[colour_name] = max(max_colours.get(colour_name, 0), int(colour.group('count')))

    return game_id, max_colours

def answer(input: str) -> int:

    valid_game_id_sum = 0

    for line in input.splitlines():
        game_id, colours = read_game(line)

        if all(colours.get(colour, 0) <= bag[colour] for colour in colours):
            valid_game_id_sum += game_id

            print(f'Game {game_id} = {colours=}')

    return valid_game_id_sum

print(answer(Path('test.txt').read_text()))
print(answer(Path('input.txt').read_text()))
