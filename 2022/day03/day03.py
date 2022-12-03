input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

part_1 = 0
for a in input:
    length = int(len(a)/2)
    first_string = a[0:length]
    second_string = a[length:]
    value = ''.join(set.intersection(set(first_string), set(second_string)))
    if ord(value) > 96:
        int_value = ord(value) - 96
    else:
        int_value = ord(value) - 38
    part_1 += int_value
print("Part 1: ", part_1)

part_2 = 0
group = []
for a in input:
    group.append(a)
    if len(group) != 3:
        continue
    value = ''.join(set.intersection(set(group[0]), set(group[1]), set(group[2]))))
    if ord(value) > 96:
        int_value = ord(value) - 96
    else:
        int_value = ord(value) - 38
    part_2 += int_value
    group.clear()
print("Part 2: ", part_2)