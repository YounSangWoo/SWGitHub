# https://www.acmicpc.net/problem/17608 막대기

#막대기의 개수 (2 ≤ N ≤ 100,000) N줄 각각에는 막대기의 높이를 나타내는 정수 h(1 ≤ h ≤ 100,000)가 주어진다

import sys
input = sys.stdin.readline

count = 1

N  = int(input())
sticks = list(int(input()) for _ in range(N))
pivot = sticks.pop()

H = len(sticks)

while H>0:
    a = sticks.pop()
    H-=1

    if a>pivot:
        count+=1
        pivot = a
    
print(count)
