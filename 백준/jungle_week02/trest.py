import sys
word = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()

check = []

for index,i in enumerate(word) :
    if i in bomb :
        number = bomb.find(i)
        check.append((number, index))

stack = []
result = []
bomb_len = len(bomb)
for i in range(len(check)):

    if check[i][0] == 0 :
            stack.append(check[i])

    elif stack[-1][0] == check[i][0] -1 :
            stack.append(check[i])
            if stack[-1][0] == len(bomb):                
                for j in range(len(bomb)):
                    index = stack.pop()[1]

                    result.append(index)


print(result)     