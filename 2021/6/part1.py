fishies = {}

with open('input.txt') as f:
    for x in f.read().split(','):
        fishies[int(x)] = fishies.get(int(x), 0) + 1

for _ in range(80):
    fishies = {
        age - 1: quantity for age, quantity in fishies.items()
    }

    fishies[6] = fishies.get(6, 0) + fishies.get(-1, 0)
    fishies[8] = fishies.get(-1, 0)
    if -1 in fishies: del fishies[-1]

print(sum(fishies.values()))
# 362666
