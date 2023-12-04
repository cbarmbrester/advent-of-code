import math

input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

total = 0
total_2 = 0
copies = {}
for x in range(len(input)):
    copies[x+1] = {'Amount': 1}

for line in input:
    count = 0
    game = line.split(': ')[0].split(' ')
    game = [int(x) for x in game if x!= '' and x != 'Card' ]
    winning, card = line.split(': ')[1].split(' | ')
    winning = winning.split(' ')
    card = card.split(' ')
    card = [x for x in card if x != '']
    for x in winning:
        if x in card:
            count +=1
    if count:
        total += math.pow(2,count-1)
    total_2 += copies[game[0]]['Amount']
    for a in range(count):
        copies[game[0]+a+1]['Amount'] += copies[game[0]]['Amount']

print('Part 1: ', total)
print('Part 2: ', total_2)