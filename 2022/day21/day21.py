import re

input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

inputIndex = []
rootIndex = 0
for a in range(len(input)):
    inputIndex.append(input[a].split(':')[0])
    input[a] = [input[a].split(': ')[1],a]
    if inputIndex[a] == 'root':
        rootIndex = a

def numeric(equation):
    if '+' in equation:
        y = equation.split('+')
        z = int(y[0])+int(y[1])
    elif 'minus' in equation:
        y = equation.split('minus')
        z = int(y[0])-int(y[1])
    elif '*' in equation:
        y = equation.split('*')
        z = int(y[0])*int(y[1])
    else:
        y = equation.split('/')
        z = int(int(y[0])/int(y[1]))
    return z

while len(input) > 0:
    a = input.pop(0)
    if re.search('[a-z]', a[0]) != None:
        input.append(a)
        continue
    if re.search('[-+*\/]', a[0]) != None:
        a[0] = numeric(a[0].replace('-','minus'))
    if a[1] == rootIndex:
        print('Part 1: ', a[0])
        break
    for b in range(len(input)):
        input[b][0] = input[b][0].replace(inputIndex[a[1]], str(a[0]))

input = list(txt.splitlines())
for a in range(len(input)):
    input[a] = [input[a].split(': ')[1],a]

human = input.pop(inputIndex.index('humn'))    
lastChange = 0

while len(input) > 0 and lastChange < len(input) + 2:
    a = input.pop(0)
    if re.search('[a-z]', a[0]) != None:
        input.append(a)
        lastChange += 1
        continue
    if re.search('[-+*\/]', a[0]) != None:
        a[0] = numeric(a[0].replace('-','minus'))
    if a[1] == rootIndex:
        print('Part 1: ', a[0])
        break
    for b in range(len(input)):
        input[b][0] = input[b][0].replace(inputIndex[a[1]], str(a[0]))
    lastChange = 0

nextStep = 'root'
solution = 0
curSolution = 0
temp = 0

while len(input) > 0:
    x = input.pop(0)
    if inputIndex[x[1]] == nextStep:
        a = x[0].split(' ')
        if nextStep == 'root':
            if re.search('[a-z]', a[0]) != None:
                nextStep = a[0]
                solution = a[2]
            else:
                nextStep = a[2]
                solution = int(a[0])
        else:
            if re.search('[a-z]', a[0]) != None:
                nextStep = a[0]
                curSolution = a[2]
            else:
                nextStep = a[2]
                if a[1] == '+' or a[1] == '*':
                    curSolution = a[0]
                else:
                    if a[1] == '-':
                        a[1] = '+'
                    elif a[1] == '/':
                        a[1] = '*'
                    temp = a[0]
                    curSolution = solution
                    solution = temp
            if a[1] == '+':
                a[1] = '-'
            elif a[1] == '-':
                a[1] = '+'
            elif a[1] == '*':
                a[1] = '/'
            else:
                a[1] = '*'
            solution = numeric(str(solution) + a[1].replace('-', 'minus') + str(curSolution))
    else:
        input.append(x)
        
print('Part 2: ', solution)