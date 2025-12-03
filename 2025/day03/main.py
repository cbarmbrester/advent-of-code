input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

def battery(loops, input):
    total = 0
    for a in input:
        intArray = [int(x) for x in a]
        maxString = ''
        max_index = -1
        for x in range(loops-1, -1, -1):
            max_index += 1
            if len(intArray[max_index:-x]) == 0:
                maxString += str(max(intArray[max_index:]))
            else:
                maxValue = max(intArray[max_index:-x])
                max_index += intArray[max_index:-x].index(maxValue)
                maxString += str(maxValue)
        total += int(maxString)
    return total

print('Part 1: ', battery(2, input))
print('Part 2: ', battery(12, input))