import math
from typing import Callable

class Monkey:
    def __init__(self, starting_items: list[int], operation: Callable[[int], int], throw_decider: Callable[[int], int]):
        self.items = starting_items
        self.op = operation
        self.decide_throw = throw_decider
        self.inspect_count = 0

    def operation(self, *args):
        self.inspect_count += 1
        new_worry = self.op(*args)
        return new_worry

    def __repr__(self) -> str:
        return f'Monkey(items={self.items}, inspect_count={self.inspect_count})'


monkies = [
    Monkey([79, 98], lambda x: x * 19, lambda x: 2 if x % 23 == 0 else 3),
    Monkey([54, 65, 75, 74], lambda x: x + 6, lambda x: 2 if x % 19 == 0 else 0),
    Monkey([79, 60, 97], lambda x: x * x, lambda x: 1 if x % 13 == 0 else 3),
    Monkey([74], lambda x: x + 3, lambda x: 0 if x % 17 == 0 else 1),
]
'''
monkies = [
    Monkey(
        [89, 74],
        lambda x: x * 5,
        lambda x: 4 if x % 17 == 0 else 7
    ),
    Monkey(
        [75, 69, 87, 57, 84, 90, 66, 50],
        lambda x: x + 3,
        lambda x: 3 if x % 7 == 0 else 2
    ),
    Monkey(
        [55],
        lambda x: x + 7,
        lambda x: 0 if x % 13 == 0 else 7
    ),
    Monkey(
        [69, 82, 69, 56, 68],
        lambda x: x + 5,
        lambda x: 0 if x % 2 == 0 else 2
    ),
    Monkey(
        [72, 97, 50],
        lambda x: x + 2,
        lambda x: 6 if x % 19 == 0 else 5
    ),
    Monkey(
        [90, 84, 56, 92, 91, 91],
        lambda x: x * 19,
        lambda x: 6 if x % 3 == 0 else 1
    ),
    Monkey(
        [63, 93, 55, 53],
        lambda x: x * x,
        lambda x: 3 if x % 5 == 0 else 1
    ),
    Monkey(
        [50, 61, 52, 58, 86, 68, 97],
        lambda x: x + 4,
        lambda x: 5 if x % 11 == 0 else 4
    ),
]
'''

def round():
    for monkey in monkies:
        # Monkey turn

        for item in monkey.items:
            worry = monkey.operation(item) // 3
            destination_monkey = monkey.decide_throw(worry)
            monkies[destination_monkey].items.append(worry)

        monkey.items = []

for r in range(20):
    round()

for monkey_num, monkey in enumerate(monkies):
    print(f'{monkey_num}: {monkey}')

most_active_monkies = sorted(monkies, key=lambda m: m.inspect_count)[-2:]
print(f'{most_active_monkies=}')

print('Monkey business: ', most_active_monkies[0].inspect_count * most_active_monkies[1].inspect_count)