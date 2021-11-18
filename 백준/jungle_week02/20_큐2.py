# https://www.acmicpc.net/problem/18258\
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

Que = deque()

for _ in range(N):
    A = list(input().split())

    if A[0]=='push':
        Que.append(A[1])
    
    elif A[0]=='pop':
        try: print(Que.popleft())
        except: print(-1)


    elif A[0]=='front':
        try:print(Que[0])
        except: print(-1)
    
    elif A[0]=='back':
        try:print(Que[-1])
        except: print(-1)
    
    elif A[0]=='size':
        print(len(Que))
    
    elif A[0]=='empty':
        if len(Que)==0:
            print(1)
        else : print(0)
    

    