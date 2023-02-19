import os
import re

vents = []

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    for line in f:
        m = re.match(r'(\d+),(\d+) -> (\d+),(\d+)', line.strip())
        x1, y1, x2, y2 = [int(s) for s in m.groups()]
        vents.append(((x1, y1), (x2, y2)))

max_x = max(max(start[0], end[0]) for start, end in vents)
max_y = max(max(start[1], end[1]) for start, end in vents)

grid = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

for start, end in vents:
    x1, y1 = start
    x2, y2 = end
    if x1 != x2 and y1 != y2:
        continue
    dx = abs(x1 - x2)
    dirx = -1 if x2 < x1 else 1 if x2 > x1 else 0
    dy = abs(y1 - y2)
    diry = -1 if y2 < y1 else 1 if y2 > y1 else 0
    cx, cy = x1, y1
    grid[cy][cx] += 1
    for _ in range(max(dx, dy)):
        cx, cy = cx+dirx, cy+diry
        grid[cy][cx] += 1

result = sum(1 if overlap >= 2 else 0 for row in grid for overlap in row)

print(result)
