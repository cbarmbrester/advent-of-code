input = []
f = open("./input.txt", "r")
txt = f.read()
input = txt.splitlines()

grid = {}
elf = 0
curLocation = []
looking = []

for y, row in enumerate(input):
    for x, value in enumerate(row):
        if value == '#':
            grid[elf] = {'location': (x,y), 'looking': None}
            elf += 1
            curLocation.append((x,y))

facing = {0: (0, -1), 1: (0, 1), 2: (-1, 0), 3: (1, 0)}
turn = 0

def neighbors8(r, c):
    for dr, dc in ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)):
        rr, cc = (r + dr, c + dc)
        yield (rr, cc)

loop = True
while loop:
    for elfIndex in range(len(grid)):
        found = [0,0,0,0]
        x, y = grid[elfIndex]['location']
        for count, neighbor in enumerate(neighbors8(x,y), start=1):
            if neighbor in curLocation:
                if count == 1 or count == 2 or count == 3:
                    found[0] = 1
                if count == 6 or count == 7 or count == 8:
                    found[1] = 1
                if count == 1 or count == 4 or count == 6:
                    found[2] = 1
                if count == 3 or count == 5 or count == 8:
                    found[3] = 1
        if any(found):
            for faceIndex in range(4):
                if not found[(turn + faceIndex) % 4]:
                    dx, dy = facing[(turn + faceIndex) % 4]
                    grid[elfIndex]['looking'] = (dx+x, dy+y)
                    looking.append((dx+x, dy+y))
                    break
    curLocation.clear()
    loop = False
    if turn % 20 == 0:
        print('Turn', turn, 'Lookings left:', len(looking))
    for elfIndex in range(len(grid)):
        if grid[elfIndex]['looking'] == None:
            curLocation.append(grid[elfIndex]['location'])
            continue
        loop = True
        if looking.count(grid[elfIndex]['looking']) == 1:
            grid[elfIndex]['location'] = grid[elfIndex]['looking']
        curLocation.append(grid[elfIndex]['location'])        
        grid[elfIndex]['looking'] = None
    looking.clear()        
     
    turn += 1
    if turn == 10:
        minx, miny = 100, 100
        maxx, maxy = -100, -100
        for location in curLocation:
            x, y = location
            minx = min(minx, x)
            miny = min(miny, y)
            maxx = max(maxx, x)
            maxy = max(maxy, y)
        print('Part 1:', (maxx-minx+1) * (maxy-miny+1) - len(grid))
print('Part 2:', turn)