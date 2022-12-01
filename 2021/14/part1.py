from collections import Counter

def read(path):
    template = None
    insertion_rules = {}

    with open(path) as f:
        for line in (x.strip() for x in f.readlines()):
            if not line:
                continue

            if template is None:
                template = line
                continue

            pair, insertion = line.split(' -> ', maxsplit=1)

            insertion_rules[pair] = insertion

    return template, insertion_rules

def step(template, rules):
    polymer = ''
    for a, b in zip(template, template[1:]):

        if not polymer:
            polymer += a

        polymer += rules[a+b]
        polymer += b

    return polymer

template, rules = read('input.txt')
print(f'{template=}')
print(f'{rules}')

for i in range(10):
    template = step(template, rules)
    print(f'After steo {i}: {template}')

counts = Counter(template)

most_common_count = counts.most_common(1)[0][1]
least_common_count = counts.most_common()[-1][1]

print(counts)
print(most_common_count - least_common_count)
# 3587
