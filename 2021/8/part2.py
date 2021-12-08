from typing import List, Dict


def read():
    with open('input.txt') as f:
        for line in f.readlines():
            signal_patterns, output_value = line.split(' |', maxsplit=1)

            signal_patterns = signal_patterns.split(' ')
            output_value = output_value.split()

            yield [set(x) for x in signal_patterns], [''.join(sorted(x)) for x in output_value]


def decode(signal_pattern: List[str]) -> Dict[str, str]:
    decoded = {
        8: set('abcdefg')
    }

    for pattern in signal_pattern:
        if len(pattern) == 2:
            decoded[1] = pattern
        elif len(pattern) == 3:
            decoded[7] = pattern
        elif len(pattern) == 4:
            decoded[4] = pattern

    for pattern in signal_pattern:
        if len(pattern) == 6 and pattern > decoded[4]:
            decoded[9] = pattern
            break

    for pattern in signal_pattern:
        if len(pattern) == 6 and pattern != decoded[9] and pattern > decoded[1]:
            decoded[0] = pattern
            break

    for pattern in signal_pattern:
        if len(pattern) == 6 and pattern != decoded[9] and pattern != decoded[0]:
            decoded[6] = pattern
            break

    for pattern in signal_pattern:
        if len(pattern) == 5 and pattern > decoded[1]:
            decoded[3] = pattern
            break

    decoded[5] = decoded[9] & decoded[6]

    for pattern in signal_pattern:
        if len(pattern) == 5 and pattern != decoded[3] and pattern != decoded[5]:
            decoded[2] = pattern
            break

    return {''.join(sorted(pattern)): str(value) for value, pattern in decoded.items()}


def digits(output_value, encoding) -> int:
    s = ''

    for c in output_value:
        s += encoding[c]

    return s


total = 0
for signal_pattern, output_value in read():
    print(f'{signal_pattern=}, {output_value=}')
    decoded = decode(signal_pattern)
    print(f'{decoded=}')
    value = digits(output_value, decoded)
    print(f'{value}')
    total += int(value)

print(f'{total=}')
# 1083859
