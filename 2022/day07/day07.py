# def getSize(directory, input):
#     for i in range(len(input)):
#         a = input[i]
#         if(a.find('cd ' + directory) >= 0):
#             size = 0
#             listing = False
#             i+=1
#             nextLine = input[i]
#             if(nextLine == '$ ls'):
#                 listing = True
#             while(listing):
#                 i+=1
#                 if(i >= len(input)):
#                     break
#                 nextLine = input[i]
#                 if(nextLine[0] == '$'):
#                     listing = False
#                     break
#                 elif(nextLine.find('dir') >= 0):
#                     directory_name = nextLine.split(' ')
#                     size += getSize(directory_name[1], input)
#                 else:
#                     currentLine = nextLine.split(' ')
#                     size += int(currentLine[0])
#             files.append([directory,size])
#             return(size)

input = []
f = open("./input.txt", "r")
txt = f.read()
input = list(txt.splitlines())

files = {}
directory_path = []

for a in input:
    if(a.startswith('$')):
        listing = False        
        if(a.find('cd') >= 0):
            directory = a.split(' ')[-1]
            if directory == '/':
                directory_path = ['']
            elif directory == '..':
                directory_path.pop()
            else:
                directory_path.append(directory)
        elif(a.find('ls') >= 0):
            listing = True
    elif listing:
            key = '/'.join(directory_path)    
            if(key not in files):
                files[key] = {'size': 0, 'file': []}
            if a.startswith('dir'):
                files[key]['file'].append(a.split(' ')[1])
            else:
                files[key]['size'] += int((a.split(' '))[0])
                
def getSize(key):
    total = sum([getSize(key + '/' + a) for a in files[key]['file']])
    return files[key]['size'] + total

part_1 = 0

files_2 = {}

for key in files:
    size = getSize(key)
    files_2[key] = {'size': size}
    if size <= 100000:
        part_1 += size

print('Part 1: ' + str(part_1))

dif = files_2['']['size'] - 40000000
print(dif)

part_2_key = ''
part_2_best = dif
for key in files_2:
    temp = files_2[key]['size'] - dif
    if temp > 0 and temp < part_2_best:
        part_2_key = key
        part_2_best = temp
        
print('Part 2: ' + str(files_2[part_2_key]['size']))