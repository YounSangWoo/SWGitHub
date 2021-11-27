# https://www.acmicpc.net/problem/12865

""" 
예제 입력 1 
4 7
6 13
4 8
3 6
5 12
예제 출력 1 
14
"""

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

warray =[[0,0]]
for i in range(N):
    warray.append(list(map(int,input().split())))

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = warray[i][0]        
        value = warray[i][1]

        if j < weight:
            dp[i][j] = dp[i-1][j]
        else :
            dp[i][j] = max(value+dp[i-1][j-weight], dp[i-1][j])

print(dp[N][K])


