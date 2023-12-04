import re
from dataclasses import dataclass, field
from functools import reduce
from pathlib import Path
from typing import Iterable, Tuple, Union

@dataclass
class Card:
    id: int

    winning_numbers: field(default_factory=set)
    numbers: field(default_factory=set)

    def score(self) -> int:

        score = 0

        for _ in self.winning_numbers.intersection(self.numbers):
            if score == 0:
                score = 1
            else:
                score *= 2

        return score

def read_cards(input: str) -> Iterable[Card]:
    for line in input.splitlines():

        if (match := re.match(r'Card\s+(?P<card>\d+):\s+(?P<winners>.*)\s+\|\s+(?P<numbers>.*)', line)) is not None:

            winners = set(int(i) for i in re.split(r'\s+', match.group('winners')))
            numbers = set(int(i) for i in re.split(r'\s+', match.group('numbers')))

            card = Card(int(match.group('card')), winners, numbers)
            print(card)
            print(card.score())
            yield card

def answer(input: str) -> str:

    total = sum(card.score() for card in read_cards(input))
    return total


#print(answer(Path('test.txt').read_text()))
print(answer(Path('input.txt').read_text()))
