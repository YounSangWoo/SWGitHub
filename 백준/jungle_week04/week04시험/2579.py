# https://www.acmicpc.net/problem/2579

N = int(input())

step = [0]
for i in range (N):
    a = int(input().rstrip())
    step.append(a)

dp = [0]*(N+1)

if N == 1:
    print(step[1])
else:
    dp[1] = step[1]
    dp[2] = step[1]+step[2]
    for n in range(3, N+1):
        dp[n] = max(dp[n-2]+step[n], dp[n-3]+step[n]+step[n-1])
    print(dp[N])

""" 

초기 dp 1 번째 계단을 올라가는동안 최대 획득 가능한 점수는 step[1]
dp2 계단을 올라가는 동안 최대 획등가능한 점수는 step[1]+step[2]

3번째 계단은 두단계 아래 계단까지 최대획득한 점수(dp[3-2])+마지막계단점수(step[3]) 또는
3단계 전 까지 획득한 점수 (dp[3-3]) + 마지막 전 계단점수(step[3-1]) + 마지막계단 점수 (step[3])
중 최댓값을 가지게 됩니다.

점화식
dp[n] = max(dp[n-2]+step[n], dp[n-3]+step[n]+step[n-1])

"""