input = []
f = open("./input.txt", "r")
txt = f.read()
input = txt.splitlines()

part1_sum = 0
part1 = ''
for a in input:
    length = len(a)
    temp = 0
    for b in a:
        length -=1
        if b == '-':
            b = -1
        elif b == '=':
            b = -2
        temp += int(b)*pow(5,length)
    part1_sum += temp

lastStep = -1
while part1_sum != 0:
    step = 0
    while True:
        temp = round(part1_sum / pow(5,step))
        if -2 <= temp <= 2:
            if temp == -1:
                new_part1 = '-'
            elif temp == -2:
                new_part1 = '='
            else:
                new_part1 = str(round(part1_sum / pow(5,step)))
            if lastStep - 1 != step and lastStep != -1:
                for x in range(step+1, lastStep):
                    part1+='0'
            part1+=new_part1        
            part1_sum -= pow(5,step) * temp
            lastStep = step
            if step == 1 and part1_sum == 0:
                part1 += '0'
            break
        else:
            step+=1
print('Part 1:', part1)