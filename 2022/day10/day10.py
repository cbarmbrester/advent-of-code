input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

total = 1
counter = 0
part_1 = 0
for a in input:
    if(a.find('addx') >= 0):
        for x in range(2):
            counter += 1
            if((counter + 20) % 40 == 0):
                part_1 += (total * counter)
        total += int(a.split(' ')[-1])
    else:
        counter += 1
        if((counter + 20) % 40 == 0):
            part_1 += (total * counter)
    if(counter > 220):
        break
print(part_1)

total = 1
counter = 0
part_2 = []
for a in input:
    if(a.find('addx') >= 0):
        for x in range(2):
            counter += 1
            if((counter - 1) % 40 >= total - 1 and (counter - 1) % 40 <= total + 1):
                part_2.append('#')
            else:
                part_2.append('.')
            if(counter % 40 == 0):
                print(part_2)
                part_2.clear()
        total += int(a.split(' ')[-1])
    else:
        counter += 1
        if((counter - 1) % 40 >= total - 1 and (counter - 1) % 40 <= total + 1):
            part_2.append('#')
        else:
            part_2.append('.')
        if(counter % 40 == 0):
            print(part_2)
            part_2.clear()
    if(counter == 240):
        break