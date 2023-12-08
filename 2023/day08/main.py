from math import lcm

input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

maps = {}
loc = []

for line in input:
    if line == '':
        continue
    if line.find('=') == -1:
        route = line
    else:
        temp = line.split(' = ')
        maps[temp[0]] = {'L': temp[1].split(', ')[0].lstrip('('), 'R': temp[1].split(', ')[1].rstrip(')')}
        if temp[0][-1] == 'A':
            loc.append(temp[0])
        
step = 0
loc_1 = 'AAA'

while loc_1 != 'ZZZ':
    loc_1 = maps[loc_1][route[step % len(route)]]
    step += 1

print('Part 1: ', step)

part_2 = 1
for x in range(len(loc)):
    step = 0
    while loc[x][-1] != 'Z':
        loc[x] = maps[loc[x]][route[step % len(route)]]
        step += 1
    part_2 = lcm(part_2, step)

print('Part 2: ', part_2)