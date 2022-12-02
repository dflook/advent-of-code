from pathlib import Path

WIN = 6
DRAW = 3
LOSE = 0


def round_score(opponent: str, me: str) -> int:
    if me == opponent:
        return DRAW

    if ((me == 'R' and opponent == 'S') or
            (me == 'P' and opponent == 'R') or
            (me == 'S' and opponent == 'P')):
        return WIN

    return LOSE


def move_score(move) -> int:
    move_score = {
        'R': 1,
        'P': 2,
        'S': 3
    }

    return move_score.get(move)


def read(p):
    moves = {
        'A': 'R',
        'B': 'P',
        'C': 'S',
        'X': 'R',
        'Y': 'P',
        'Z': 'S'
    }

    for line in Path(p).read_text().splitlines():
        opponent, me = line.split(' ')
        yield moves.get(opponent), moves.get(me)


sum = 0
for o, m in read('input.txt'):
    print(o, m)
    sum += round_score(o, m) + move_score(m)
    print(round_score(o, m) + move_score(m))
    print(sum)
