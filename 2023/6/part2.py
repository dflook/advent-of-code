from typing import Tuple

#Time:      71530
#Distance:  940200
test = [
    (71530, 940200),
]

#Time:        46828479
#Distance:   347152214061471
input = [
    (46828479, 347152214061471),
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

11111111