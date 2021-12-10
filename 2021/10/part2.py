def autocompleted(line):
    chunks_types = {
        '[': ']',
        '<': '>',
        '(': ')',
        '{': '}'
    }

    autocomplete_scores = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    chunks = []
    for char in line:
        if char in chunks_types:
            chunks.append(char)
            continue

        a = chunks.pop()
        if chunks_types[a] != char:
            # corrupted
            return False

    autocomplete = [chunks_types[a] for a in reversed(chunks)]
    print(f'{autocomplete=}')

    score = 0
    for c in autocomplete:
        score *= 5
        score += autocomplete_scores[c]
    return score


with open('input.txt') as f:
    scores = []

    for line in (l.strip() for l in f.readlines()):
        if score := autocompleted(line):
            scores.append(score)

scores = sorted(scores)
print(f'{scores=}')
winner = scores[int(len(scores) / 2)]
print(f'{winner=}')
# 2360030859
