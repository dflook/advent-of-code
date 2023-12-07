import re
from dataclasses import dataclass
from pathlib import Path
import progressbar

@dataclass
class InputRange:
    """
    A range of inputs, such as seeds or locations.

    The range is inclusive, so a range of 0-10 includes 0 and 10.
    """

    category: str
    start: int
    end: int

    @property
    def size(self) -> int:
        return self.end - self.start + 1

    def __str__(self):
        return f'{self.category} range {self.start}-{self.end} ({self.size})'

    def __bool__(self):
        return self.size > 0

@dataclass
class MapRange:
    """
    A range of mapped values in a map.

    The range is inclusive, so a range of 0-10 includes 0 and 10.
    """

    start: int
    end: int
    destination_start: int = 0

    def __bool__(self):
        return self.size > 0

    @property
    def size(self):
        return self.end - self.start + 1

    @property
    def destination_end(self) -> int:
        return self.destination_start + self.size - 1

    def __str__(self):
        return f'{self.start}-{self.end} ({self.size})-> {self.destination_start}-{self.destination_end}'

    def __repr__(self):
        return f'Range({self.destination_start}, {self.start}, {self.end})'

class Map:
    def __init__(self, source: str, destination: str, ranges: list[MapRange]):
        self.source = source
        self.destination = destination
        self.ranges = ranges

    def __str__(self):
        s = f'{self.source}-to-{self.destination} map:\n'
        for range in self.ranges:
            s += f'  {range}\n'
        return s

    def __repr__(self):
        return f'Map({self.source}, {self.destination}, {self.ranges})'

    def __getitem__(self, source: int) -> int:
        for range in self.ranges:
            if source >= range.start and source < range.end:
                return range.destination_start + (source - range.start)

        return source

def parse_input(input: str) -> tuple[list[InputRange], list[Map]]:

    maps = []
    source, destination = None, None

    ranges = []
    seed_ranges = []

    for line in input.splitlines():
        if (match := re.match(r'^seeds:\s+(?P<seeds>.*)', line)):

            seed_input = [int(seed) for seed in match.group('seeds').split()]
            for seed_begin, seed_range in zip(seed_input[::2], seed_input[1::2]):
                seed_ranges.append(InputRange('seed', seed_begin, seed_begin + seed_range - 1))

        elif (match := re.match(r'^(?P<source>.*)-to-(?P<destination>.*)\s+map:', line)):
            if source and destination:
                maps.append(Map(source, destination, sorted(ranges, key=lambda x: x.start)))

            source = match.group('source')
            destination = match.group('destination')
            ranges = []

        elif line:
            destination_start, source_start, range = [int(x) for x in line.split()]

            ranges.append(MapRange(
                start=source_start,
                end=source_start + range - 1,
                destination_start=destination_start,
            ))

    if source and destination:
        maps.append(Map(source, destination, sorted(ranges, key=lambda x: x.start)))

    return seed_ranges, maps

def find(destination_type: str, source_type: str, source: int, maps: list[Map]) -> int:

    for map in maps:
        assert map.source == source_type
        destination = map[source]
        #print(f'{source_type} {source} -> {map.destination} {destination}')
        source = destination
        source_type = map.destination

        if source_type == destination_type:
            return source

    raise ValueError(f'Could not find {destination_type} for {source_type} {source}')

def find_lowest_in_range(seed_range: InputRange, maps: list[Map]) -> int:
    lowest_location = None

    bar = progressbar.ProgressBar(max_value=seed_range.size)
    for seed in bar(range(seed_range.start, seed_range.end)):

        l = find('location', 'seed', seed, maps)

        if lowest_location is None:
            lowest_location = l
        else:
            lowest_location = min(lowest_location, l)

    return lowest_location

def main():
    seed_ranges, maps = parse_input(Path('input.txt').read_text())

    print(seed_ranges)
    print(maps)

    lowest = None
    for seed_range in seed_ranges:
        l = find_lowest_in_range(seed_range, maps)
        if lowest is None:
            lowest = l
        else:
            lowest = min(lowest, l)

    print(lowest)

if __name__ == '__main__':
    main()