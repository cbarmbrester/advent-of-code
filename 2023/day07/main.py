import math

input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break
    return array

hand = []
part_1 = 0

for line in input:
    cardCount = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}
    temp = line.split(' ')
    cards = []
    for a in temp[0]:
        if a.isnumeric():
            cards.append(int(a))
        else:
            a = a.replace('T', '10').replace('J','11').replace('Q','12').replace('K', '13').replace('A','14')
            cards.append(int(a))
        cardCount[int(a)] += 1
    if [x for x in cardCount if cardCount[x] > 4]:
        # print(cards, ' Five of a Kind')
        type = 7
    elif [x for x in cardCount if cardCount[x] > 3]:
        # print(cards, ' Four of a Kind')    
        type = 6
    elif [x for x in cardCount if cardCount[x] > 2]:
        if len([x for x in cardCount if cardCount[x] > 1]) > 1:
            # print(cards, ' Full House')
            type = 5
        else:
            # print(cards, ' Three of a Kind')
            type = 4
    elif [x for x in cardCount if cardCount[x] > 1]:
        if len([x for x in cardCount if cardCount[x] > 1]) > 1:
            # print(cards, ' Two Pair')
            type = 3
        else:
            # print(cards, ' One Pair')
            type = 2
    else:
        # print(cards, 'High Card')
        type = 1
    
    hand.append([cards, int(temp[1]), type])

stack = hand.copy()
rank = len(input)

for a in range(7,0,-1):
    temp = [stack[x] for x in range(len(stack)) if stack[x][2] == a]
    sort = bubble_sort(temp)
    for b in sort:
        part_1 += rank * b[1]
        rank -= 1
    for b in reversed(temp):
        stack.pop(stack.index(b))

print('Part 1: ', part_1)

hand = []
part_2 = 0

for line in input:
    cardCount = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 12: 0, 13: 0, 14: 0}
    temp = line.split(' ')
    cards = []
    joker = 0
    for a in temp[0]:
        if a.isnumeric():
            cards.append(int(a))
        else:
            a = a.replace('T', '10').replace('J','1').replace('Q','12').replace('K', '13').replace('A','14')
            cards.append(int(a))
        if int(a) != 1:
            cardCount[int(a)] += 1
        else:
            joker += 1
    if joker:
        cardCount[next(iter(dict(reversed(sorted(cardCount.items(), key=lambda item: item[1])))))] += joker
    if [x for x in cardCount if cardCount[x] > 4]:
        # print(cards, ' Five of a Kind')
        type = 7
    elif [x for x in cardCount if cardCount[x] > 3]:
        # print(cards, ' Four of a Kind')    
        type = 6
    elif [x for x in cardCount if cardCount[x] > 2]:
        if len([x for x in cardCount if cardCount[x] > 1]) > 1:
            # print(cards, ' Full House')
            type = 5
        else:
            # print(cards, ' Three of a Kind')
            type = 4
    elif [x for x in cardCount if cardCount[x] > 1]:
        if len([x for x in cardCount if cardCount[x] > 1]) > 1:
            # print(cards, ' Two Pair')
            type = 3
        else:
            # print(cards, ' One Pair')
            type = 2
    else:
        # print(cards, 'High Card')
        type = 1
    
    hand.append([cards, int(temp[1]), type])

stack = hand.copy()
rank = len(input)

for a in range(7,0,-1):
    temp = [stack[x] for x in range(len(stack)) if stack[x][2] == a]
    sort = bubble_sort(temp)
    for b in sort:
        part_2 += rank * b[1]
        rank -= 1
    for b in reversed(temp):
        stack.pop(stack.index(b))

print('Part 2: ', part_2)