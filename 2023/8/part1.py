import itertools
import re
from pathlib import Path
from typing import Tuple, Iterable


def parse(input: str) -> Tuple[Iterable[str], dict[str, Tuple[str, str]]]:
    instructions = None
    nodes = {}

    for line in input.splitlines():
        if instructions is None:
            instructions = itertools.cycle([c for c in line])
            continue

        if (match := re.match(r'^(?P<node>.*?) = \((?P<left>.*?), (?P<right>.*?)\)$', line)):
            nodes[match.group('node')] = (match.group('left'), match.group('right'))

    return instructions, nodes

def walk(instructions: Iterable[str], nodes: dict[str, Tuple[str, str]], current_node='AAA') -> int:

    steps = 0
    for instruction in instructions:
        if current_node == 'ZZZ':
            return steps

        steps += 1
        if instruction == 'L':
            current_node = nodes[current_node][0]
        elif instruction == 'R':
            current_node = nodes[current_node][1]

instructions, nodes = parse(Path('test1.txt').read_text())
print(walk(instructions, nodes))

instructions, nodes = parse(Path('test2.txt').read_text())
print(walk(instructions, nodes))

instructions, nodes = parse(Path('input.txt').read_text())
print(walk(instructions, nodes))
