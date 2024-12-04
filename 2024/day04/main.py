import re
from collections import defaultdict

input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

total_1 = 0
total_2 = 0

def groups(data, func):
    grouping = defaultdict(list)
    for y in range(len(data)):
        for x in range(len(data[y])):
            grouping[func(x, y)].append(data[y][x])
    return list(map(grouping.get, sorted(grouping)))


cols = groups(input, lambda x, y: x)
rows = groups(input, lambda x, y: y)
fdiag = groups(input, lambda x, y: x + y)
bdiag = groups(input, lambda x, y: x - y)


for a in rows:
    a = ''.join(a)
    total_1 += len(re.findall("XMAS", a))
    total_1 += len(re.findall("SAMX", a))

for a in cols:
    a = ''.join(a)
    total_1 += len(re.findall("XMAS", a))
    total_1 += len(re.findall("SAMX", a))

for a in fdiag:
    a = ''.join(a)
    total_1 += len(re.findall("XMAS", a))
    total_1 += len(re.findall("SAMX", a))

for a in bdiag:
    a = ''.join(a)
    total_1 += len(re.findall("XMAS", a))
    total_1 += len(re.findall("SAMX", a))

print("Part 1: ", total_1)

for x, a in enumerate(rows):
    if x == 0 or x == len(rows) - 1:
        continue
    for y, b in enumerate(a):
        if y == 0 or y == len(a) - 1:
            continue
        if b != 'A':
            continue
        count = {'M': 0, 'S': 0, 'X': 0, 'A': 0}
        count[rows[x-1][y-1]] +=1
        count[rows[x-1][y+1]] +=1
        count[rows[x+1][y+1]] +=1
        count[rows[x+1][y-1]] +=1
        if count['S'] == 2 and count['M'] == 2 and rows[x-1][y-1] != rows[x+1][y+1]:
            total_2 += 1

print("Part 2: ", total_2)