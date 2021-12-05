import re


def read(path):
    with open(path) as f:
        for line in f.readlines():
            if match := re.match(r'(?P<start_x>\d+),(?P<start_y>\d+) -> (?P<end_x>\d+),(?P<end_y>\d+)', line):

                line = {k: int(v) for k, v in match.groupdict().items()}

                if not (line['start_x'] == line['end_x'] or line['start_y'] == line['end_y']):
                    continue

                if line['end_x'] < line['start_x']:
                    line['start_x'], line['end_x'] = line['end_x'], line['start_x']

                if line['end_y'] < line['start_y']:
                    line['start_y'], line['end_y'] = line['end_y'], line['start_y']

                yield line


lines = list(read('input.txt'))

diagram = {}

for line in lines:
    print(f'line {line}')
    for x in range(line['start_x'], line['end_x'] + 1):
        print(f'{x=}')

        for y in range(line['start_y'], line['end_y'] + 1):
            print(f'{y=}')
            diagram[(x, y)] = diagram.get((x, y), 0) + 1

overlaps = 0
for (x, y), count in diagram.items():
    print(f'{x=}, {y=}, {count=}')
    if count > 1:
        overlaps += 1

print(f'{overlaps=}')
# 6311
