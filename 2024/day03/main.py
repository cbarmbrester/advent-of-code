import re

input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

total_1 = 0
total_2 = 0
mulOn = True

for a in input:
    memory = re.findall("mul\(\d+,\d+\)", a)
    newInstructions = re.split("mul\(\d+,\d+\)", a)
    count = 0
    for b in memory:
        if newInstructions[count].rfind('do()') > newInstructions[count].rfind('don\'t()'):
            mulOn = True
        elif newInstructions[count].rfind('don\'t()') > newInstructions[count].rfind('do()'):
            mulOn = False
        temp = [int(x) for x in re.findall("\d+,\d+", b)[0].split(',')]
        total_1 += temp[0] * temp[1]
        if mulOn:
           total_2 += temp[0] * temp[1]
        count+=1

print("Part 1: ", total_1)
print("Part 2: ", total_2)