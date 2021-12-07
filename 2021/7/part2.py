crabs = {}
num_crabs = 0

with open('input.txt') as f:
    for pos in (int(x) for x in f.read().strip().split(',')):
        num_crabs += 1
        crabs[pos] = crabs.get(pos, 0) + 1

print(crabs)


def total_fuel_cost(pos, crabs):
    return sum(
        fuel_cost(abs(pos - crab_pos)) * crab_count
        for crab_pos, crab_count in crabs.items()
    )


def fuel_cost(distance):
    return sum(range(distance + 1))


lowest_fuel_cost = None

for i in range(min(crabs.keys()), max(crabs.keys())):
    c = total_fuel_cost(i, crabs)
    print(f'Cost to move to {i} is {c}')
    if lowest_fuel_cost is None or c < lowest_fuel_cost:
        lowest_fuel_cost = c

print(f'lowest fuel cost is {lowest_fuel_cost}')
# 92881128
