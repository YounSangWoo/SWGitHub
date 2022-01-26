def solution(land):
    answer = 0
    N = len(land)  # 행의 갯수
    dp = [[0]*4 for _ in range(N)]
    dp[0] = land[0]

    for k in range(1, N):
      for t in range(4):
        for i in range(4):
            if i != t:
                dp[k][t] = max(dp[k][t], dp[k-1][i]+land[k][t])
    answer = max(dp[-1])

    return answer
