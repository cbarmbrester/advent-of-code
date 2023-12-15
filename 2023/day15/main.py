input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.split(','))

def hash_string(text):
    value = 0
    for b in text:
        value = ((value + ord(b)) * 17) % 256
    return value

part_1 = 0
for a in input:
    part_1+= hash_string(a)
print('Part 1: ', part_1)

box = {}
for a in range(256):
    box[a] = {'label': [], 'lens': []}
for a in input:
    index = max(a.find('-'), a.find('='))
    boxNum = hash_string(a[0:index])
    if a[index] == '=':
        if a[0:index] in box[boxNum]['label']:
            box[boxNum]['lens'][box[boxNum]['label'].index(a[0:index])] = int(a[index+1:])
        else:
            box[boxNum]['label'].append(a[0:index])
            box[boxNum]['lens'].append(int(a[index+1:]))
    else:
        if a[0:index] in box[boxNum]['label']:
            box[boxNum]['lens'].pop(box[boxNum]['label'].index(a[0:index]))
            box[boxNum]['label'].remove(a[0:index])

part_2 = 0
for a in box:
    if box[a]['label'] == []:
        continue
    for order, b in enumerate(box[a]['lens']):
        part_2 += (a+1) * (order+1) * b
print('Part 2: ', part_2)        