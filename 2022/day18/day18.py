def neighbors6(x, y, z):
    for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
        xx, yy, zz = (x + dx, y + dy, z + dz)
        yield (xx, yy, zz)
        
input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())
points = set()
for a in input:
    points.add(tuple(map(int, a.split(','))))

part_1 = 0
for a in points:
    for neighbor in neighbors6(a[0], a[1], a[2]):
        if neighbor not in points:
            part_1 += 1

print('Part 1: ', part_1)

min_x = min(x for x,y,z in points)
max_x = max(x for x,y,z in points)
min_y = min(y for x,y,z in points)
max_y = max(y for x,y,z in points)
min_z = min(z for x,y,z in points)
max_z = max(z for x,y,z in points)

x_range = range(min_x, max_x+1)
y_range = range(min_y, max_y+1)
z_range = range(min_z, max_z+1)

known_exterior = set()

def exterior(x, y, z):
    if (x, y, z) in points:
        return False

    checked = set()
    todo = [(x, y, z)]

    while todo:
        x, y, z = todo.pop()
        if (x, y, z) in checked:
            continue
        checked.add((x, y, z))
        if (x, y, z) in known_exterior:
            known_exterior.update(checked - points)
            return True
        if x not in x_range or y not in y_range or z not in z_range:
            # We breached the range, it's exterior!
            known_exterior.update(checked - points)
            return True
        if (x, y, z) not in points:
            todo += neighbors6(x, y, z)

    # We couldn't reach the outside!
    return False

answer = 0

for x, y, z in points:
    for neighbor in neighbors6(x, y, z):
        if exterior(neighbor[0], neighbor[1], neighbor[2]):
            answer += 1
print('Part 2: ', answer)