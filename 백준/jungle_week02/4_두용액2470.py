# https://www.acmicpc.net/problem/2470 두 용액

import sys
input = sys.stdin.readline


N = int(input())
liquid = list(map(int, (input().split()[:N])))
liquid.sort()

pl = 0 
pr = N-1

ans =liquid[pl] + liquid[pr] 
min = abs(ans)+1

while pl<pr:
    ans = liquid[pl] + liquid[pr]
    if abs(ans)<min:
        min = abs(ans)
        answer =[liquid[pl], liquid[pr]]

    elif ans == 0:
        answer = [liquid[pl], liquid[pr]]
        break
    
    elif ans<0:
        pl+=1
    else : 
        pr-=1

for i in answer:
    print(i, end=' ')


