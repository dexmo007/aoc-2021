with open('input.txt') as f:
    lines = f.readlines()

commands = []

for line in lines:
    command, value = line.strip().split(' ')
    value = int(value)
    commands.append((command, value))

position = 0, 0

for command, value in commands:
    x, y = position
    if command == 'up':
        y -= value
    elif command == 'down':
        y += value
    elif command == 'forward':
        x += value
    position = x, y

x, y = position
print(x*y)
