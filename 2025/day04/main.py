input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())
puzzle_input = []
solution = 0

def neighbors8(r, c, h, w):
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1),(1, 1), (1, -1), (-1, 1), (-1, -1)):
        rr, cc = (r + dr, c + dc)
        if 0 <= rr < h and 0 <= cc < w:
            yield (rr, cc)

for a in input:
    puzzle_input.append([x for x in str(a)])

h, w = len(puzzle_input), len(puzzle_input[0])

removed = []
loop = 1
while 1==1:
    for x in range(len(puzzle_input)):
        for y in range(len(puzzle_input[x])):
            if puzzle_input[x][y] != '@':
                continue
            count = 0
            for neighbor in neighbors8(x, y, h, w):
                nr, nc  = neighbor
                if puzzle_input[nr][nc] == '@':
                    count += 1
            if count < 4:
                solution += 1
                removed.append((x,y))
    if loop == 1:
        print('Part 1: ', solution)

    for changed in removed:
        rx, ry = changed
        puzzle_input[rx][ry] = '.'

    if len(removed) == 0:
        break
    loop += 1
    removed = []

print('Part 2: ', solution)