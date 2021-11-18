# https://www.acmicpc.net/problem/2630

import sys
input = sys.stdin.readline

def list_sum(a:list):
    S=0
    for i in range(len(a)):
        S +=sum(a[i])
    return S

def divpaper(paper,end):
    paperA = []
    paperB = []
    paperC = []
    paperD = []
    S= list_sum(paper)

    if S==end**2:
        global Blue 
        Blue+=1
        return 
    elif S==0:
        global white
        white+=1
        return
    
    for i in range(end//2):
            paperA.append(paper[i][:end//2])  # 1사분면
            paperB.append(paper[i][end//2:])  # 2사분면
   
    for n in range(end//2,end):
            paperC.append(paper[n][:end//2])  # 3사분면
            paperD.append(paper[n][end//2:])  # 4사분면
    
    divpaper(paperA,len(paperA))
    divpaper(paperB,len(paperB))
    divpaper(paperC,len(paperC))
    divpaper(paperD,len(paperD))
    return

############### 입력
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]


white = 0
Blue = 0
divpaper(paper,len(paper))

print(white)
print(Blue)
