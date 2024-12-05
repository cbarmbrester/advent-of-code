input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

total_1 = 0
total_2 = 0

rules = {}

for a in input:
    if len(a) == 0:
        continue
    if a.find('|') > -1:
        temp = [int(x) for x in a.split('|')]
        if temp[0] in rules.keys():
            rules[temp[0]].append(temp[1])
        else:
            rules[temp[0]] = [temp[1]]
    elif a.find(',') > -1:
        temp = [int(x) for x in a.split(',')][::-1]
        correctOrder = False
        loop = 1
        while correctOrder == False:
            correctOrder = True
            for x in range(len(temp)-1):
                if temp[x] in rules.keys():
                    if not set(temp[x+1:]).isdisjoint(rules[temp[x]]):
                        correctOrder = False
                        break
            if not correctOrder:
                temp.append(temp.pop(x))
                loop += 1
        if loop == 1:
            total_1 += temp[int((len(temp)-1)/2)]
        else:
            total_2 += temp[int((len(temp)-1)/2)]

print("Part 1: ", total_1)
print("Part 2: ", total_2)