import os

MAX_AGE = 8
AFTER_SPAWN_AGE = 6

lanternfish = [0 for _ in range(MAX_AGE + 1)]

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    for line in f:
        for age in line.strip().split(','):
            lanternfish[int(age)] += 1

days = 256

for _ in range(days):
    n = lanternfish.pop(0)
    lanternfish[AFTER_SPAWN_AGE] += n
    lanternfish.append(n)

print(sum(lanternfish))
