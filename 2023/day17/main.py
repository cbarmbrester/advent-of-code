import heapq
from collections import defaultdict
from math import inf as INFINITY

d = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
d2 = {tuple((-1, 0)): 'U', tuple((1, 0)): 'D', tuple((0, -1)): 'L', tuple((0, 1)): 'R'}

def neighbors4(r, c, h, w):
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        rr, cc = (r + dr, c + dc)
        if 0 <= rr < w and 0 <= cc < h:
            yield (rr, cc)

def dijkstra(grid, part_2):
    h, w = len(grid), len(grid[0])
    source = (0, 0)
    # destination = (h - 1, w - 1)

    # Start with only the source in our queue of nodes to visit and in the
    # mindist dictionary, with distance 0.
    queue = [(0, source, 'X', -1, [])]
    mindist = defaultdict(lambda: INFINITY, {source: 0})
    S = {}
    visited = set()

    while queue:
        # Get the node with lowest distance from the queue (and its distance)
        dist, node, direction, numDir, path = heapq.heappop(queue)

        # If we got to the destination, we have our answer.
        # if node == destination:
        #     return dist

        # If we already visited this node, skip it, proceed to the next one.
        if (node, direction, numDir) in visited:
            continue

        S[(node, direction, numDir)] = dist
        # Mark the node as visited.
        visited.add((node, direction, numDir))
        path.append(node)
        r, c = node

        # For each unvisited neighbor of this node...
        for neighbor in neighbors4(r, c, h, w):
            nr, nc  = neighbor

            # Calculate the total distance from the source to this neighbor
            # passing through this node.
            newdist = dist + grid[nr][nc]
            newDir = d2[(nr-r,nc-c)]
            new_numDir = (1 if newDir != direction else numDir+1)
            
            valid_1 = (new_numDir <=3)
            valid_2 = (new_numDir <=10 and (numDir >=4 or numDir == -1 or newDir == direction))
            valid = (valid_2 if part_2 else valid_1)

            if valid and neighbor not in path:
                if newdist < mindist[neighbor]:
                    mindist[neighbor] = newdist
                heapq.heappush(queue, (newdist, neighbor, newDir, new_numDir, path.copy()))

    ans = 1e9
    for (node, direction, numDir), dist in S.items():
        if node == (h-1,w-1):
            ans = min(ans, dist)
    return(ans)

input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

grid = []
for a in input:
    grid.append([int(x) for x in str(a)])

print('Part 1: ', dijkstra(grid, False))
print('Part 2: ', dijkstra(grid, True))