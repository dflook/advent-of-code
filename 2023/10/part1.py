from dataclasses import dataclass
from pathlib import Path
from typing import Tuple, Optional


@dataclass
class Pipe:
    north: bool = False
    south: bool = False
    west: bool = False
    east: bool = False

    char: str = None

    def __str__(self):
        return self.char


pipes = {
    '|': Pipe(north=True, south=True, char='┃'),
    '-': Pipe(west=True, east=True, char='━'),
    'L': Pipe(north=True, east=True, char='┗'),
    'J': Pipe(north=True, west=True, char='┛'),
    '7': Pipe(south=True, west=True, char='┓'),
    'F': Pipe(south=True, east=True, char='┏'),
    '.': Pipe(char=' '),
    'S': Pipe(char='S')
}


class PipeSegment:
    def __init__(self, repr: str):
        self.pipe = pipes[repr]

        self.map_north = None
        self.map_south = None
        self.map_east = None
        self.map_west = None

    def flow(self, from_direction: Optional[str]=None) -> Tuple['PipeSegment', str]:
        """Returns the next pipe segment in the flow"""

        def opposite(dir: str) -> str:
            if dir == 'north':
                return 'south'
            elif dir == 'south':
                return 'north'
            elif dir == 'east':
                return 'west'
            elif dir == 'west':
                return 'east'

        for dir in ['north', 'south', 'east', 'west']:
            if getattr(self.pipe, dir) and dir != from_direction:
                return getattr(self, f'map_{dir}'), opposite(dir)

        raise Exception('No next pipe segment found')

    def __str__(self):
        return str(self.pipe)


Map = list[list[PipeSegment]]

def guess_pipe(segment: PipeSegment) -> Pipe:
    """Guesses the pipe type based on the surrounding segments"""

    if segment.map_north.pipe.south and segment.map_south.pipe.north:
        return pipes['|']
    elif segment.map_east.pipe.west and segment.map_west.pipe.east:
        return pipes['-']
    elif segment.map_north.pipe.south and segment.map_east.pipe.west:
        return pipes['L']
    elif segment.map_north.pipe.south and segment.map_west.pipe.east:
        return pipes['J']
    elif segment.map_south.pipe.north and segment.map_west.pipe.east:
        return pipes['7']
    elif segment.map_south.pipe.north and segment.map_east.pipe.west:
        return pipes['F']

    raise Exception('Could not guess segment type')

def build_map(input: str) -> Tuple[Map, PipeSegment]:
    map = [[PipeSegment(c) for c in r] for r in input.splitlines()]

    start = None

    # Plumbing
    rows_max = len(map) - 1
    cols_max = len(map[0]) - 1
    for ri, r in enumerate(map):
        for ci, p in enumerate(r):
            if p.pipe.char == 'S':
                start = p

            if ci != 0:
                p.map_west = map[ri][ci - 1]
            if ci != cols_max:
                p.map_east = map[ri][ci + 1]
            if ri != 0:
                p.map_north = map[ri - 1][ci]
            if ri != rows_max:
                p.map_south = map[ri + 1][ci]

    # Figure out the S pipe
    start.pipe = guess_pipe(start)

    return map, start


def loop_length(start: PipeSegment) -> int:

    incoming_direction = None
    length = 0
    pipe = start

    while True:
        pipe, incoming_direction = pipe.flow(incoming_direction)
        length += 1

        if pipe is start:
            break

    return length


def print_map(map: Map) -> None:
    for row in map:
        for pipe in row:
            print(pipe, end='')
        print()


def answer(input: str) -> int:
    map, start = build_map(input)
    print_map(map)

    return int(loop_length(start) / 2)


print(answer(Path('test.txt').read_text()))
print(answer(Path('input.txt').read_text()))
