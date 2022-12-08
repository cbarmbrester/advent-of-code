import numpy as np

input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())
grid = []

for a in input:
    grid.append([x for x in str(a)])
forest = np.array(grid)

part_1 = 0
for x in range(len(forest[0])):
    for y in range(len(forest)):
        if(x == 0 or y == 0 or x == len(forest[0]) - 1 or y == len(forest) - 1):
            part_1 += 1
        else:
            tree = forest[x][y]
            left = max(forest[x,0:y])
            right = max(forest[x,y+1:])
            up = max(forest[0:x,y])
            down = max(forest[x+1:,y])
            if(tree > left or tree > right or tree > up or tree > down):
                part_1 += 1

print(part_1)
        
part_2 = np.full((len(forest[0]),len(forest)),0)

for x in range(len(forest[0])):
    for y in range(len(forest)):
        if(x == 0 or y == 0 or x == len(forest[0]) - 1 or y == len(forest) - 1):
            part_2[x][y] = 0
        else:
            tree = forest[x][y]
            sides = np.zeros(4, dtype =object)
            sides[0] = np.flip(forest[x,0:y])
            sides[1] = forest[x,y+1:]
            sides[2] = np.flip(forest[0:x,y])
            sides[3] = forest[x+1:,y]

            tree_count = 1
            for z in range(4):
                temp_count = 0
                for side in range(len(sides[z])):
                    if(tree > sides[z][side]):
                        temp_count += 1
                    else:
                        temp_count += 1
                        break
                tree_count *= temp_count
            part_2[x][y] = tree_count

print(np.amax(part_2))