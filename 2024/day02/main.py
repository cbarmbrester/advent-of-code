input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

total_1 = 0
total_2 = 0
for a in input:
    lists = a.split(' ')
    flag = 0
    if all(int(lists[i]) <= int(lists[i+1]) for i in range(len(lists)-1)) or all(int(lists[j]) >= int(lists[j+1]) for j in range(len(lists)-1)):
        flag = 1
        for b in range(len(lists)-1):
            if abs(int(lists[b+1]) - int(lists[b])) > 3 or abs(int(lists[b+1]) - int(lists[b])) < 1:
                flag = 0
    if flag:
        total_1 += 1
        total_2 += 1
    else:
        for x in range(len(lists)):
            newList = lists.copy()
            newList.pop(x)
            if all(int(newList[i]) <= int(newList[i+1]) for i in range(len(newList)-1)) or all(int(newList[j]) >= int(newList[j+1]) for j in range(len(newList)-1)):
                flag = 1
                for b in range(len(newList)-1):
                    if abs(int(newList[b+1]) - int(newList[b])) > 3 or abs(int(newList[b+1]) - int(newList[b])) < 1:
                        flag = 0
            if flag:
                total_2 += 1
                break

print("Part 1: ", total_1)
print("Part 2: ", total_2)