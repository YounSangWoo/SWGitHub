# https://www.acmicpc.net/problem/9095

T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())
    dp = [0,1,2,4]
    for i in range(4,N+1):
        dp.append(dp[i-1]+dp[i-2]+dp[i-3])
    
    print(dp[N])


