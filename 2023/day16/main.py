import heapq

d = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

def neighbors4(r, c, h, w, direction):
    dr, dc = d[direction]
    rr, cc = (r + dr, c + dc)
    if 0 <= rr < h and 0 <= cc < w:
        yield (rr, cc)

def dijkstra(grid, source, direction='R'):
    h, w = len(grid), len(grid[0])
    queue = [(direction, source)]
    seen = set()
    visit = set()

    while queue:
        direction, node = heapq.heappop(queue)
        # If we already visited this node, skip it, proceed to the next one.
        if (direction, node) in seen:
            continue

        # Mark the node as visited.
        seen.add((direction, node))
        visit.add(node)
        r, c = node

        # For each unvisited neighbor of this node...
        for neighbor in neighbors4(r, c, h, w, direction):
            if (direction, neighbor) in visit:
                continue
            nr, nc  = neighbor
            if(grid[nr][nc] == '|'):
                if direction in ('R', 'L'):
                    heapq.heappush(queue, ('U', neighbor))
                    heapq.heappush(queue, ('D', neighbor))
                else:
                    heapq.heappush(queue, (direction, neighbor))
            elif(grid[nr][nc] == '-'):
                if direction in ('U', 'D'):
                    heapq.heappush(queue, ('L', neighbor))
                    heapq.heappush(queue, ('R', neighbor))
                else:
                    heapq.heappush(queue, (direction, neighbor))
            elif(grid[nr][nc] == '|'):
                if direction in ('R', 'L'):
                    heapq.heappush(queue, ('U', neighbor))
                    heapq.heappush(queue, ('D', neighbor))
                else:
                    heapq.heappush(queue, (direction, neighbor))
            elif(grid[nr][nc] == '/'):
                if direction == 'U':
                    heapq.heappush(queue, ('R', neighbor))
                elif direction == 'R':
                    heapq.heappush(queue, ('U', neighbor))
                elif direction == 'L':
                    heapq.heappush(queue, ('D', neighbor))
                elif direction == 'D':
                    heapq.heappush(queue, ('L', neighbor))
            elif(grid[nr][nc] == '\\'):
                if direction == 'U':
                    heapq.heappush(queue, ('L', neighbor))
                elif direction == 'L':
                    heapq.heappush(queue, ('U', neighbor))
                elif direction == 'R':
                    heapq.heappush(queue, ('D', neighbor))
                elif direction == 'D':
                    heapq.heappush(queue, ('R', neighbor))
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
    
print('Part 1: ', len(dijkstra(grid, (0,-1)))-1)

part_2 = 0
for x in range(len(grid)):
    part_2 = max(part_2, len(dijkstra(grid, (x,-1),'R'))-1)
    part_2 = max(part_2, len(dijkstra(grid, (x,len(grid[0])),'L'))-1)
for x in range(len(grid[0])):
    part_2 = max(part_2, len(dijkstra(grid, (-1,x),'D'))-1)
    part_2 = max(part_2, len(dijkstra(grid, (len(grid),x),'U'))-1)
print('Part 2: ', part_2)
    