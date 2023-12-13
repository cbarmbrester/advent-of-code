input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())
grid = []

def mirror(grid, part=1):
    found = False
    at = -1
    for x in range(len(grid) - 1):
        if found:
            break
        count = 0
        for z in range(len(grid[x])):
            if grid[x][z] != grid[x+1][z]:
                count += 1
        if count <= 1:
            found = True
            at = x
            y = x+2
            for x in range(x-1, x-min(x, len(grid)-x-2)-1, -1):
                if grid[x] != grid[y]:
                    for z in range(len(grid[x])):
                        if grid[x][z] != grid[y][z]:
                            count += 1
                y+=1
            if part == 1 and count != 0:
                found = False
            elif part == 2 and count != 1:
                found = False
    return found, at+1

part_1 = 0
part_2 = 0
for i, line in enumerate(input):
    if line != '' and i < len(input) - 1:
        grid.append([x for x in line])
        continue
    found, at = mirror(grid)
    if found:
        part_1 += (100 * at)
    else:
        found, at = mirror(list(zip(*grid[::-1])))
        if found:
            part_1 += at
    #Part 2
    found, at = mirror(grid, 2)
    if found:
        part_2 += (100 * at)
    else:
        found, at = mirror(list(zip(*grid[::-1])), 2)
        if found:
            part_2 += at
    
    grid = []
print('Part 1: ', part_1)
print('Part 2: ', part_2)