from collections import defaultdict

with open('input.txt') as f:
    lines = f.readlines()

occurances = defaultdict(lambda: defaultdict(lambda: 0))
n_bits = None
for line in lines:
    line = line.strip()
    if n_bits is None:
        n_bits = len(line)
    for i, bit in enumerate(line):
        occurances[i][bit] += 1


def get_metric(fn):
    metric = ''.join(fn(occurances[i], key=occurances[i].get)
                     for i in range(n_bits))
    return int(metric, 2)


gamma = get_metric(max)
epsilon = get_metric(min)

print(gamma * epsilon)
