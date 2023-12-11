import heapq

def neighbors4(r, c, h, w):
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        rr, cc = (r + dr, c + dc)
        if 0 <= rr < h and 0 <= cc < w:
            yield (rr, cc)

def dijkstra(grid, source):
    h, w = len(grid), len(grid[0])
    queue = [(0, source)]
    visited = set()
    path = []

    while queue:
        # Get the node with lowest distance from the queue (and its distance)
        dist, node = heapq.heappop(queue)

        # If we already visited this node, skip it, proceed to the next one.
        if node in visited:
            continue
        
        # Mark the node as visited.
        visited.add(node)
        path.append((dist,node))
        r, c = node

        # For each unvisited neighbor of this node...
        for neighbor in neighbors4(r, c, h, w):
            if neighbor in visited:
                continue
            nr, nc  = neighbor
            if(grid[nr][nc] == '.'):
                continue
            if grid[r][c] == 'S' and (grid[nr][nc] == '-' or grid[nr][nc] == '|'):
                heapq.heappush(queue, (dist + 1, neighbor))
            if nr == r and nc > c and (grid[r][c] == '-' or grid[r][c] == 'L' or grid[r][c] == 'F'):
                if grid[nr][nc] == '-' or grid[nr][nc] == '7' or grid[nr][nc] == 'J':
                    heapq.heappush(queue, (dist + 1, neighbor))
            elif nr == r and nc < c and (grid[r][c] == '-' or grid[r][c] == 'J' or grid[r][c] == '7'):
                if grid[nr][nc] == '-' or grid[nr][nc] == 'F' or grid[nr][nc] == 'L':
                    heapq.heappush(queue, (dist + 1, neighbor))
            elif nr > r and nc == c and (grid[r][c] == '|' or grid[r][c] == 'F' or grid[r][c] == '7'):
                if grid[nr][nc] == '|' or grid[nr][nc] == 'L' or grid[nr][nc] == 'J':
                    heapq.heappush(queue, (dist + 1, neighbor))
            elif nr < r and nc == c and (grid[r][c] == '|' or grid[r][c] == 'J' or grid[r][c] == 'L'):
                if grid[nr][nc] == '|' or grid[nr][nc] == 'F' or grid[nr][nc] == '7':
                    heapq.heappush(queue, (dist + 1, neighbor))
                
    # print(path)
    return path, visited

input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())
puzzle_input = []

for a in input:
    puzzle_input.append([x for x in str(a)])

for x in range(len(input)):
    if input[x].find('S') != -1:
        source = (x,input[x].index('S'))
path, visited = dijkstra(puzzle_input,source)
print('Part 1: ', path[-1])

#Making the Source pipe the correct pipe
r,c = source
dir = []
for neighbor in neighbors4(r,c,len(input), len(input[0])):
    nr,nc = neighbor
    if puzzle_input[nr][nc] == '-':
        if nc > c:
            dir.append('R')
        else:
            dir.append('L')
    if puzzle_input[nr][nc] == '|':
        if nr > r:
            dir.append('D')
        else:
            dir.append('U')

if 'U' in dir:
    if 'L' in dir: 
        puzzle_input[r][c] = 'J'
    else:
        puzzle_input[r][c] = 'L'
else:
    if 'L' in dir:
        puzzle_input[r][c] = '7'
    else:
        puzzle_input[r][c] = 'F'

part_2 = 0
for y in range(len(input)):
    for x in range(len(input[y])):
        if (y,x) in visited:
            continue
        cross = 0
        crosses = []
        x2 = x + 1
        y2 = y + 1
        while x2 < len(input[y]) and y2 < len(input):
            if (y2,x2) in visited and puzzle_input[y2][x2] != "L" and puzzle_input[y2][x2] != "7":
                crosses.append((x2,y2,puzzle_input[y2][x2]))
                cross += 1
            x2 += 1
            y2 += 1
        if cross % 2 == 1:
            part_2+=1
print('Part 2: ', part_2)
