input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

d = {'U': (1, 0), 'D': (-1, 0), 'L': (0, -1), 'R': (0, 1)}
d2 = {'3': (1, 0), '1': (-1, 0), '2': (0, -1), '0': (0, 1)}

def shoe_lace(points):
    res = sum(
        points[i - 1][0] * points[i][1] - points[i][1] * points[i][0]
        for i in range(len(points))
    )
    return abs(res)

polygon = []
polygon2 = []
pos = (0,0)
pos2 = (0,0)
polygon.append(pos)
polygon2.append(pos2)
part_1 = 0
part_2 = 0

for a in input:
    x, y, z = a.split(' ')
    r,c = pos
    nr, nc = d[x]
    nr *= int(y)
    nc *= int(y)
    pos = (nr+r, nc+c)
    polygon.append(pos)
    part_1 += int(y)
        
    r,c = pos2
    nr, nc = d2[z[7]]
    nr *= int(z[2:7], 16)
    nc *= int(z[2:7], 16)
    pos2 = (nr+r, nc+c)
    polygon2.append(pos2)
    part_2 += int(z[2:7], 16)

print('Part 1: ', shoe_lace(polygon) + part_1 // 2 + 1)
print('Part 2: ', shoe_lace(polygon2) + part_2 // 2 + 1)