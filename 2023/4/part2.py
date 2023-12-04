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

    copies = 1

    def score(self) -> int:
        return len(self.winning_numbers.intersection(self.numbers))

def read_cards(input: str) -> Iterable[Card]:
    for line in input.splitlines():

        if (match := re.match(r'Card\s+(?P<card>\d+):\s+(?P<winners>.*)\s+\|\s+(?P<numbers>.*)', line)) is not None:

            winners = set(int(i) for i in re.split(r'\s+', match.group('winners')))
            numbers = set(int(i) for i in re.split(r'\s+', match.group('numbers')))

            card = Card(int(match.group('card')), winners, numbers)
            print(card)
            yield card

def answer(input: str) -> str:

    cards = {card.id: card for card in read_cards(input)}

    total_cards = 0

    for card in cards.values():
        total_cards += card.copies

        for i in range(card.id + 1, card.id + card.score() + 1):
            cards[i].copies += card.copies

    return total_cards

#print(answer(Path('test.txt').read_text()))
print(answer(Path('input.txt').read_text()))
