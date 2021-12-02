# https://www.acmicpc.net/problem/2156
""" 
예제 입력 1
6
6
10
13
9
8
1
예제 출력 1
33
 """
N = int(input())
glass = [0]
for i in range(N):
    glass.append(int(input().rstrip()))

dp = [0]*(N+1)

if N == 1:
    print(glass[1])
else:
    dp[1] = glass[1]
    dp[2] = glass[1]+glass[2]
    for n in range(3, N+1):
        dp[n] = max(dp[n-2]+glass[n], dp[n-3]+glass[n]+glass[n-1], dp[n-1])
    print(dp[N])
