from dataclasses import dataclass
from typing import List, Iterable, Tuple


@dataclass
class BingoNumber:
    value: int
    marked: bool = False


BingoRow = List[BingoNumber]
BingoBoard = List[BingoRow]


def read(path):
    with open(path) as f:
        puzzle_input = f.read().splitlines()

    draw_order = [int(x) for x in puzzle_input[0].split(',')]

    boards = []
    board = []
    for line in [l.strip() for l in puzzle_input[1:]]:
        if line == '':
            if board:
                boards.append(board)
                board = []
            continue

        board.append([BingoNumber(int(x.strip())) for x in line.split(' ') if x])

    if board:
        boards.append(board)

    return draw_order, boards


def mark_boards(draw: int, boards: List[BingoBoard]):
    for board in boards:
        for row_num, row in enumerate(board):
            for column_num, bingo_number in enumerate(row):
                if bingo_number.value == draw:
                    bingo_number.marked = True


def is_marked(row: Iterable[BingoNumber]) -> bool:
    return all(number.marked for number in row)


def is_winner(board: BingoBoard) -> bool:
    for row in board:
        if is_marked(row):
            return True

    for col in zip(*board):
        if is_marked(col):
            return True

    return False


def do_the_bingo(draw_order, boards) -> Tuple[int, int, int]:
    winners = []
    winning_draw = {}
    winning_score = {}

    for draw in draw_order:
        mark_boards(draw, boards)

        for i, board in enumerate(boards):
            if is_winner(board) and i not in winners:
                winners.append(i)
                winning_draw[i] = draw
                winning_score[i] = score_board(board)

    last_winner = winners.pop()
    return winning_draw[last_winner], last_winner, winning_score[last_winner]


def score_board(board: BingoBoard):
    score = 0

    for row in board:
        for number in row:
            if not number.marked:
                score += number.value

    return score


draw_order, boards = read('input.txt')

winning_draw, winning_board, winning_score = do_the_bingo(draw_order, boards)
print(f'Winning boards is {winning_board}')
print(f'Winning score is {winning_score}')
print(f'Answer is {winning_draw * winning_score}')
# 21184
