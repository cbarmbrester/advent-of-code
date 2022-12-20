input = []
f = open("./input.txt", "r")
txt = f.read()
input = [int(x) for x in list(txt.splitlines())]

numValues = len(input)
decryption = 811589153
loops = 10
    
newInput = [x for x in range(numValues)]
for loops in range(loops):
    for i in range(numValues):
        move = input[i] * decryption
        if move == 0:
            continue
        curPos = newInput.index(i)
        newPos = (move + curPos) % (numValues - 1)
        newInput.insert(newPos,newInput.pop(curPos))
    
zeroIndex = newInput.index(input.index(0))

print('Answer: ', input[newInput[(zeroIndex + 1000) % numValues]] * decryption, input[newInput[(zeroIndex + 2000) % numValues]] * decryption, input[newInput[(zeroIndex + 3000) % numValues]] * decryption)
print('Answer: ', (input[newInput[(zeroIndex + 1000) % numValues]]+input[newInput[(zeroIndex + 2000) % numValues]]+input[newInput[(zeroIndex + 3000) % numValues]]) * decryption) 