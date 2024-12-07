input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

total_1 = 0
total_2 = 0

def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

for a in input:
    bPart1 = False
    a = a.replace(':', '')
    line = [int(x) for x in a.split(' ')]
    for x in range(pow(2,len(line)-2)):
        result = 0
        operator = bin(x)[2:].zfill(len(line)-2)[::-1]
        for y in range(1,len(line)):
            if y == 1:
                result += line[1]
                continue
            if operator[y-2] == '0':
                result += line[y]
            elif operator[y-2] == '1':
                result *= line[y]
        if result == line[0]:
            total_1 += line[0]
            total_2 += line[0]
            bPart1 = True
            break
    if not bPart1:
        for x in range(pow(3,len(line)-2)):
            result = 0
            operator = ternary(x).zfill(len(line)-2)[::-1]
            for y in range(1,len(line)):
                if y == 1:
                    result += line[1]
                    continue
                if operator.find('2') == -1:
                    break
                if operator[y-2] == '0':
                    result += line[y]
                elif operator[y-2] == '1':
                    result *= line[y]
                elif operator[y-2] == '2':
                    result = int(str(result) + str(line[y]))
                if result > line[0]:
                    break

            if result == line[0]:
                total_2 += line[0]
                bPart1 = True
                break

print('Part 1: ', total_1)
print('Part 2: ', total_2)