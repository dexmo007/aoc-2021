from collections import defaultdict

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]


def get_occurances(numbers, bit_position):
    occurances = defaultdict(lambda: 0)
    for number in numbers:
        occurances[number[bit_position]] += 1
    return occurances


def get_metric(bit_criteria, draw_value):
    numbers = lines[:]
    i = 0
    while len(numbers) > 1:
        occurances = get_occurances(numbers, i)
        if occurances['0'] == occurances['1']:
            keep = draw_value
        else:
            keep = bit_criteria(occurances, key=occurances.get)
        numbers = list(n for n in numbers if n[i] == keep)
        i += 1
    return int(numbers[0], 2)


oxygen_generator_rating = get_metric(max, '1')
co2_scrubber_rating = get_metric(min, '0')

life_support_rating = oxygen_generator_rating * co2_scrubber_rating

print(life_support_rating)
