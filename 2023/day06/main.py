import math

input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

time = []
dist = []
part_1 = 1
for x in input[0].split(' '):
    if x.isnumeric():
        time.append(int(x))
for x in input[1].split(' '):
    if x.isnumeric():
        dist.append(int(x))

# for a in time:
#     for x in range(a):
#         if (x * (a-x)) > dist[time.index(a)]:
#             print('Time: ', a, ' Solutions: ', (a - ((x-1) * 2) - 1))
#             part_1 *= (a - ((x-1) * 2) - 1)
#             break

for a in range(len(time)):
    temp = (-1 * time[a] + math.sqrt((time[a] * time[a]) - (4 * dist[a]))) / 2
    part_1 *= (time[a] - ((int(abs(temp)+1)-1) * 2) - 1)
    print('Time: ', time[a], ' Solutions: ', (time[a] - ((int(abs(temp)+1)-1) * 2) - 1))
print('Part 1: ', part_1)        

time_2 = [int(input[0].replace(' ','').split(':')[1])]
dist_2 = [int(input[1].replace(' ','').split(':')[1])]

# for a in time_2:
#     for x in range(a):
#         if (x * (a-x)) > dist_2[time_2.index(a)]:
#           print('Part 2: ', (a - ((x-1) * 2) - 1))
#           break
      
for a in range(len(time_2)):
    temp = (-1 * time_2[a] + math.sqrt((time_2[a] * time_2[a]) - (4 * dist_2[a]))) / 2
    print('Time: ', time_2[a], ' Solutions: ', (time_2[a] - ((int(abs(temp)+1)-1) * 2) - 1))