import heapq

def neighbors4(r, c, h, w):
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        rr, cc = (r + dr, c + dc)
        if 0 <= rr < h and 0 <= cc < w:
            yield (rr, cc)
            
d2 = {1: (1, 0), 3: (-1, 0), 2: (0, -1), 0: (0, 1)}

def dijkstra(grid, source):
    h, w = len(grid), len(grid[0])
    
    # Start with only the source in our queue of nodes to visit and in the
    # mindist dictionary, with distance 0.
    queue = []
    queue.append((0, source))
    visited = set()

    while queue:
        # Get the node with lowest distance from the queue (and its distance)
        dist, node = heapq.heappop(queue)
        
        # If we already visited this node, skip it, proceed to the next one.
        if node in visited:
            continue
        
        # Mark the node as visited.
        visited.add(node)
        r, c = node

        # For each unvisited neighbor of this node...
        for neighbor in neighbors4(r, c, h, w):
            if neighbor in visited:
                continue
            nr, nc  = neighbor
            if(grid[r][c] != grid[nr][nc]):
                continue
            heapq.heappush(queue, (dist + 1, neighbor))

    return visited


input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

total_1 = 0
total_2 = 0
puzzle_input = []
fence = {}
corners = {}

for a in input:
    puzzle_input.append([x for x in str(a)])
    
h, w = len(puzzle_input), len(puzzle_input[0])

for x, a in enumerate(puzzle_input):
    for y, b in enumerate(puzzle_input[x]):
        totalFence = 0
        if x == 0 or x == h - 1:
            totalFence += 1
        if y == 0 or y == w - 1:                
            totalFence += 1
        for neighbor in neighbors4(x, y, h, w):
            nr, nc  = neighbor
            if(puzzle_input[x][y] == puzzle_input[nr][nc]):
                continue
            totalFence+= 1
        fence[(x,y)] = totalFence
        
for x in range(len(puzzle_input)):
    for y in range(len(puzzle_input[0])):
        if puzzle_input[x][y] != '.':
            visit = dijkstra(puzzle_input, (x,y))
            # print(puzzle_input[x][y], visit)
            temp_2 = 0
            for x1, y1 in visit:
                total_1 += (len(visit) * fence[(x1, y1)])                
                # Outer corners
                temp_2 += ( x1 - 1, y1 ) not in visit and ( x1, y1 - 1 ) not in visit
                temp_2 += ( x1 + 1, y1 ) not in visit and ( x1, y1 - 1 ) not in visit
                temp_2 += ( x1 - 1, y1 ) not in visit and ( x1, y1 + 1 ) not in visit
                temp_2 += ( x1 + 1, y1 ) not in visit and ( x1, y1 + 1 ) not in visit
                # Inner corners
                temp_2 += ( x1 - 1, y1 ) in visit and ( x1, y1 - 1 ) in visit and ( x1 - 1, y1 - 1 ) not in visit
                temp_2 += ( x1 + 1, y1 ) in visit and ( x1, y1 - 1 ) in visit and ( x1 + 1, y1 - 1 ) not in visit
                temp_2 += ( x1 - 1, y1 ) in visit and ( x1, y1 + 1 ) in visit and ( x1 - 1, y1 + 1 ) not in visit
                temp_2 += ( x1 + 1, y1 ) in visit and ( x1, y1 + 1 ) in visit and ( x1 + 1, y1 + 1 ) not in visit
                
                puzzle_input[x1][y1] = '.'
            total_2 += len(visit) * temp_2
    
print('Part 1: ', total_1)
print('Part 2: ', total_2)