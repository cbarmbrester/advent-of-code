input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

list1 = []
list2 = []

for a in input:
    lists = a.split('   ')
    list1.append(int(lists[0]))
    list2.append(int(lists[1]))

list1 = sorted(list1)
list2 = sorted(list2)

total = 0
for x in range(len(list1)):
    total += abs(list1[x] - list2[x])    

print("Part 1: ", total)

total = 0
for x in list1:
    total += (int(x) * int(list2.count(x)))

print("Part 2: ", total)