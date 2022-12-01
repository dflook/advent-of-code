import itertools
from collections import Counter
from itertools import pairwise
from typing import Dict, Tuple, Iterable

Character = str

def read(path: str) -> Tuple[str, Dict[str, str]]:
    template = None
    insertion_rules = {}

    with open(path) as f:
        for line in (x.strip() for x in f.readlines()):
            if not line:
                continue

            if template is None:
                template = line
                continue

            pair, insertion = line.split(' -> ', maxsplit=1)

            insertion_rules[pair] = insertion

    return template, insertion_rules

def expand(a: Character, b: Character, rules: Dict[str, str], depth) -> str:
    e = a + rules[a+b] + b

    c = Counter(a, rules[a+b], b)

template, rules = read('test.txt')
print(f'{template=}')
print(f'{rules}')

counts = Counter()

for a, b in itertools.pairwise(template):
    counts += expand((a, b), rules)

most_common_count = counts.most_common(1)[0][1]
least_common_count = counts.most_common()[-1][1]

print(counts)
print(most_common_count - least_common_count)
