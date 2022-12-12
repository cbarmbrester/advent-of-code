import heapq

def neighbors4(r, c, h, w):
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        rr, cc = (r + dr, c + dc)
        if 0 <= rr < h and 0 <= cc < w:
            yield (rr, cc)

def dijkstra(grid, source, destination):
    h, w = len(grid), len(grid[0])

    # Start with only the source in our queue of nodes to visit and in the
    # mindist dictionary, with distance 0.
    queue = [(0, source)]
    steps = 0
    visited = set()

    while queue:
        # Get the node with lowest distance from the queue (and its distance)
        dist, node = heapq.heappop(queue)
        print(dist, node)

        # If we got to the destination, we have our answer.
        if node in destination:
            print('Correct')
            return dist

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
#            if(grid[r][c] < grid[nr][nc] - 1):
            if(grid[r][c] > grid[nr][nc] + 1):
                continue
            heapq.heappush(queue, (dist + 1, neighbor))

    # If we ever empty the queue without entering the node == destination check
    # in the above loop, there is no path from source to destination!
    print('Oops')
    return steps

input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())
puzzle_input = []
source_2 = set()

for a in input:
    puzzle_input.append([x for x in str(a)])

for x in range(len(puzzle_input)):
    for y in range(len(puzzle_input[x])):
        if(puzzle_input[x][y] != 'S' and puzzle_input[x][y] != 'E'):
            puzzle_input[x][y] = (ord(puzzle_input[x][y]) - 96)
            if(puzzle_input[x][y] == 1):
                source_2.add((x,y))
        elif(puzzle_input[x][y] == 'S'):
            source = (x,y)
            source_2.add((x,y))
            puzzle_input[x][y] = 1
        else:
            destination = (x,y)
            puzzle_input[x][y] = 26

#print(dijkstra(puzzle_input, source, set(destination)))
print(dijkstra(puzzle_input, destination, source_2))