from collections import Counter

total = 0
setbits = Counter()

for line in [l.strip() for l in open('input.txt').readlines()]:
    total += 1
    setbits.update({i: int(v) for i, v in enumerate(line)})

gamma = ''.join('1' if setbits[i] > total/2 else '0' for i in range(len(setbits)))
epsilon = ''.join('0' if c == '1' else '1' for c in gamma)

print(f'gamma: {gamma}')
print(f'epsilon: {epsilon}')

print(int(gamma, base=2) * int(epsilon, base=2))
# 2498354
