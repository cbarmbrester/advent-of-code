input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

total_1 = 0
total_2 = 0
reverseIndex = len(input[0])-1
fileNum = 0
sList = list(input[0])

for x, a in enumerate(sList):
    if x >= reverseIndex:
        break
    if x % 2 == 0:
        for i in range(int(a)):
            total_1 += int(x / 2) * fileNum
            fileNum += 1
    elif x % 2 == 1:
        for i in range(int(a)):
            while True:
                if sList[reverseIndex] == '0':
                    reverseIndex -= 2
                else:
                    break
            if x >= reverseIndex:
                break
            total_1 += int(reverseIndex / 2) * fileNum
            fileNum += 1
            sList[reverseIndex] = str(int(sList[reverseIndex])-1)

if x == reverseIndex:
    for i in range(int(sList[reverseIndex])):
        total_1 += int(reverseIndex / 2) * fileNum
        fileNum += 1
    
print('Part 1: ', total_1)

sList = list(input[0])
iList = []
fullFile = 0

for x, a in enumerate(sList):
    iList.append(fullFile)
    fullFile+=int(a)
    
for x in range(len(sList)-1, -1, -2):
    moved = False
    for y in range(1,x,2):
        if int(sList[y]) >= int(sList[x]):
            total_2 += int(x/2) * int((int(sList[x]) / 2) * ((2 * iList[y]) + int(sList[x]) - 1))
            sList[y] = str(int(sList[y]) - int(sList[x]))
            iList[y] += int(sList[x])
            moved = True
            break
    if not moved:
        total_2 += int(x/2) * int((int(sList[x]) / 2) * ((2 * iList[x]) + int(sList[x]) - 1))      

print('Part 2: ', total_2)