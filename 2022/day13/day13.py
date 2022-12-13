from ast import literal_eval

input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

def compare_string(left, right):
    if type(left) is int and type(right) is int:
        if left < right:
            return -1
        elif left == right:
            return 0
        else:
            return 1
    elif type(left) is int and type(right) is list:
        left = [left]
    elif type(left) is list and type(right) is int:
        right = [right]
    
    len_left = len(left)
    len_right = len(right)
    
    for lefts, rights in zip(left,right):
        result = compare_string(lefts,rights)
        if result != 0:
            return result
    if len_left < len_right:
        return -1
    elif len_left == len_right:
        return 0
    else:
        return 1

x=0
part_1 = 0
part_2 = []
while x < len(input):
    left = literal_eval(input[x])
    right = literal_eval(input[x+1])
    part_2.append(left)
    part_2.append(right)
    result = compare_string(left, right)
    x+=3
    if result == -1:
        part_1 += int(x/3)

print(part_1)

two, six = [[2]], [[6]]
part_2.append(two)
part_2.append(six)
two_index = 0
six_index = 0
for a in part_2:
    if compare_string(a, two) <= 0:
        two_index += 1
    if compare_string(a, six) <= 0:
        six_index += 1
print(two_index, six_index, two_index * six_index)