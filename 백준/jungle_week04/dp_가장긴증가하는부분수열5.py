# https://www.acmicpc.net/problem/14003
""" 
예제 입력 1
6
10 20 10 30 20 50
예제 출력 1
4
10 20 30 50
 """
# 시간초과

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
nums = list(map(int, (input().split()[:N])))

dp = [0]*N
for i in range(N):
    for j in range(i):
        if nums[i] > nums[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))

max_v = max(dp)
stack = deque()
for i in range(N-1, -1, -1):
    if dp[i] == max_v:
        stack.appendleft(nums[i])
        max_v -= 1

for i in range(len(stack)):
    print(stack[i], end=' ')
