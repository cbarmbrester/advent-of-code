input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

total_1 = set()
total_2 = set()
d = {}
r = len(input)
c = len(input[0])

for x, a in enumerate(input):
    for y, b in enumerate(a):
        if b == '.':
            continue
        if b in d.keys():
            d[b].append((x,y))
        else:
            d[b] = [(x,y)]
        total_2.add((x,y))

for a in d:
    for i, b in enumerate(d[a]):
        x1, y1 = b
        for j in range(i+1, len(d[a])):
            x2, y2 = d[a][j]
            dx = x2-x1
            dy = y2-y1
            loop = 1
            while True:
                if 0 <= x1-(loop * dx) < c and 0 <= y1-(loop * dy) < r:
                    total_2.add((x1-(loop * dx), y1-(loop * dy)))
                    if loop == 1:
                        total_1.add((x1-dx, y1-dy))
                    loop += 1
                else:
                    break
            loop = 1
            while True:
                if 0 <= x2+(loop * dx) < c and 0 <= y2+(loop * dy) < r:
                    total_2.add((x2+(loop * dx), y2+(loop * dy)))
                    if loop == 1:
                        total_1.add((x2+dx, y2+dy))
                    loop += 1
                else:
                    break

print('Part 1: ', len(total_1))
print('Part 2: ', len(total_2))