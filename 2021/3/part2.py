from typing import Iterable


def filter_for(report: Iterable[int], bit_pos: int, chooser):
    mask = 1 << bit_pos

    set = []
    not_set = []

    for value in report:
        if value & mask == mask:
            set.append(value)
        else:
            not_set.append(value)

    if len(set) + len(not_set) == 1:
        yield from set + not_set
        return

    report_set = chooser(set, not_set)

    print(f'Filter for {bit_pos}: {report_set}')
    yield from report_set


def rating(report, bit_len, set_chooser) -> int:
    r = report
    for i in range(bit_len - 1, -1, -1):
        r = filter_for(r, i, set_chooser)
    return next(r)


bit_len = 0
report = []
with open('input.txt') as f:
    for line in f.readlines():
        report.append(int(line, base=2))
        bit_len = max(bit_len, len(line.strip()))

oxygen_rating = rating(
    report,
    bit_len,
    lambda set, not_set: not_set if len(not_set) > len(set) else set
)
print(f'oxygen_rating: {oxygen_rating}')

scrubber_rating = rating(
    report,
    bit_len,
    lambda set, not_set: set if len(not_set) > len(set) else not_set
)
print(f'scrubber_rating: {scrubber_rating}')

print(f'life support rating: {scrubber_rating * oxygen_rating}')
# 3277956
