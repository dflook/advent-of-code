from __future__ import annotations
from dataclasses import dataclass, field
from pprint import pprint
from typing import Set, List


@dataclass
class Cave:
    name: str
    paths: Set[Cave] = field(default_factory=set)

def read(path):

    caves = {}

    with open(path) as f:
        for line in f.readlines():
            a, b = line.strip().split('-', maxsplit=1)

            if a not in caves:
                caves[a] = Cave(a)
            if b not in caves:
                caves[b] = Cave(b)

            caves[a].paths.add(b)
            caves[b].paths.add(a)

    return caves

def explore(cave) -> List[str]:
    for path in cave.paths:
        return [cave] + path

caves = read('minitest.txt')
pprint(caves)
