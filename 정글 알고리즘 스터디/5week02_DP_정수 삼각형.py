from collections import defaultdict
def solution(triangle):
    answer = 0
    N = len(triangle)
    dp = defaultdict(list)
    dp[0] = triangle[0]

    for i in range(1, N):
        k = -1
        for j in dp[i-1]:
            
            k +=1
            a = triangle[i][k]+j
            b = triangle[i][k+1]+j
            if dp[i]:
                if dp[i][k]<=a:
                    dp[i][k] = a        
                dp[i].append(b)
            else :
                dp[i].append(a)
                dp[i].append(b)
    answer = max(dp[N-1])
    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

""" 정확성  테스트
테스트 1 〉	통과(0.02ms, 10.3MB)
테스트 2 〉	통과(0.02ms, 10.2MB)
테스트 3 〉	통과(0.08ms, 10.2MB)
테스트 4 〉	통과(0.27ms, 10.3MB)
테스트 5 〉	통과(1.75ms, 10.5MB)
테스트 6 〉	통과(0.52ms, 10.3MB)
테스트 7 〉	통과(2.03ms, 10.4MB)
테스트 8 〉	통과(0.35ms, 10.3MB)
테스트 9 〉	통과(0.02ms, 10.2MB)
테스트 10 〉	통과(0.23ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과(33.06ms, 17.9MB)
테스트 2 〉	통과(25.93ms, 16.2MB)
테스트 3 〉	통과(37.98ms, 19MB)
테스트 4 〉	통과(30.32ms, 18MB)
테스트 5 〉	통과(31.30ms, 17.5MB)
테스트 6 〉	통과(34.89ms, 19.2MB)
테스트 7 〉	통과(36.07ms, 18.6MB)
테스트 8 〉	통과(29.71ms, 17MB)
테스트 9 〉	통과(31.55ms, 17.6MB)
테스트 10 〉	통과(33.47ms, 18.6MB)
 """

# 진호 풀이

# def solution(triangle):
#     answer = 0
#     n = len(triangle)

#     dp = [[0] * i for i in range(1, n+1)]
#     dp[0][0] = triangle[0][0]

#     for j in range(1, n):
#         for k in range(j+1):
#             if k == 0:
#                 dp[j][k] = dp[j-1][k] + triangle[j][k]
#             elif k == j:
#                 dp[j][k] = dp[j-1][k-1] + triangle[j][k]
#             else:
#                 dp[j][k] = max(dp[j-1][k-1], dp[j-1][k]) + triangle[j][k]

#     answer = max(dp[n-1])
#     return answer
