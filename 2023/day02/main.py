input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

bag = {'red': 12, 'green': 13, 'blue': 14}
total = 0
total_2 = 0

for line in input:
    valid = True
    min_bag = {'red': 0, 'green': 0, 'blue': 0}
    parse = line.split(': ')
    id = int(parse[0].replace('Game ',''))
    pulls = parse[1].split('; ')
    for pull in pulls:
        for cubes in pull.split(', '):
            cube = cubes.split(' ')
            if min_bag[cube[1]] < int(cube[0]):
                min_bag[cube[1]] = int(cube[0])
            if int(cube[0]) > bag[cube[1]]:
                valid = False
    if valid:
        total += id
    temp = 1
    for a in min_bag.values():
        temp = a * temp
    total_2 += temp
    
print('Part 1: ', total)
print('Part 2: ', total_2)
