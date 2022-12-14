import numpy as np

input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

parsed = []
x=[0,0] #min/max values
y=[0,0] #min/max values
for a in input:
    a = a.split(' -> ')
    parsed.append(a)
    for step in range(len(a)):
        temp = [int(z) for z in a[step].split(',')]
        if x == [0,0]:
            x = [temp[0],temp[0]]
            y = [temp[1],temp[1]]
        if temp[0] < x[0]:
            x[0] = temp[0]
        if temp[0] > x[1]:
            x[1] = temp[0]
        if temp[1] < y[0]:
            y[0] = temp[1]
        if temp[1] > y[1]:
            y[1] = temp[1]
#h = y[1]+1             #part 1
#w = x[1]-x[0]+center+1        #part 1
#center = 0                     #part 1
h = y[1]+3 #part 2
w = 1 + (2 * (y[1] + 3))
center = (y[1] + 4) - (500 - x[0])
y[1]+=2
grid = np.full((h,w),0)
for a in range(len(grid[0])):
    grid[h-1][a] = 1
for a in parsed:
    for step in range(len(a)):
        temp = [int(z) for z in a[step].split(',')]
        if step == 0:
            grid[temp[1]][temp[0]-x[0]+center] = 1
        else:
            temp2 = [int(z) for z in a[step-1].split(',')]
            if temp[0] == temp2[0]:
                if temp[1] > temp2[1]:
                    for fill in range(temp2[1], temp[1]+1):
                        grid[fill][temp[0]-x[0]+center] = 1
                else:
                    for fill in range(temp[1], temp2[1]+1):
                        grid[fill][temp[0]-x[0]+center] = 1
            else:
                if temp[0] > temp2[0]:
                    for fill in range(temp2[0], temp[0]+1):
                        grid[temp[1]][fill-x[0]+center] = 1
                else:
                    for fill in range(temp[0], temp2[0]+1):
                        grid[temp[1]][fill-x[0]+center] = 1

count = 0
canStop = True
while canStop:
    stepStart = [0,500-x[0]+center]
    dropping = True
    while dropping:
        if stepStart[0] >= y[1] or stepStart[1] >= w or stepStart[1] < 0:
            canStop = False
            break
        if grid[stepStart[0]+1][stepStart[1]] == 0:
            stepStart[0] = stepStart[0]+1
        elif stepStart[1] - 1 < 0:
            canStop = False
            break
        elif grid[stepStart[0]+1][stepStart[1]-1] == 0:
            stepStart[0] = stepStart[0]+1
            stepStart[1] = stepStart[1]-1
        elif stepStart[1] + 1 >= w:
            canStop = False
            break
        elif grid[stepStart[0]+1][stepStart[1]+1] == 0:
            stepStart[0] = stepStart[0]+1
            stepStart[1] = stepStart[1]+1
        else:
            grid[stepStart[0]][stepStart[1]] = 1
            dropping = False
            count += 1
            if stepStart == [0,500-x[0]+center]:
                canStop = False
                break


print(grid)
print(count)
