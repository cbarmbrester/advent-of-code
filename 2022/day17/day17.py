import numpy as np

input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())[0]
input = [x for x in input]
move_count = 0

limit = 1000000000000
board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
cycle = []
cycle_loop = False
rock = 0

while rock < limit:
    #line
    canMove = True
    if rock % 5 == 0:
        board.append([0,0,1,1,1,1,0])
        x1, y = 2, len(board)-1
        while canMove:
            if input[move_count] == '<':
                if x1 != 0:
                    if board[y][x1-1] != 1:
                        board[y][x1-1] = 1
                        board[y][x1+3] = 0
                        x1 = x1-1
            else:
                if x1+3 != len(board[0])-1:
                    if board[y][x1+4] != 1:
                        board[y][x1+4] = 1
                        board[y][x1] = 0
                        x1 = x1+1
            move_count+= 1
            if move_count == len(input):
                move_count = 0
            if y != 0:
                if board[y-1][x1] == 1 or board[y-1][x1+1] == 1 or board[y-1][x1+2] == 1 or board[y-1][x1+3] == 1:
                    canMove=False
                else:
                    board[y-1][x1] = 1 
                    board[y-1][x1+1] = 1 
                    board[y-1][x1+2] = 1
                    board[y-1][x1+3] = 1
                    board[y][x1] = 0
                    board[y][x1+1] = 0 
                    board[y][x1+2] = 0
                    board[y][x1+3] = 0
            else:
                canMove=False
            y -= 1
    #plus 
    elif rock % 5 == 1:
        board.append([0,0,0,1,0,0,0])
        board.append([0,0,1,1,1,0,0])
        board.append([0,0,0,1,0,0,0])
        x1, y = 3, len(board)-2
        while canMove:
            if input[move_count] == '<':
                if x1-1 != 0:
                    if board[y][x1-2] != 1 and board[y-1][x1-1] != 1 and board[y+1][x1-1] != 1:
                        board[y+1][x1-1] = 1
                        board[y][x1-2] = 1
                        board[y-1][x1-1] = 1
                        board[y+1][x1] = 0
                        board[y][x1+1] = 0
                        board[y-1][x1] = 0
                        x1 -= 1
            else:
                if x1+1 != len(board[0])-1:
                    if board[y][x1+2] != 1 and board[y-1][x1+1] != 1 and board[y+1][x1+1] != 1:
                        board[y+1][x1+1] = 1
                        board[y][x1+2] = 1
                        board[y-1][x1+1] = 1
                        board[y+1][x1] = 0
                        board[y][x1-1] = 0
                        board[y-1][x1] = 0
                        x1 += 1
            move_count+= 1
            if move_count == len(input):
                move_count = 0
            if y-1 != 0:
                if board[y-2][x1] == 1 or board[y-1][x1+1] == 1 or board[y-1][x1-1] == 1:
                    canMove=False
                else:
                    board[y-2][x1] = 1 
                    board[y-1][x1+1] = 1 
                    board[y-1][x1-1] = 1
                    board[y+1][x1] = 0
                    board[y][x1+1] = 0 
                    board[y][x1-1] = 0
            else:
                canMove=False
            y -= 1        
    #J
    elif rock % 5 == 2:
        board.append([0,0,1,1,1,0,0])
        board.append([0,0,0,0,1,0,0])
        board.append([0,0,0,0,1,0,0])
        x1, y = 4, len(board)-3
        while canMove:
            if input[move_count] == '<':
                if x1-2 != 0:
                    if board[y][x1-3] != 1 and board[y+1][x1-1] != 1 and board[y+2][x1-1] != 1:
                        board[y+2][x1-1] = 1
                        board[y+1][x1-1] = 1
                        board[y][x1-3] = 1
                        board[y+2][x1] = 0
                        board[y+1][x1] = 0
                        board[y][x1] = 0
                        x1 -= 1
            else:
                if x1 != len(board[0])-1:
                    if board[y][x1+1] != 1 and board[y+1][x1+1] != 1 and board[y+2][x1+1] != 1:
                        board[y+2][x1+1] = 1
                        board[y+1][x1+1] = 1
                        board[y][x1+1] = 1
                        board[y+2][x1] = 0
                        board[y+1][x1] = 0
                        board[y][x1-2] = 0
                        x1 += 1
            move_count+= 1
            if move_count == len(input):
                move_count = 0
            if y != 0:
                if board[y-1][x1-2] == 1 or board[y-1][x1-1] == 1 or board[y-1][x1] == 1:
                    canMove=False
                else:
                    board[y-1][x1-2] = 1 
                    board[y-1][x1-1] = 1 
                    board[y-1][x1] = 1
                    board[y][x1-2] = 0
                    board[y][x1-1] = 0 
                    board[y+2][x1] = 0
            else:
                canMove=False
            y -= 1
    #I
    elif rock % 5 == 3:
        board.append([0,0,1,0,0,0,0])
        board.append([0,0,1,0,0,0,0])
        board.append([0,0,1,0,0,0,0])
        board.append([0,0,1,0,0,0,0])
        x1, y = 2, len(board)-4
        while canMove:
            if input[move_count] == '<':
                if x1 != 0:
                    if board[y][x1-1] != 1 and board[y+1][x1-1] != 1 and board[y+2][x1-1] != 1 and board[y+3][x1-1] != 1:
                        board[y][x1-1] = 1
                        board[y+1][x1-1] = 1
                        board[y+2][x1-1] = 1
                        board[y+3][x1-1] = 1
                        board[y][x1] = 0
                        board[y+1][x1] = 0
                        board[y+2][x1] = 0
                        board[y+3][x1] = 0
                        x1 -= 1
            else:
                if x1 != len(board[0])-1:
                    if board[y][x1+1] != 1 and board[y+1][x1+1] != 1 and board[y+2][x1+1] != 1 and board[y+3][x1+1] != 1:
                        board[y][x1+1] = 1
                        board[y+1][x1+1] = 1
                        board[y+2][x1+1] = 1
                        board[y+3][x1+1] = 1
                        board[y][x1] = 0
                        board[y+1][x1] = 0
                        board[y+2][x1] = 0
                        board[y+3][x1] = 0
                        x1 += 1
            move_count+= 1
            if move_count == len(input):
                move_count = 0
            if y != 0:
                if board[y-1][x1] == 1:
                    canMove=False
                else:
                    board[y-1][x1] = 1 
                    board[y+3][x1] = 0
            else:
                canMove=False
            y -= 1
    #square
    elif rock % 5 == 4:
        board.append([0,0,1,1,0,0,0])
        board.append([0,0,1,1,0,0,0])
        x1, y = 3, len(board)-2
        while canMove:
            if input[move_count] == '<':
                if x1-1 != 0:
                    if board[y][x1-2] != 1 and board[y+1][x1-2] != 1:
                        board[y+1][x1-2] = 1
                        board[y][x1-2] = 1
                        board[y+1][x1] = 0
                        board[y][x1] = 0
                        x1 -= 1
            else:
                if x1 != len(board[0])-1:
                    if board[y][x1+1] != 1 and board[y+1][x1+1] != 1:
                        board[y+1][x1+1] = 1
                        board[y][x1+1] = 1
                        board[y+1][x1-1] = 0
                        board[y][x1-1] = 0
                        x1 += 1
            move_count+= 1
            if move_count == len(input):
                move_count = 0
            if y != 0:
                if board[y-1][x1] == 1 or board[y-1][x1-1] == 1:
                    canMove=False
                else:
                    board[y-1][x1-1] = 1 
                    board[y-1][x1] = 1
                    board[y+1][x1-1] = 0 
                    board[y+1][x1] = 0
            else:
                canMove=False
            y -= 1
            
    emptyCount = 0        
    for i in range(len(board)):
        if any(board[len(board)-1-i]):
            break
        else:
            emptyCount +=1
    if emptyCount > 3:
        for i in range(emptyCount - 3):
            board.pop(-1)
    elif emptyCount < 3:
        for i in range(emptyCount):
            board.append([0,0,0,0,0,0,0])
    
    rock += 1
    if rock == 2021:
        print('Part 1: ', len(board)-3)
        cycle = [rock % 5, move_count, len(board)-3, rock]
    if rock > 2021:
        if rock % 5 == cycle[0] and move_count == cycle[1] and not cycle_loop:
            dh = len(board)-3 - cycle[2]
            di = rock - cycle[3]
            future_cycles = int((limit - rock)/di)
            rock += di*future_cycles
            height_offset = dh*future_cycles
            cycle_loop = True
print('Part 2: ', len(board)-3 + height_offset)