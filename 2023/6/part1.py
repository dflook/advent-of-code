from typing import Tuple

#Time:      7  15   30
#Distance:  9  40  200
test = [
    (7, 9),
    (15, 40),
    (30, 200)
]

#Time:        46     82     84     79
#Distance:   347   1522   1406   1471
input = [
    (46, 347),
    (82, 1522),
    (84, 1406),
    (79, 1471)
]

def distance(button_time: int, race_time: int) -> int:

    running_time = race_time - button_time
    return running_time * button_time

def find_winners(race_time: int, record: int ) -> int:

    win_count = 0

    print(f'Racing for {race_time}')
    for button_time in range(race_time):
        d = distance(button_time, race_time)
        print(f'Pressing for {button_time} seconds = {d}')
        if d > record:
            win_count += 1

    print(f'{win_count} ways to win')
    return win_count

def answer(races: Tuple[int, int]) -> int:
    a = 1
    for race_time, record in races:
        a *= find_winners(race_time, record)
    return a

print(answer(input))