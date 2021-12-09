from typing import List


def read():
    map: List[List[int]] = []

    with open('input.txt') as f:
        for line in f.readlines():
            map.append([int(x) for x in line.strip()])

    return map


map = read()
risk = 0

for row in range(len(map)):
    for col in range(len(map[row])):

        this = map[row][col]

        if col > 0 and this >= map[row][col - 1]:
            continue

        if col < len(map[row]) - 1 and this >= map[row][col + 1]:
            continue

        if row > 0 and this >= map[row - 1][col]:
            continue

        if row < len(map) - 1 and this >= map[row + 1][col]:
            continue

        print(f'low point at {row},{col}: {this}')
        risk += 1 + this

print(f'{risk=}')
# 516
