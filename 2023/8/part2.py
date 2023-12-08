import itertools
import math
import re
from pathlib import Path
from typing import Tuple, Iterable


def parse(input: str) -> Tuple[Iterable[str], dict[str, Tuple[str, str]]]:
    instructions = None
    nodes = {}

    for line in input.splitlines():
        if instructions is None:
            instructions = [c for c in line]
            continue

        if (match := re.match(r'^(?P<node>.*?) = \((?P<left>.*?), (?P<right>.*?)\)$', line)):
            nodes[match.group('node')] = (match.group('left'), match.group('right'))

    return instructions, nodes

def walk(instructions: Iterable[str], nodes: dict[str, Tuple[str, str]], current_node: str) -> int:

    steps = 0
    repeat_steps = 0
    end_node = None

    for instruction in itertools.cycle(instructions):
        if current_node.endswith('Z'):
            if end_node is None:
                end_node = current_node
            else:
                assert end_node == current_node
                assert steps == repeat_steps
                # All paths are unique and repeat from the starting point!
                return steps

        if end_node:
            repeat_steps += 1
        else:
            steps += 1

        if instruction == 'L':
            current_node = nodes[current_node][0]
        elif instruction == 'R':
            current_node = nodes[current_node][1]

def ghost_walk(instructions: Iterable[str], nodes: dict[str, Tuple[str, str]]) -> list[int]:

    path_steps = []

    initial_nodes = [n for n in nodes if n.endswith('A')]
    for initial_node in initial_nodes:
        steps = walk(instructions, nodes, initial_node)
        print(steps)
        path_steps.append(steps)

    return path_steps

def how_many_steps(steps: list[int]) -> int:
    # There is probably a mathy way to do this
    return math.lcm(*steps)


instructions, nodes = parse(Path('part2.txt').read_text())
print(how_many_steps(ghost_walk(instructions, nodes)))
instructions, nodes = parse(Path('input.txt').read_text())
print(how_many_steps(ghost_walk(instructions, nodes)))
