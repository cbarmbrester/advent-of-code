def numeric(equation):
    if '+' in equation:
        y = equation.split('+')
        x = int(y[0])+int(y[1])
    elif '*' in equation:
        y = equation.split('*')
        x = int(y[0])*int(y[1])
    return x

input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())
   
monkeys = {}

for x in range(len(input)):
    if(input[x].find('Monkey') >= 0):
        monkeyNum = int(input[x].split(' ')[-1].strip(':'))
        items = input[x+1].split(': ')[-1].split(', ')
        #items = [int(item) for item in str_items]
        operation = input[x+2].split('= ')[-1]
        test = int(input[x+3].split('by ')[-1])
        true = input[x+4].split('monkey ')[-1]
        false = input[x+5].split('monkey ')[-1]
        monkeys[monkeyNum] = {'items': items, 'operation': operation, 'test': test, 'true': true, 'false': false, 'inspections': 0}
        x += 6

rounds = 10000
lcm = 1
for x in range(len(monkeys)):
    lcm *= monkeys[x]['test']

for curRound in range(rounds):
    for x in range(len(monkeys)):
        for a in range(len(monkeys)):
            while(len(monkeys[x]['items'])):
                inspect = monkeys[x]['items'].pop(0)
                monkeys[x]['inspections'] += 1
                operation = monkeys[x]['operation'].replace('old',str(inspect))
                worry = numeric(operation)
                #worry = int(worry / 3)
                worry %= lcm
                if(worry % monkeys[x]['test'] == 0):
                    monkeys[int(monkeys[x]['true'])]['items'].append(worry)
                else:
                    monkeys[int(monkeys[x]['false'])]['items'].append(worry)


solution = [0,0]
for a in range(len(monkeys)):
    print(a, ': ', monkeys[a]['inspections'])
    if(monkeys[a]['inspections'] > min(solution)):
        solution.remove(min(solution))
        solution.append(monkeys[a]['inspections'])
print(solution[0] * solution[1])