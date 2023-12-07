from collections import Counter
from functools import total_ordering
from pathlib import Path

card_strength = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

@total_ordering
class Hand:

    Types = [
        'High card',
        'One pair',
        'Two pair',
        'Three of a kind',
        'Full house',
        'Four of a kind',
        'Five of a kind'
    ]

    def __init__(self, hand: str, bid: int):
        self.hand = [c for c in hand]
        self.bid = bid
        self.type = self.find_type()

    def find_type(self) -> str:
        unique_cards = Counter(self.hand)
        most_common_count = unique_cards.most_common(1)[0][1]

        if len(unique_cards) == 1:
            # Five of a kind
            return 'Five of a kind'

        elif len(unique_cards) == 2:
            if most_common_count == 4:
                return 'Four of a kind'
            else:
                return 'Full house'

        elif len(unique_cards) == 3:

            if most_common_count == 3:
                return 'Three of a kind'
            elif most_common_count == 2:
                return 'Two pair'

        elif len(unique_cards) == 4:
            return 'One pair'

        else:
            return 'High card'

    def __eq__(self, other):
        return self.hand == other.hand

    def __lt__(self, other):
        if not isinstance(other, Hand):
            return NotImplemented

        if self.type != other.type:
            return self.Types.index(self.type) < self.Types.index(other.type)

        for card, other_card in zip(self.hand, other.hand):
            if card != other_card:
                return card_strength.index(card) < card_strength.index(other_card)

    def __repr__(self) -> str:
        return f'Hand({self.hand}, {self.bid})'

    def __str__(self) -> str:
        return f'{self.hand} {self.bid}'

def answer(input: str) -> int:

    hands = []

    for line in input.splitlines():
        hand, bid = line.split()
        hands.append(Hand(hand, int(bid)))

    hands.sort()

    winnings = 0
    for rank, hand in enumerate(hands, start=1):
        print(f'{hand} has rank {rank}, so has won {hand.bid * rank}')
        winnings += hand.bid * rank

    return winnings

print(answer(Path('input.txt').read_text()))
