from pathlib import Path

WIN = 'Z'
DRAW = 'Y'
LOSE = 'X'

ROCK = 'A'
PAPER = 'B'
SCISSORS = 'C'


def round_score(opponent: str, me: str) -> int:
    if me == opponent:
        return 3

    if ((me == ROCK and opponent == SCISSORS) or
            (me == PAPER and opponent == ROCK) or
            (me == SCISSORS and opponent == PAPER)):
        return 6

    return 0


def move_score(move) -> int:
    move_score = {
        ROCK: 1,
        PAPER: 2,
        SCISSORS: 3
    }

    return move_score[move]


def choose_move(opponent: str, desired_result: str) -> str:
    if desired_result == DRAW:
        return opponent

    winning_moves = {
        ROCK: SCISSORS,
        PAPER: ROCK,
        SCISSORS: PAPER
    }

    if desired_result == LOSE:
        return winning_moves[opponent]

    # win
    for m, o in winning_moves.items():
        if o == opponent:
            return m


def read(p):
    for line in Path(p).read_text().splitlines():
        yield line.split(' ')


sum = 0
for opponent, desired_result in read('input.txt'):
    print(f'{opponent=}, {desired_result=}')
    me = choose_move(opponent, desired_result)
    print(f'{me=}')
    sum += round_score(opponent, me) + move_score(me)
print(sum)
