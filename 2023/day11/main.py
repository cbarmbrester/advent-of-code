input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())
puzzle_input = []
rows = []
col = []
age = 1000000

for count, a in enumerate(input):
    puzzle_input.append([x for x in str(a)])
    if '#' not in a:
        rows.append(count)


for a in range(len(puzzle_input[0])-1,-1, -1):
    gal = False
    for b in range(len(puzzle_input)):
        if puzzle_input[b][a] == '#':
            gal = True
            break
    if gal:
        continue
    else:
        col.append(a)

gal_loc = [] 
for a in range(len(puzzle_input)):
    for b in range(len(puzzle_input[0])):
        if puzzle_input[a][b] == '#':
            gal_loc.append((a,b))

part_1 = 0
temp = 0
for a in range(len(gal_loc) - 1):
    r,c = gal_loc[a]
    for b in range(a+1, len(gal_loc)):
        nr,nc = gal_loc[b]
        col_cross = len([x for x in rows if x > min(r,nr) and x < max(r,nr)])
        row_cross = len([x for x in col if x > min(c,nc) and x < max(c,nc)])
        part_1 += abs(nr-r) + abs(nc-c) + (col_cross * age) + (row_cross * age)
        if age != 1:
            temp += col_cross + row_cross


print(part_1-temp)