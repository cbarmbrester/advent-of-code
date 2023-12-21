from collections import deque
from math import lcm

input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

sequence = {}
p2Source = ''
for a in input:
    temp = a.split(' -> ')
    name = temp[0]
    symbol = ''
    if temp[0] != 'broadcaster':
        symbol = temp[0][0]
        name = temp[0][1:]
    sequence[name] = {'output': temp[1].replace(' ', '').split(','), 'symbol': symbol, 'state': 0, 'last': {}}
    if 'rx' in sequence[name]['output']:
        p2Source = name

temp = [a for a in sequence if sequence[a]['symbol'] == '&']
p2 = {}
for a in sequence:
    for b in sequence[a]['output']:
        for c in temp:
            if b in c:
                sequence[c]['last'][a] = 0
        if p2Source == b:
            p2[a] = 0
    
loop = 1000
i = 0
low_count = 0
high_count = 0
part_2 = True
while part_2:
    low_count+=1
    prev = 'button'
    queue = deque([('broadcaster', 0, prev)])
    while queue:
        name, pulse, prev = queue.popleft()
        symbol = ''
        if name != 'broadcaster':
            symbol = name[0]
        if name not in sequence.keys():
            continue
        if sequence[name]['symbol'] == '%':
            if pulse == 0:
                sequence[name]['state'] = (sequence[name]['state'] + 1) % 2
                pulse = 1 if sequence[name]['state'] == 1 else 0
            else:
                continue
        elif sequence[name]['symbol'] == '&':
            sequence[name]['last'][prev] = pulse
            conjun = False
            for inner in sequence[name]['last']:
                if sequence[name]['last'][inner] == 0:
                    conjun = False
                    break
                else:
                    conjun = True
            pulse = 0 if conjun else 1
        for a in sequence[name]['output']:
            queue.append((a, pulse, name))
            if name in p2 and pulse == 1:
                p2[name] = i+1
        if pulse == 0:
            low_count += len(sequence[name]['output'])
        else:
            high_count += len(sequence[name]['output'])
    i+=1
    if i == 1000:
        print('Part 1: ', low_count, high_count, low_count * high_count)
    if 0 not in p2.values():
        part_2 = False
        print('Part 2: ', lcm(*p2.values()))