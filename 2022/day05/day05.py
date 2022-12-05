input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

numStacks = int((len(input[0]) + 1) / 4)
stacks = []
stacks_2 = []
for x in range (numStacks):
    stacks.append([])
    stacks_2.append([])
parse_moves = False
for a in input:
    if(len(a) == 0):
        parse_moves = True
        #print(stacks)
        continue
    if(parse_moves == False):
        block_found = True
        index = 0
        while(block_found):
            found_index = a.find('[',index)
            if(found_index == -1):
                block_found = False
                continue
            curStack = int((found_index / 4))
            stacks[curStack].append(a[found_index+1])
            stacks_2[curStack].append(a[found_index+1])
            index = found_index + 1
    else:
        moves = a.split(' ')
        #print(moves)
        for x in range(int(moves[1])):
            stacks[int(moves[5]) - 1].insert(0,stacks[int(moves[3]) - 1].pop(0))
            stacks_2[int(moves[5]) - 1].insert(x,stacks_2[int(moves[3]) - 1].pop(0))
        #print(stacks)
for a in range(numStacks):
    print(stacks[a][0], end="")
print()
for a in range(numStacks):
    print(stacks_2[a][0], end="")