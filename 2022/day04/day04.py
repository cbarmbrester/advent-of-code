input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

count_1 = 0
count_2 = 0

for a in input:
    pair = a.split(',')
    left_pair = [int(x) for x in pair[0].split('-')]
    right_pair = [int(x) for x in pair[1].split('-')]
    if((left_pair[0] <= right_pair[0] and left_pair[1] >= right_pair[1]) or (right_pair[0] <= left_pair[0] and right_pair[1] >= left_pair[1])):
        count_1+=1
    if((left_pair[0] >= right_pair[0] and left_pair[0] <= right_pair[1]) or (left_pair[1] >= right_pair[0] and left_pair[0] <= right_pair[1]) or (right_pair[0] >= left_pair[0] and right_pair[0] <= left_pair[1]) or (right_pair[1] >= left_pair[0] and right_pair[1] <= left_pair[1])):
        count_2 +=1
print(count_1)
print(count_2)
