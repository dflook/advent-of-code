from dataclasses import dataclass
from typing import List, Optional, Iterable, Tuple


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
        for row in board:
            for bingo_number in row:
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


def check_winner(boards) -> Optional[int]:
    for i, board in enumerate(boards):
        if is_winner(board):
            return i


def do_the_bingo(draw_order, boards) -> Tuple[int, int]:
    for draw in draw_order:
        mark_boards(draw, boards)
        if winner := check_winner(boards):
            return draw, winner


def score_board(board: BingoBoard):
    score = 0

    for row in board:
        for number in row:
            if not number.marked:
                score += number.value

    return score


draw_order, boards = read('input.txt')

winning_draw, winning_board = do_the_bingo(draw_order, boards)
print(f'Winning boards is {winning_board}')
winning_score = score_board(boards[winning_board])
print(f'Winning score is {winning_score}')

print(f'Answer is {winning_draw * winning_score}')
# 38594
