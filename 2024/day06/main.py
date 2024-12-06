import heapq
import copy

d = {0: (-1, 0), 2: (1, 0), 3: (0, -1), 1: (0, 1)}

def neighbors4(r, c, h, w, direction):
    dr, dc = d[direction]
    rr, cc = (r + dr, c + dc)
    if 0 <= rr < h and 0 <= cc < w:
        yield (rr, cc)

def dijkstra(grid2, source, direction=0):
    h, w = len(grid2), len(grid2[0])
    queue = [(direction, source)]
    seen = set()
    visit = set()
    # path = []

    while queue:
        direction, node = heapq.heappop(queue)
        # path.append((direction, node))
        if (direction,node) in seen:
            return -1
        # Mark the node as visited.
        seen.add((direction, node))
        visit.add(node)
        r, c = node

        # For each unvisited neighbor of this node...
        for neighbor in neighbors4(r, c, h, w, direction):
            if (direction, neighbor) in visit:
                continue
            nr, nc  = neighbor
            if(grid2[nr][nc] == '#'):
                heapq.heappush(queue, ((direction+1)%4, node))
            else:
                heapq.heappush(queue, (direction, neighbor))
                
    # print(path)
    return visit

input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

grid = []
for a in input:
    grid.append([x for x in str(a)])
    if a.find('^') > -1:
        start = (len(grid)-1, a.find('^'))

visited = dijkstra(grid, start)    
print('Part 1: ', len(visited))

visited.remove(start)
total_2 = 0

for a, b in visited:
    new_grid = copy.deepcopy(grid)
    new_grid[a][b] = '#'
    if isinstance(dijkstra(new_grid, start),int):
        total_2 += 1
        
print('Part 2: ', total_2)