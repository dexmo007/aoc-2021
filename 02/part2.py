with open('input.txt') as f:
    lines = f.readlines()

commands = []

for line in lines:
    command, value = line.strip().split(' ')
    value = int(value)
    commands.append((command, value))

x, y = 0, 0
aim = 0

for command, value in commands:
    if command == 'up':
        aim -= value
    elif command == 'down':
        aim += value
    elif command == 'forward':
        x += value
        y += aim * value

print(x*y)
