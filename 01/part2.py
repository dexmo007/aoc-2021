n_larger = 0

with open('input.txt') as f:
    triples = []
    for line in f:
        current_value = int(line.strip())
        for triple in triples[-2:]:
            triple.append(current_value)
        triples.append([current_value])
        if len(triples) >= 4 and sum(triples[-3]) > sum(triples[-4]):
            n_larger += 1


print(n_larger)
