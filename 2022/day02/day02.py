input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())
        
score_1 = 0
score_2 = 0
for a in input:
    game_round = a.split(' ')
    if game_round[0] == 'A' and game_round[1] == 'X':
        score_1 += 4
        score_2 += 3
    if game_round[0] == 'A' and game_round[1] == 'Y':
        score_1 += 8
        score_2 += 4
    if game_round[0] == 'A' and game_round[1] == 'Z':
        score_1 += 3
        score_2 += 8
    if game_round[0] == 'B' and game_round[1] == 'X':
        score_1 += 1
        score_2 += 1
    if game_round[0] == 'B' and game_round[1] == 'Y':
        score_1 += 5
        score_2 += 5
    if game_round[0] == 'B' and game_round[1] == 'Z':
        score_1 += 9
        score_2 += 9
    if game_round[0] == 'C' and game_round[1] == 'X':
        score_1 += 7
        score_2 += 2
    if game_round[0] == 'C' and game_round[1] == 'Y':
        score_1 += 2
        score_2 += 6
    if game_round[0] == 'C' and game_round[1] == 'Z':
        score_1 += 6
        score_2 += 7   
print('Scores:', score_1, score_2)