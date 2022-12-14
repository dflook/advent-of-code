from __future__ import annotations

from pathlib import Path
from typing import Iterable


class Packet:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        try:
            compare(self.value, other.value)
        except Ordered:
            return True
        except Unordered:
            return False

        return False

    def __repr__(self):
        return repr(self.value)


def read_packets(inp: str) -> Iterable[Packet]:
    for line in inp.splitlines():
        if not line:
            continue
        yield Packet(eval(line))
    yield Packet([[2]])
    yield Packet([[6]])


packets = list(read_packets(Path('input.txt').read_text()))


class Ordered(Exception): pass


class Unordered(Exception): pass


def compare(left, right, indent=0):
    prefix = ' ' * indent
    print(f'{prefix}- Compare {left} vs {right}')
    prefix += '  '

    if isinstance(left, list) and isinstance(right, list):
        for l, r in zip(left, right):
            compare(l, r, indent + 2)
        if len(left) < len(right):
            print(f'{prefix}- Left side ran out of items, so inputs are in the right order')
            raise Ordered
        elif len(left) > len(right):
            print(f'{prefix}- Right side ran out of items, so inputs are not in the right order')
            raise Unordered

        # Equal lists
        return

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            print(f'{prefix}- Left side is smaller, so inputs are in the right order')
            raise Ordered
        elif left > right:
            print(f'{prefix}- Right side is smaller, so inputs are not in the right order')
            raise Unordered
        else:
            # Equal compare, continue
            return

    # mixed types
    left = left if isinstance(left, list) else [left]
    right = right if isinstance(right, list) else [right]
    print(f'{prefix}- Mixed types; convert to {left}, {right} and retry comparison')
    return compare(left, right, indent + 2)


ordered_packets = sorted(packets)
start = 0
end = 0
for i, packet in enumerate(ordered_packets):
    if packet.value == [[2]]:
        start = i + 1
    if packet.value == [[6]]:
        end = i + 1
print(f'{start=}, {end=}, {start*end=}')
