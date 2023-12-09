input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

def pattern(his):
    temp = []
    for a in range(len(his)-1):
        temp.append(his[a+1]-his[a])
    return temp 

part_1 = 0
part_2 = 0

for line in input:
    done = False
    temp = [[int(x) for x in line.split(' ')]]
    while done == False:
        temp.append(pattern(temp[-1]))
        if len(set(temp[-1])) == 1:
            sol = temp.pop(-1)
            value = sol[-1]
            value_2 = sol[0]
            while temp:
                sol = temp.pop(-1)
                value += sol[-1]
                value_2 = sol[0] - value_2
            part_1 += value
            part_2 += value_2
            done = True

print('Part 1: ', part_1)
print('Part 2: ', part_2)