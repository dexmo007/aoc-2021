n_larger = 0

with open('input.txt') as f:
    previous = None
    for line in f:
        current = int(line.strip())
        if previous is not None and current > previous:
            n_larger += 1
        previous = current

print(n_larger)
