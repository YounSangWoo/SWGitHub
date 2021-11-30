T = int(input().rstrip())
for i in range(T):
    N = int(input().rstrip())
    dp = [0, 1, 1]
    for i in range(3, N+1):
        dp.append(dp[i-2]+dp[i-3])
    print(dp[N])
