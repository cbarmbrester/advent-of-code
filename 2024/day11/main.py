from collections import Counter

input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())[0]
input = [int(x) for x in input.split(' ')]

puzzle_input = []
d = Counter(input)

for i in range(75):
    newD = Counter()
    for a in d:
        if a == 0:
            newD[1] += d[a]
        elif len(str(a)) % 2 == 0:
            newD[int(str(a)[0:int(len(str(a))/2)])] += d[a]
            newD[int(str(a)[int(len(str(a))/2):])] += d[a]
        else:
            newD[a*2024] += d[a]
    d = newD
    if i == 24:
        print('Part 1: ', sum(d.values()))

print('Part 2: ', sum(d.values()))