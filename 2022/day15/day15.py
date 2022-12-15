import re
import time
start_time = time.time()

input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

index = 2000000
upperRange = 4000000

def buildRange(index, input):
    beaconRange = []
    beacons = set()
    for a in input:
        temp = re.findall(r"x=+[0123456789-]+|y=+[0123456789-]+", a)
        for x in range(len(temp)):
            temp[x] = int(temp[x].strip('xy='))
        if temp[3] == index:
            beacons.add((temp[2],temp[3]))
        distance = abs(temp[0] - temp[2]) + abs(temp[1] - temp[3])
        disIndex = distance - abs(index - temp[1])
        if disIndex >= 0:
            beaconRange.append([temp[0] - disIndex,temp[0] + disIndex])
    return beaconRange, len(beacons)

def indexGrid(beaconRange):
    solution_2 = []
    while len(beaconRange):
        append=True
        x, y = beaconRange.pop()
        for i in range(len(beaconRange)):
            dx, dy = beaconRange[i]
            if (x <= dx and y >= dx) or (x <= dy and y >= dy) or (dx <= x and dy >= x) or (dx <= y and dy >= y):
                beaconRange[i] = [min(x,dx),max(y,dy)]
                append = False
                break
        if append:
            solution_2.append([x,y])
    for i in range(len(solution_2) - 1):
        if (solution_2[i][1] + 1 == solution_2[i+1][0]) or (solution_2[i+1][1] + 1 == solution_2[i][0]):
            solution_2[i] = [min(solution_2[i][0],solution_2[i][1], solution_2[i+1][0], solution_2[i+1][1]),max(solution_2[i][0],solution_2[i][1], solution_2[i+1][0], solution_2[i+1][1])]
            solution_2.pop(i+1)
    return solution_2

#Part 1
beaconRange, beacons = buildRange(index, input)
ranges = indexGrid(beaconRange)
print('Part 1: ', ranges[0][1]-ranges[0][0] + 1 - beacons)

#Part 2
for loop in range(upperRange + 1):
    beaconRange, beacons = buildRange(loop, input)
    ranges = indexGrid(beaconRange)
    if len(ranges) > 1:
        print('Part 2: ', ranges, loop)
        break
    elif loop % 100000 == 0:
        print(loop, ': No')

m, s = divmod(time.time() - start_time, 60)    
print('{:02.0f} minute(s) {:07.4f} seconds'.format(m, s))