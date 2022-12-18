input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

valves = {}
rates = {}
removeZeros = []

for a in input:
    a = a.split(' ')
    index = a[1]
    rate = int(a[4].strip('rate=;'))
    if rate:
        rates[index] = rate
    elif index != 'AA':
        removeZeros.append(index)
    paths = []
    if a[8] == 'valves':
        for i in range(9,len(a)):
            paths.append(a[i].strip(','))
    else:
        paths.append(a[9])
    valves[index] = {'rate': rate, 'paths': paths}

distances = {a: {b: 100 for b in valves} for a in valves}
 
for a in valves:
    distances[a][a] = 0
    for b in valves[a]['paths']:
        distances[a][b] = 1
 
for a in valves:
    for b in valves:
        for c in valves:
            distances[b][c] = min(distances[b][c], distances[b][a] + distances[a][c])

for a in removeZeros:
    distances.pop(a)
for a in distances:
    for b in removeZeros:
        distances[a].pop(b)

def find_paths(dist, rates, t):
    pressures = []
    paths = []
    stack = [(t, 0, ['AA'])]
    while stack:
        t, p, path = stack.pop()
        cur = path[-1]
        new = []
        for n, d in dist[cur].items():
            if d > t - 2 or n in path:
                continue
            tt = t - d - 1
            pp = p + rates[n] * tt
            s = tt, pp, path + [n]
            new.append(s)
        if new:
            stack.extend(new)
        else:
            pressures.append(p)
            paths.append(path[1:])
    return pressures, paths

pressures, paths = find_paths(distances, rates, 30)
x = list(zip(pressures, paths))
pressures, paths = zip(*sorted(x, reverse=True))
print('Part 1:', pressures[0], paths[0])

#Part 2
pressures, paths = find_paths(distances, rates, 26)
x = list(zip(pressures, paths))
pressures, paths = zip(*sorted(x, reverse=True))
i, j = 0, 1
while any(y in paths[j] for y in paths[i]):
    j += 1
ans = pressures[i] + pressures[j]
j_max = j  
for i in range(1, j_max):
    for j in range(i + 1, j_max + 1):
        if any(x in paths[j] for x in paths[i]):
            continue
        ans = max(ans, pressures[i] + pressures[j])
print('Part 2: ', ans)