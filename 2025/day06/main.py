import math

input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

problems = []
operator = []

part_1 = 0
part_2 = 0

for a in input:
    if a.find('*') == -1:
        problems.append([int(x) for x in a.split()])
    else:
        operator = a.split()

for index, x in enumerate(operator):
    total = 0
    if x == '*':
        total = 1
    for y in range(len(problems)):
        if x == '+':
            total += problems[y][index]
        else:
            total *= problems[y][index]
    part_1 += total

print('Part 1: ', part_1)

problems = []
operator = []

for a in input:
    if a.find('*') == -1:
        problems.append(a)
    else:
        operator = a

def findNext(opString, start):
    add = opString.find('+', start)
    if add == -1:
        add = math.inf
    mult = opString.find('*', start)
    if mult == -1:
        mult = math.inf
    return min(add,mult)

parseP = []
parseO = []

for index, a in enumerate(operator):
    total = 0
    if a == '*':
        total = 1
    if a != ' ':
        nextIndex = findNext(operator,index+1)
        if nextIndex == math.inf:
            nextIndex = len(operator)+1
        for x in range(index, nextIndex-1):
            tempValue = ''
            for y in problems:
                if y[x] != ' ':
                    tempValue += y[x]
            tempValue = int(tempValue)
            if a == '+':
                total += tempValue
            else:
                total *= tempValue
        part_2 += total

    
print('Part 2: ', part_2)