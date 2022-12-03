input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())
        

elfs = []
currentElf = 0
for a in input:
    if len(a) == 0:
        elfs.append(int(currentElf))
        currentElf = 0
    else:
        currentElf += int(a)
list_sort = sorted(elfs)
list_sort = list_sort[::-1]
print ("Top 3: ", list_sort[0], list_sort[1], list_sort[2])
print ("Sum: ", list_sort[0] + list_sort[1] + list_sort[2])
