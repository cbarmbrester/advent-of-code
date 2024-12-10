import heapq
import copy

def neighbors4(r, c, h, w):
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        rr, cc = (r + dr, c + dc)
        if 0 <= rr < h and 0 <= cc < w:
            yield (rr, cc)

def dijkstra(grid, source, part_2):
    h, w = len(grid), len(grid[0])
    d = {}
    score = 0

    # Start with only the source in our queue of nodes to visit and in the
    # mindist dictionary, with distance 0.
    queue = []
    for a in source:        
        queue.append((0, a))
        d[a] = set()
        d[a].add(a)

    while queue:
        # Get the node with lowest distance from the queue (and its distance)
        dist, node = heapq.heappop(queue)
        if dist == 9:
            score += 1
            continue
        r, c = node

        # For each unvisited neighbor of this node...
        for neighbor in neighbors4(r, c, h, w):
            # if neighbor in visited:
                # continue
            nr, nc  = neighbor
            if(grid[r][c] != grid[nr][nc] + 1):
                continue
            if not part_2 and neighbor in d.keys():
                for o in d[node]:
                    d[neighbor].add(o)
                continue
            heapq.heappush(queue, (dist + 1, neighbor))
            d[neighbor] = copy.deepcopy(d[node])
                
    return d, score

input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())
puzzle_input = []
source = set()
dest = set()
part_1 = 0

for a in input:
    puzzle_input.append([int(x) for x in str(a)])

for x in range(len(puzzle_input)):
    for y in range(len(puzzle_input[x])):
        if(puzzle_input[x][y] == 9):
            source.add((x,y))
        elif(puzzle_input[x][y] == 0):
            dest.add((x,y))

d, score = dijkstra(puzzle_input, source, False)
temp=[]
for a in dest:
    if a not in d.keys():
        continue
    part_1 += len(d[a])
print('Part 1: ', part_1)
d, score = dijkstra(puzzle_input, source, True)
print('Part 2: ', score)