def solution(n, money):
    answer = 0
    dp = [0]*(n+1)
    dp[0] = 1
    for i in money:
        for j in range(i, n+1):
            dp[j] += dp[j-i]

    answer = dp[n] % 1000000007

    return answer

# 동전이 주어졌을때 거스름돈 낼 수 있는 방법의 수 