from functools import cache

input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

@cache
def recurse(board, segment, result=0):
    if len(segment) == 0:
        if '#' not in board:
            return 1
        else:
            return 0
        
    current, segment = segment[0], segment[1:]
    for i in range(len(board) - sum(segment) - len(segment) - current + 1):
        if "#" in board[:i]:
            break
        next = i + current
        if next <= len(board) and '.' not in board[i:next] and board[next:next+1] != "#":
            result += recurse(board[next+1:], segment)
    return result

part_1 = 0
part_2 = 0
for line in input:
    board, segment = line.split(' ')
    segment = [int(x) for x in segment.split(',')]
    part_1 += recurse(board, tuple(segment))
    part_2 += recurse('?'.join([board] * 5), tuple(segment*5))
    
print('Part 1: ', part_1)
print('Part 2: ', part_2)