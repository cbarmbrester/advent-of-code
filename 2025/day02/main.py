input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

part_1 = 0
part_2 = 0

ranges = input[0].split(',')
for a in ranges:
    values = [int(x) for x in a.split('-')]
    seen_1 = []
    seen_2 = []
    for num in values:
        scale = len(str(num))
        if (num == values[1] and scale == len(str(values[0]))):
            break
        denom = []
        for x in range(1,scale):
            if scale % x == 0:
                denom.append(x)
        for x in denom:
            for y in range(int(str(num)[0:x]),10**x):
                temp = int(str(y) * int(scale/x))
                if temp > values[1]:
                    break
                if temp >= values[0] and temp <= values[1]:
                    if temp not in seen_2:
                        part_2 += temp
                        seen_2.append(temp)
                    if int(scale/x) == 2 and temp not in seen_1:
                        part_1 += temp
                        seen_1.append(temp)

print('Part 1: ', part_1)
print('Part 2: ', part_2)