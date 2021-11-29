# https://www.acmicpc.net/problem/6549 히스토그램
import sys
input = sys.stdin.readline

# print(n,numbers)

def countmax(N:list):
    maxcnt=0
    for i in range(1,len(N)):
        cnt = 0
        if i !=1 and N[i-1]<N[i]:
            for j in range(i, len(N)):
                if N[i]<=N[j] :
                        cnt +=N[i]
                else:
                    if i < j:
                        break
                    else:
                        cnt = 0
        else :
            for j in range(1, len(N)):
                if N[i]<=N[j] :
                        cnt +=N[i]
                else:
                    if i < j:
                        break
                    else:
                        cnt = 0
        maxcnt =max(maxcnt, cnt)
            
    return maxcnt

while True:
    
    N = list(map(int,(input().split())))
    if N[0] == 0:
        break

    else : print(countmax(N))