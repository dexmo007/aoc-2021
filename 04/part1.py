import os
import re

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    numbers = [int(n.strip()) for n in next(f).split(',')]
    next(f)
    boards = [[]]
    for line in f:
        if not line.strip():
            boards.append([])
            continue
        boards[-1].append([(int(n), False)
                          for n in re.split(r"\s+", line.strip())])


def find_index(board: list[list[int]], n: int):
    for i, row in enumerate(board):
        for j, (value, _) in enumerate(row):
            if value == n:
                return (i, j)
    return (-1, None)


def has_bingo(board: list[list[int]]):
    for row in board:
        for (_, hit) in row:
            if not hit:
                break
        else:
            return True
    for i in range(len(board[0])):
        for j in range(len(board)):
            _, hit = board[j][i]
            if not hit:
                break
        else:
            return True
    return False


result = None
try:
    for n in numbers:
        for board in boards:
            i, j = find_index(board, n)
            if i != -1:
                board[i][j] = (n, True)
            if not has_bingo(board):
                continue
            result = n * sum(v for row in board for (v, hit) in row if not hit)
            raise StopIteration
except StopIteration:
    pass
print(result)
