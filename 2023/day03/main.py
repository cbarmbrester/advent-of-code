from itertools import product

input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

size = len(input)

def neighbors(cell):
    for c in product(*(range(n-1, n+2) for n in cell)):
        if c != cell and all(0 <= n < size for n in c):
            yield c

gears = {}
for x in range(len(input)):
    for y in range(len(input[0])):
        if input[y][x] == '*':
            gears[(y,x)] = {'count': 0, 'total': 1}
        
total = 0
count = 0

for x in input:
    y = 0
    while y < len(x):
        if x[y].isnumeric():
            part = True
            symbol = False
            star = False
            temp = ''
            while part:
                temp += x[y]
                seen = set()
                stack = list(neighbors((y, count)))
                while stack:
                    x1, x2 = stack.pop()
                    if (x1, x2) in seen:
                        continue
                    if input[x2][x1].isnumeric() == False and input[x2][x1] != '.':
                        symbol = True
                        if input[x2][x1] == '*':
                            star = (x2,x1)                        
                    seen.add((x1,x2))
                y+=1
                if y >= len(x):
                    part = False
                elif x[y].isnumeric() == False:
                    part = False
            if symbol:
                total += int(temp)
                if star:
                    gears[star]['count'] += 1
                    gears[star]['total'] *= int(temp)
        y+=1            
    count+=1

print(total)

total_2 = 0
for x in gears:
    if gears[x]['count'] == 2:
        total_2 += gears[x]['total']

print(total_2)