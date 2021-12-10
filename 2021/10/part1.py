def corrupted_line(line):
    chunks_types = {
        '[': ']',
        '<': '>',
        '(': ')',
        '{': '}'
    }

    corruption_scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    chunks = []
    for char in line.strip():
        if char in chunks_types:
            chunks.append(char)
            continue

        a = chunks.pop()
        if chunks_types[a] != char:
            return corruption_scores[char]

    return False


with open('input.txt') as f:
    corruption_total = 0
    for line in f.readlines():
        if score := corrupted_line(line):
            print(line.strip())
            corruption_total += score

print(f'{corruption_total=}')
# 321237
