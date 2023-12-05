import re
from dataclasses import dataclass
from pathlib import Path

Seed = int

@dataclass
class Range:
    destination_range_start: int
    source_range_start: int
    range_length: int

    def __repr__(self):
        return f'Range({self.destination_range_start}, {self.source_range_start}, {self.range_length})'

class Map:
    def __init__(self, source: str, destination: str, ranges: list[Range]):
        self.source = source
        self.destination = destination
        self.ranges = ranges

    def __repr__(self):
        return f'Map({self.source}, {self.destination}, {self.ranges})'

    def __getitem__(self, source: int) -> int:
        for range in self.ranges:
            if source >= range.source_range_start and source < range.source_range_start + range.range_length:
                return range.destination_range_start + (source - range.source_range_start)

        return source

def parse_input(input: str) -> tuple[list[Seed], list[Map]]:

    seeds, maps = [], []
    source, destination = None, None

    ranges = []
    for line in input.splitlines():
        if (match := re.match(r'^seeds:\s+(?P<seeds>.*)', line)):
            seeds = [int(seed) for seed in match.group('seeds').split()]
        elif (match := re.match(r'^(?P<source>.*)-to-(?P<destination>.*)\s+map:', line)):
            if source and destination:
                maps.append(Map(source, destination, ranges))

            source = match.group('source')
            destination = match.group('destination')
            ranges = []

        elif line:
            ranges.append(Range(*[int(x) for x in line.split()]))

    if source and destination:
        maps.append(Map(source, destination, ranges))

    return seeds, maps

def find(destination_type: str, source_type: str, source: int) -> int:

    for map in maps:
        assert map.source == source_type
        destination = map[source]
        print(f'{source_type} {source} -> {map.destination} {destination}')
        source = destination
        source_type = map.destination

        if source_type == destination_type:
            return source

    raise ValueError(f'Could not find {destination_type} for {source_type} {source}')

seeds, maps = parse_input(Path('input.txt').read_text())

locations = []

for seed in seeds:
    locations.append(find('location', 'seed', seed))

print(min(locations))