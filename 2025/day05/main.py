input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

ranges = []
values = []
parseFlag = False

part_1 = 0
part_2 = 0

for a in input:
    if len(a) == 0:
        parseFlag = True
        continue
    if parseFlag:
        values.append(int(a))       
    else:
        ranges.append([int(x) for x in a.split('-')])

for x in values:
    for y in ranges:
        if x in range(y[0],y[1]+1):
            part_1 += 1
            break

loopChanged = True

while loopChanged:
    temp_ranges = []
    loopChanged = False
    for x in ranges:        
        changed = False
        if len(temp_ranges) == 0:
            temp_ranges.append(x)
            continue
        for index, y in enumerate(temp_ranges):
            if x[0] in range(y[0],y[1]+1) or x[1] in range(y[0],y[1]+1) or y[0] in range(x[0],x[1]+1) or y[1] in range(x[0],x[1]+1):
                temp_ranges[index][0] = min(y[0],x[0])
                temp_ranges[index][1] = max(y[1],x[1])
                changed = True
                loopChanged = True
                break
        if not changed:
            temp_ranges.append(x)
    ranges = temp_ranges.copy()
    
for a in ranges:
    part_2 += (a[1] - a[0]) + 1

print('Part 1: ', part_1)
print('Part 2: ', part_2)