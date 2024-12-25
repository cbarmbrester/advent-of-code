from collections import Counter

input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

total_1 = 0

lock = Counter()
key = Counter()
temp = []
length = 6

for line in input:
    if len(line) > 0:
        temp.append(line)
    else:
        if temp[0] == '#####':
            sType = 'lock'
        else:
            sType = 'key'
        
        temp = list(zip(*temp[::-1]))
        pins = ''
        for a in temp:
            pins += str(a.count('#')-1)
        if sType == 'key':
            key[pins]+=1
        else:
            lock[pins]+=1
        temp = []
        
for a in list(key):
    for b in list(lock):
        bFits = True
        for x in range(5):
            if int(a[x]) + int(b[x]) >= length:
                bFits = False
                break
        if bFits:
            total_1 += key[a]
                
print('Part 1: ', total_1)