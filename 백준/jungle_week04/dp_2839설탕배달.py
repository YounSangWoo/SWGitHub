# https://www.acmicpc.net/problem/2839

import sys
input = sys.stdin.readline

n = int(input())
c = [3,5]
dp = [0 for i in range(n + 1)]
dp[1],dp[2] = -1,-1
for i in range(3, n + 1):
    a = []
    for j in c:
        if j <= i and dp[i - j] != -1:
            a.append(dp[i - j])
    if not a:
        dp[i] = -1
    else:
        dp[i] = min(a) + 1
print(dp[n])
