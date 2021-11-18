# https://www.acmicpc.net/problem/11053 가장 긴 증가하는 부분수열 LIS

import sys
input = sys.stdin.readline


N = int(input())
num = list(map(int, (input().split()[:N])))

dp = [0 for i in range(N)]

for i in range (N):
    for j in range(i):
        if num[i]>num[j] and dp[i] < dp[j]: 
            #입력받은값이 증가하고 
           dp[i] = dp[j]
    dp[i] += 1 #초기 값은 1이 들어감

print(max(dp))


