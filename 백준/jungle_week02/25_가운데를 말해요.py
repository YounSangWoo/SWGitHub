# https://www.acmicpc.net/problem/1655
""" import heapq
import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
heapleft = []
heapright = []
ans = []
for i in range(1, N+1):
    if i % 2:  # 홀수
        A = int(input())
        heapq.heappush(heapright, [-A, A])
        ans.append(heapright[0][1])
    else:  # 짝수
        A = int(input())
        heapq.heappush(heapleft, A)
        ans.append((heapright[0][1]))

for i in range(N):
    print(ans[i])
 """

import sys
import heapq
input = sys.stdin.readline


N = int(input())
max_h, min_h = [], []

# max_h[0][1]값을 기준으로 큰 값은 min_h, 같거나 작은 값은 max_h에 삽입

for _ in range(N):
    A = int(input())

    if len(max_h) == len(min_h):
        heapq.heappush(max_h, (-A, A))

    else:
        heapq.heappush(min_h, (A, A))
    
    if len(max_h) >= 1 and len(min_h) >= 1 and max_h[0][1] > min_h[0][1]:
        max_value = heapq.heappop(max_h)[1]
        min_value = heapq.heappop(min_h)[1]
        heapq.heappush(max_h, (-min_value, min_value))
        heapq.heappush(min_h, (max_value, max_value))
    print(max_h[0][1])
