from collections import deque

input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

d={'x': 0, 'm': 1, 'a': 2, 's': 3}
def test(point, flows):
    for i, x in enumerate(flows):
        if i == len(flows)-1:
            return(x)
        temp = x.split(':')
        if x[1] == '>':
            if point[d[x[0]]] > int(temp[0][2:]):
                return temp[1]
        else:
            if point[d[x[0]]] < int(temp[0][2:]):
                return temp[1]

flows = {}
part_1 = 0
for a in input:
    if len(a) == 0:
        continue
    elif a[0] != '{':
        name, temp = a.split('{')
        temp = temp[:-1].split(',')
        flows[name] = {'step': temp}
    else:
        point = []
        temp = a.split(',')
        for b in temp:
            point.append(int(b.split('=')[1].replace('}','')))
        flow = 'in'
        while flow not in ('A', 'R'):
            flow = test(point, flows[flow]['step'])
        if flow == 'A':
            part_1 += sum(point)
print('Part 1: ', part_1)

def new_range(operator, number, low, high):
    if operator == '>':
        low = max(low, number + 1)
    elif operator == '<':
        high = min(high, number - 1)
    elif operator == '>=':
        low = max(low, number)
    elif operator == '<=':
        high = min(high, number)
    return(low, high)

def new_ranges(pName, operator, number, x1, x2, m1, m2, a1, a2, s1, s2):
    if pName == 'x':
        x1, x2 = new_range(operator, number, x1, x2)
    elif pName == 'm':
        m1, m2 = new_range(operator, number, m1, m2)
    elif pName == 'a':
        a1, a2 = new_range(operator, number, a1, a2)
    elif pName == 's':
        s1, s2 = new_range(operator, number, s1, s2)        
    return (x1, x2, m1, m2, a1, a2, s1, s2)

part_2 = 0
queue = deque([('in', 1, 4000, 1, 4000, 1, 4000, 1, 4000)])
while queue:
    name, x1, x2, m1, m2, a1, a2, s1, s2 = queue.pop()
    if x1 > x2 or m1 > m2 or a1 > a2 or s1 > s2:
        continue
    if name == 'A':
        part_2 += (x2 - x1 + 1) * (m2 - m1 + 1) * (a2 - a1 + 1) * (s2 - s1 + 1)
        continue
    elif name == 'R':
        continue
    else:
        for i, step in enumerate(flows[name]['step']):
            if i == len(flows[name]['step']) - 1:
                queue.append((step, x1, x2, m1, m2, a1, a2, s1, s2))
                break
            else:
                temp = step.split(':')
                queue.append((temp[1], *new_ranges(temp[0][0], temp[0][1], int(temp[0][2:]), x1, x2, m1, m2, a1, a2, s1, s2)))
                if temp[0][1] == '>':
                    x1, x2, m1, m2, a1, a2, s1, s2 = new_ranges(temp[0][0], '<=', int(temp[0][2:]), x1, x2, m1, m2, a1, a2, s1, s2)
                else:
                    x1, x2, m1, m2, a1, a2, s1, s2 = new_ranges(temp[0][0], '>=', int(temp[0][2:]), x1, x2, m1, m2, a1, a2, s1, s2)

print('Part 2: ', part_2)