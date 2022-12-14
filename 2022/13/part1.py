from pathlib import Path


def read_packets(inp: str) -> tuple[list, list]:
    left = None
    for line in inp.splitlines():
        if not line:
            continue

        if left:
            yield eval(left), eval(line)
            left = None
        else:
            left = line


packets = list(read_packets(Path('test.txt').read_text()))


class Ordered(Exception): pass


class Unordered(Exception): pass


def compare(left, right, indent=0):
    prefix = ' ' * indent
    print(f'{prefix}- Compare {left} vs {right}')
    prefix += '  '

    if isinstance(left, list) and isinstance(right, list):
        for l, r in zip(left, right):
            compare(l, r, indent + 2)
        if len(left) < len(right):
            print(f'{prefix}- Left side ran out of items, so inputs are in the right order')
            raise Ordered
        elif len(left) > len(right):
            print(f'{prefix}- Right side ran out of items, so inputs are not in the right order')
            raise Unordered

        # Equal lists
        return

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            print(f'{prefix}- Left side is smaller, so inputs are in the right order')
            raise Ordered
        elif left > right:
            print(f'{prefix}- Right side is smaller, so inputs are not in the right order')
            raise Unordered
        else:
            # Equal compare, continue
            return

    # mixed types
    left = left if isinstance(left, list) else [left]
    right = right if isinstance(right, list) else [right]
    print(f'{prefix}- Mixed types; convert to {left}, {right} and retry comparison')
    return compare(left, right, indent + 2)


order_sum = 0
for i, packet in enumerate(packets):
    print(f'\n== Pair {i + 1} ==')
    left, right = packet

    try:
        compare(left, right)
    except Ordered:
        order_sum += i + 1
    except Unordered:
        pass

print(order_sum)
