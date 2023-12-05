input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

maps = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
seeds = []
part_1 = set()

counter = 0
while counter < len(input):
    if input[counter].find('seeds:') > -1:
        temp = input[counter].split(': ')[1].split(' ')
        for x in temp:
            seeds.append(x)
    elif input[counter].find('seed-') > -1:
        counter +=1
        while input[counter] != '':
            temp = input[counter].split(' ')
            temp = [int(x) for x in temp]
            maps[0].append((temp[0], temp[1], temp[2]))
            counter+=1
    elif input[counter].find('soil-') > -1:
        counter +=1
        while input[counter] != '':
            temp = input[counter].split(' ')
            temp = [int(x) for x in temp]
            maps[1].append((temp[0], temp[1], temp[2]))
            counter+=1
    elif input[counter].find('fertilizer-') > -1:
        counter +=1
        while input[counter] != '':
            temp = input[counter].split(' ')
            temp = [int(x) for x in temp]
            maps[2].append((temp[0], temp[1], temp[2]))
            counter+=1
    elif input[counter].find('water-') > -1:
        counter +=1
        while input[counter] != '':
            temp = input[counter].split(' ')
            temp = [int(x) for x in temp]
            maps[3].append((temp[0], temp[1], temp[2]))
            counter+=1
    elif input[counter].find('light-') > -1:
        counter +=1
        while input[counter] != '':
            temp = input[counter].split(' ')
            temp = [int(x) for x in temp]
            maps[4].append((temp[0], temp[1], temp[2]))
            counter+=1
    elif input[counter].find('temperature-') > -1:
        counter +=1
        while input[counter] != '':
            temp = input[counter].split(' ')
            temp = [int(x) for x in temp]
            maps[5].append((temp[0], temp[1], temp[2]))
            counter+=1
    elif input[counter].find('humidity-') > -1:
        counter +=1
        while counter < len(input):
            temp = input[counter].split(' ')
            temp = [int(x) for x in temp]
            maps[6].append((temp[0], temp[1], temp[2]))
            counter+=1
    counter+=1
            
for x in seeds:
    currLoc = int(x)
    for y in range(7):
        change = False
        for z in range(len(maps[y])):
            a,b,c = maps[y][z]
            if currLoc >= b and currLoc < b+c:
                currLoc = a + currLoc - b
                change = True
            if change:
                break
    part_1.add(currLoc)
print('Part 1: ', min(part_1))

seeds_2 = []
temp = input[0].split(': ')[1].split(' ')
temp = [int(x) for x in temp]
for x in range(int(len(temp) / 2)):
    seeds_2.append((temp[2*x], temp[2*x] + temp[2*x + 1] - 1))
    
for y in range(7):
    temp_seeds = []
    # print(seeds_2)
    for z in range(len(maps[y])):
        a,b,c = maps[y][z]
        for x in range(len(seeds_2)):
            x1,y1 = seeds_2[x]
            # print(a,b,b+c-1,x1,y1)
            if b > y1 or b+c-1 < x1:
                # print('Completely ouside range.  No change')
                continue
            elif b <= x1:
                if b+c-1>=y1:
                    # print('Completely inside range.  No split')
                    temp_seeds.append((a+x1-b, a+y1-b))
                    seeds_2[seeds_2.index((x1,y1))] = (-1,-1)
                elif b+c-1 >= x1 and b+c-1 < y1:
                    # print('Top half in range.  Split')
                    temp_seeds.append((a+x1-b,a+c-1))
                    seeds_2[seeds_2.index((x1,y1))] = ((b+c,y1))
            elif b > x1:
                if b+c+1 >= y1:
                    # print('Bottom Half in Range.  Split')
                    seeds_2[seeds_2.index((x1,y1))] = ((x1,b-1))
                    temp_seeds.append((a,a+y1-b))
                elif b+c+1 < y1:
                    # print('Fully inside.  Three split')
                    seeds_2[seeds_2.index((x1,y1))] = ((x1,b-1))
                    temp_seeds.append((a,a+c-1))
                    seeds_2.append((b+c,y1))
        while (-1,-1) in seeds_2:
            seeds_2.remove((-1,-1))
    for new in temp_seeds:
        seeds_2.append(new)

part_2 = 10000000000
for x in seeds_2:
    a,b = x
    if a < part_2:
        part_2 = a
        
print('Part 2: ', part_2)