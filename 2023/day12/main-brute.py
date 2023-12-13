import math
import re

input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

part_1 = 0
for line in input:
    parse = line.split(' ')
    segment = parse[1].split(',')
    reg = '[#]{' + segment[0] + '}'
    for z in range(1, len(segment)):
        reg += '[.]+[#]{' + segment[z] + '}'
    count = line.count('?')
    poss = 0
    for x in range(int(math.pow(2,count))):
        bit = bin(x)[2:].zfill(count)
        temp = list(parse[0])
        question = 0
        for y in range(len(temp)):
            if temp[y] == '?':
                if bit[question] == '1':
                    temp[y] = '#'
                else:
                    temp[y] = '.'
                question += 1
        temp = ''.join(temp)
        if temp.count('#') != sum([int(x) for x in segment]):
            continue
        found = re.search(reg, temp)
        if found:
            poss += 1
            # print(temp, segment)
    # print(poss)
    part_1 += poss
print('Part 1: ', part_1)