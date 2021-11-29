# https://www.acmicpc.net/problem/10000 17번 원영역 플래티넘..

import sys
input = sys.stdin.readline

N = int(input())
circle = [list(map(int, input().split()))for _ in range(N)]

LR = []

for i in range(N):
    LR.append([0, (circle[i][0]-circle[i][1])])
    LR.append([1, (circle[i][0]+circle[i][1])])


LR.sort(reverse=True)
LR.sort(key=lambda x: x[1])
print(LR)

circle_stack = []
space_count = 1

for i in range(len(LR)):
    if LR[i][0] == 0:
        circle_stack.append(LR[i])

    else:
        j= len(circle_stack)-1
        remove_cnt=1

        while j>=0:
            if circle_stack[j][0]==0:
                Rad = abs(LR[i][1]-circle_stack[j][1])
                save_me = circle_stack[j][1]
                total_radius = 0
                
                for _ in range(remove_cnt):
                    total_radius += circle_stack.pop()[1]
                
                circle_stack.append([3,Rad])
                if (total_radius-save_me)== Rad:
                    space_count+=2
                else:
                    space_count+=1
                break

            else:
                remove_cnt=1
                j=-1

print(space_count)


""" 
import sys
from bisect import bisect_left
input = sys.stdin.readline

n= int(input())
L = []
for i in range(n):
    x,r = map(int,input().split())
    L.append([x-r,x+r])
print(L)
L.sort(key = lambda x : (x[0],-x[1]))

print(L)
count = 0


def check(big, small):
    global count
    if big[1] == small[1]:
        count = count + 1
        return
    nextidx = bisect_left(L, [small[1], -1000000000])
    if nextidx == len(L):
        print
        return
    if small[1] == L[nextidx][0]:
        check(big, L[nextidx])


for i in range(n-1):
    if L[i][0] == L[i+1][0]:
        check(L[i], L[i+1])
print(1 + n + count)
 """