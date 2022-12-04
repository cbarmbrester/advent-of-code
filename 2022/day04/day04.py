input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

count_1 = 0
count_2 = 0
correct = []
incorrect = []
for a in input:
    pair = a.split(',')
    left_pair = pair[0].split('-')
    right_pair = pair[1].split('-')
    if((int(left_pair[0]) <= int(right_pair[0]) and int(left_pair[1]) >= int(right_pair[1])) or (int(right_pair[0]) <= int(left_pair[0]) and int(right_pair[1]) >= int(left_pair[1]))):
        count_1+=1
    if((int(left_pair[0]) >= int(right_pair[0]) and int(left_pair[0]) <= int(right_pair[1])) or (int(left_pair[1]) >= int(right_pair[0]) and int(left_pair[0]) <= int(right_pair[1])) or (int(right_pair[0]) >= int(left_pair[0]) and int(right_pair[0]) <= int(left_pair[1])) or (int(right_pair[1]) >= int(left_pair[0]) and int(right_pair[1]) <= int(left_pair[1]))):
        count_2 +=1
print(count_1)
print(count_2)