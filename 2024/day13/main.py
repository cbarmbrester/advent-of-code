import re

input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

total_1 = 0
total_2 = 0

for a in range(int((len(input) + 1) / 4)):
    A = [int(x) for x in re.findall("\d+", input[(a*4)])]
    B = [int(x) for x in re.findall("\d+", input[(a*4)+1])]
    P = [int(x) for x in re.findall("\d+", input[(a*4)+2])]
    # print(A, B, P)
    
    #Cramer's Rule
    aPress = ((P[0] * B[1]) - (B[0] * P[1]))/((A[0]*B[1])-(B[0]*A[1]))
    bPress = ((P[1] * A[0]) - (A[1] * P[0]))/((A[0]*B[1])-(B[0]*A[1]))
    if str(aPress).split('.')[1] == '0' and str(bPress).split('.')[1] == '0':
        total_1 += 3*aPress + bPress
    
    P[0] += 10000000000000
    P[1] += 10000000000000
    
    aPress = ((P[0] * B[1]) - (B[0] * P[1]))/((A[0]*B[1])-(B[0]*A[1]))
    bPress = ((P[1] * A[0]) - (A[1] * P[0]))/((A[0]*B[1])-(B[0]*A[1]))
    if str(aPress).split('.')[1] == '0' and str(bPress).split('.')[1] == '0':
        total_2 += 3*aPress + bPress
    
print("Part 1: ", int(total_1))
print("Part 2: ", int(total_2))