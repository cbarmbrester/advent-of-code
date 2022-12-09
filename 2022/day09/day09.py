input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())
# solution = set(['0,0'])
# head = [0,0]
# tail = [0,0]

# for a in input:
#     move = a.split(' ')
#     #print(move)
#     if(move[0] == 'U'):
#         for x in range(int(move[1])):
#             head[1] += 1
#             if(abs(head[0] - tail[0]) > 1  or abs(head[1] - tail[1]) > 1):
#                 tail[1] = head[1] - 1
#                 tail[0] = head[0]
#                 solution.add(str(tail[0]) + ',' + str(tail[1]))
#             #print(head, tail)
#     if(move[0] == 'D'):
#         for x in range(int(move[1])):
#             head[1] -= 1
#             if(abs(head[0] - tail[0]) > 1  or abs(head[1] - tail[1]) > 1):
#                 tail[1] = head[1] + 1
#                 tail[0] = head[0]
#                 solution.add(str(tail[0]) + ',' + str(tail[1]))
#             #print(head, tail)
#     if(move[0] == 'L'):
#         for x in range(int(move[1])):
#             head[0] -= 1
#             if(abs(head[0] - tail[0]) > 1  or abs(head[1] - tail[1]) > 1):
#                 tail[0] = head[0] + 1
#                 tail[1] = head[1]
#                 solution.add(str(tail[0]) + ',' + str(tail[1]))
#             #print(head, tail)
#     if(move[0] == 'R'):
#         for x in range(int(move[1])):
#             head[0] += 1
#             if(abs(head[0] - tail[0]) > 1  or abs(head[1] - tail[1]) > 1):
#                 tail[0] = head[0] - 1
#                 tail[1] = head[1]
#                 solution.add(str(tail[0]) + ',' + str(tail[1]))
#             #print(head, tail)
# #print(len(solution))

# solution.clear()
solution = set(['0,0'])
solution_2 = set(['0,0'])
part_2 =[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

def innerMove(part_2):
    for i in range(1, len(part_2)):
        x, y = part_2[i-1]
        dx, dy = part_2[i]
        if abs(x-dx) > 1 or abs(y-dy) > 1:
            if x > dx:
                dx += 1
            elif x < dx:
                dx -= 1
            if y > dy:
                dy += 1
            elif y < dy:
                dy -= 1
            part_2[i] = (dx, dy)
            
for a in input:
    move = a.split(' ')
    #print(move)
    if(move[0] == 'U'):
        for x in range(int(move[1])):
            part_2[0][1] += 1
            innerMove(part_2)
            solution.add(str(part_2[1][0]) + ',' + str(part_2[1][1]))
            solution_2.add(str(part_2[-1][0]) + ',' + str(part_2[-1][1]))
    if(move[0] == 'D'):
        for x in range(int(move[1])):
            part_2[0][1] -= 1
            innerMove(part_2)
            solution.add(str(part_2[1][0]) + ',' + str(part_2[1][1]))
            solution_2.add(str(part_2[-1][0]) + ',' + str(part_2[-1][1]))
    if(move[0] == 'L'):
        for x in range(int(move[1])):
            part_2[0][0] -= 1
            innerMove(part_2)
            solution.add(str(part_2[1][0]) + ',' + str(part_2[1][1]))
            solution_2.add(str(part_2[-1][0]) + ',' + str(part_2[-1][1]))
    if(move[0] == 'R'):
        for x in range(int(move[1])):
            part_2[0][0] += 1
            innerMove(part_2)
            solution.add(str(part_2[1][0]) + ',' + str(part_2[1][1]))
            solution_2.add(str(part_2[-1][0]) + ',' + str(part_2[-1][1]))
print(len(solution), len(solution_2))