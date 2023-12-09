from pathlib import Path


def find_next(sequence: list[int]) -> int:
    if all(i == 0 for i in sequence):
        return 0

    differences = [b - a for a, b in zip(sequence, sequence[1:])]
    return sequence[-1] + find_next(differences)
def answer(input: str) -> int:

    s = 0

    for line in input.splitlines():
        sequence = list(reversed([int(i) for i in line.split()]))
        next = find_next(sequence)
        s += next

    return s

print(answer(Path('test.txt').read_text()))
print(answer(Path('input.txt').read_text()))