from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass
class Tree:
    height: int
    visible: bool = False


Grid = list[list[Tree]]


def read_grid(inp: str) -> Grid:
    grid: Grid = [[]]

    lines = inp.splitlines()

    for x, line in enumerate(lines):
        if len(grid) <= x:
            grid.append([])

        for y, tree_height in enumerate(line):
            grid[x].append(Tree(int(tree_height)))

    return grid


def mark_visible(grid: Grid) -> Grid:
    max_column_heights: list[int] = [0 for _ in range(len(grid[0]))]

    for row in grid:
        max_row_height = 0

        for column, tree in enumerate(row):

            if tree.height > max_row_height:
                tree.visible = True
                max_row_height = tree.height

            if tree.height > max_column_heights[column]:
                tree.visible = True
                max_column_heights[column] = tree.height

    max_column_heights: list[int] = [0 for _ in range(len(grid[0]))]

    for row in reversed(grid):
        max_row_height = 0

        for column, tree in enumerate(reversed(row)):

            if tree.height > max_row_height:
                tree.visible = True
                max_row_height = tree.height

            if tree.height > max_column_heights[column]:
                tree.visible = True
                max_column_heights[column] = tree.height

    return grid


def show_grid(grid: Grid) -> str:
    s = ''

    for row in grid:
        for tree in row:
            if tree.visible:
                s += str(tree.height)
            else:
                s += ' '
        s += '\n'

    return s


def count_visible(grid: Grid) -> int:
    s = 0

    for row in grid:
        s += sum(1 for tree in row if tree.visible)

    return s


def score_view(tree: Tree, view: Iterable[Tree]) -> int:
    # print(f'scoring {view}')

    score = 0

    for t in view:
        score += 1

        if t.height >= tree.height:
            return score

    return score


def scenic_score(grid: Grid, tree_row: int, tree_column: int) -> int:
    tree = grid[tree_row][tree_column]

    left = score_view(tree, reversed(grid[tree_row][:tree_column]))
    right = score_view(tree, grid[tree_row][tree_column + 1:])
    up = score_view(tree, reversed([r[tree_column] for r in grid[:tree_row]]))
    down = score_view(tree, [r[tree_column] for r in grid[tree_row + 1:]])

    return left * right * up * down


def highest_score(grid: Grid) -> int:
    highest = 0
    for row_num, row in enumerate(grid):
        for column_num, tree in enumerate(row):
            score = scenic_score(grid, row_num, column_num)
            highest = max(score, highest)

    return highest


grid = read_grid(Path('input.txt').read_text())
grid = mark_visible(grid)
print(show_grid(grid))

print(f'{count_visible(grid)=}')
print(f'{highest_score(grid)=}')
