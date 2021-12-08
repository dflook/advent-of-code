def read():
    with open('input.txt') as f:
        for line in f.readlines():
            signal_patterns, output_value = line.split(' |', maxsplit=1)
            yield output_value.split()


count = 0
for output_value in read():
    for c in output_value:
        if len(c) in [2, 4, 3, 7]:
            count += 1

print(count)
# 525
