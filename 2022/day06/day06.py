input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

for a in input:
    char_array = [char for char in a]
    solution = []
    part_1 = 0
    part_2 = 0
    for x in range(len(char_array)):
        solution.append(char_array[x])
        if(len(solution) == 4):
            if(len(set(solution)) == 4):
                part_1 = x + 1
            else:
                solution.pop(0)
        if(len(solution) == 14):
            if(len(set(solution)) == 14):
                part_2 = x + 1
                break
            else:
                solution.pop(0)                
print(part_1)
print(part_2)