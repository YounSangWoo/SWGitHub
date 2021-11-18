# https://www.acmicpc.net/problem/2164 카드2
from collections import deque
import sys
input = sys.stdin.readline

N= int(input())
card = deque()

for i in range(1,N+1):
    card.append(i)

j=len(card)-1
while j>0:
    card.popleft()
    tmp=card.popleft()
    card.append(tmp)
    j-=1

print(card[0])