input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

total = 0

for a in input:
    first = 0
    last = 0
    for b in a:
        if b.isnumeric():
            if first == 0:
                first = int(b)
                last = int(b)
            else:
                last = int(b)
    total += 10 * int(first) + int(last)
print("Part 1: ", total)

total = 0         
for a in input:
    first = 0
    last = 0
    a= a.replace('one','one1one')
    a= a.replace('two','two2two')
    a= a.replace('three','three3three')
    a= a.replace('four','four4four')
    a= a.replace('five','five5five')
    a= a.replace('six','six6six')
    a= a.replace('seven','seven7seven')
    a= a.replace('eight','eight8eight')
    a= a.replace('nine','nine9nine')
    
    for b in a:
        if b.isnumeric():
            if first == 0:
                first = int(b)
                last = int(b)
            else:
                last = int(b)
    total += 10 * int(first) + int(last)
    print(first,last)
print("Part 2: ", total)