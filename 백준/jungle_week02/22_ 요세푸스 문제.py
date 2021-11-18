# https://www.acmicpc.net/problem/11866

from collections import deque
import sys
input = sys.stdin.readline

N,k=map(int,input().strip().split())
card= deque()
for i in range(1,N+1):
    card.append(i)
#카드 1,2,3,4,5,6,7
final = []

while len(card)>0:
    n=1
    while n<k:
        card.append(card.popleft())
        n+=1
    final.append(card.popleft())

print(f"<{', '.join(map(str,final))}>")    
