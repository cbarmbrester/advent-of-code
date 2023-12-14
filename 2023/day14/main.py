input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())
grid = []
grid_2 = []

def move(grid):
    for x in range(1, len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] != 'O':
                continue
            if grid[x-1][y] != '.':
                continue
            for z in range(x-1, -1, -1):
                if grid[z][y] != '.':
                    grid[z+1][y] = 'O'
                    grid[x][y] = '.'
                    break
                if z == 0:
                    grid[z][y] = 'O'
                    grid[x][y] = '.'
                    break
    return(grid)

def rotate(grid):
    list_tuples = zip(*grid[::-1])
    return([list(elem) for elem in list_tuples])

def score(grid):
    score = 0
    for x in range(len(grid)):
        score += ((len(grid) - x) * grid[x].count('O'))
    return(score)

def to_str(grid):
    return "".join(["".join(grid[i]) for i in range(len(grid))])

for line in input:
    grid.append([x for x in line])
    grid_2.append([x for x in line])

print('Part 1: ', score(move(grid)))

part_2 = {}
total_loops = 1000000000
loop = 1
while loop < total_loops:
    for inner in range(4):
        grid_2 = rotate(move(grid_2))
    x = to_str(grid_2)        
    if x in part_2:
        cycle = loop - part_2[x][0]
        for a,b in part_2.values():
            if a >= part_2[x][0] and a % cycle == total_loops % cycle:
                print('Part 2: ', b)
                loop = total_loops
    else:
        part_2[x] = (loop, score(grid_2))
        loop+=1