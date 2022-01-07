def solution(money):
    answer = 0
    N = len(money)
    dp1 = [0]*N  # 첫번째 집을 털었을경우
    dp2 = [0]*N # 두번째 집부터 털었을 경우

    dp1[0] = money[0]
    dp2[0] = 0
    for i in range(1,N-1):
        dp1[i] = max(dp1[i-1],dp1[i-2]+money[i]) #전집과 전전집을 털고 현재 집의 돈을 더한 값중 큰값이 현재 dp
    for i in range(1,N):    
        dp2[i] = max(dp2[i-1],dp2[i-2]+money[i])
    
    answer = max(dp1[N-2],dp2[N-1])

    return answer

print(solution([1,2,3,1]))