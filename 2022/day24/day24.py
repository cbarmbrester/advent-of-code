import heapq

input = []
f = open("./input.txt", "r")
txt = f.read()
input = txt.splitlines()

r = len(input)
c = len(input[0])
elf = (2,1)
goal = (c-1,r)
grid = []
grid_move = []

for y, row in enumerate(input, start=1):
    for x, value in enumerate(row, start=1):
        if value in '><v^':
            grid.append((x,y))
            grid_move.append((value))
            
facing = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}
blizzards = grid

def blizzard_move(grid_temp):
    for a in range(len(grid_temp)):
        x,y = grid_temp[a]
        dx, dy = facing[grid_move[a]]
        grid_temp[a] = (x+dx,y+dy)
        if x+dx == c:
            grid_temp[a] = (2,y+dy)
        elif x+dx == 1:
            grid_temp[a] = (c-1,y+dy)
        elif y+dy == r:
            grid_temp[a] = (x+dx,2)
        elif y+dy == 1:
            grid_temp[a] = (x+dx,r-1)
    return grid_temp
        

def neighbors4(x, y, h, w, curBlizzard, end):
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        xx, yy = (x + dr, y + dc)
        if 1 < xx < w and 1 < yy < h and (xx,yy) not in curBlizzard:
            yield (xx, yy)
        if (xx,yy) == end:
            yield (xx, yy)
    if (x,y) not in curBlizzard:
        yield (x,y)

def bfs(turn_start, start, end, blizzards):
    next_queue = set()
    next_queue.add(start)
    step = turn_start
    curBlizzard = list(blizzards)

    done = False
    while not done and next_queue:
        curBlizzard = list(blizzard_move(curBlizzard))
        queue = next_queue
        next_queue = set()
        for pos in queue:
            if pos == end:
                done = True
                break
            x, y = pos
            for direction in neighbors4(x, y, r, c, curBlizzard,end):
                next_queue.add(direction)
        if done:
            break
        step += 1
    return step, list(curBlizzard)

part1, blizzards = bfs(0, elf, goal, blizzards)
print('Part 1:', part1)
temp_trip, blizzards = bfs(part1+1, goal, elf, blizzards)
part2,blizzards = bfs(temp_trip+1, elf, goal, blizzards)
print('Part 2:', part2)