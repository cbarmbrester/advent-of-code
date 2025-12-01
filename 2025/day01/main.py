input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

start = 50
part_1 = 0
part_2 = 0

for a in input:
    d = a[0]
    num = int(a[-(len(a)-1):])
    if d == 'L':
        num *= -1

    temp = (start + num) % 100
    if temp == 0:
        part_1 += 1
    if (start + num) <= 0 and start != 0:
        part_2 += abs(int((start + num) / 100)) + 1
    else:
        part_2 += abs(int((start + num) / 100))
    start = temp
       
print('Part 1: ', part_1)
print('Part 2: ', part_2)