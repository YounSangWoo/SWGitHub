def solution(m, n, puddles):
    answer = 0
    dp = [[0]*(m+1) for _ in range((n+1))]

    dp[1][1] = 1
    
    for k in range(1,n+1):
        for j in range(1,m+1):
            if [j,k] not in puddles :
                    dp[k][j] += (dp[k-1][j]+dp[k][j-1])
    
    answer = dp[n][m]%1000000007

    return answer


# print(solution(2, 2, []), 2)
# print(solution(3, 3, []), 6)
# print(solution(3, 3, [[2, 2]]), 2)
# print(solution(3, 3, [[2, 3]]), 3)
# print(solution(3, 3, [[1, 3]]), 5)
# print(solution(3, 3, [[1, 3], [3, 1]]), 4)
# print(solution(3, 3, [[1, 3], [3, 1], [2, 3]]), 2)
# print(solution(3, 3, [[1, 3], [3, 1], [2, 3], [2, 1]]), 1)
print(solution(7, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]), 0) # 이 값이 잘 나오면 테스트1, 테스트9 통과, 위로 가면 안됨
# print(solution(4, 4, [[3, 2], [2, 4]]), 7)
# print(solution(100, 100, []), 690285631)
""" 
정확성  테스트
테스트 1 〉	통과(0.01ms, 10.3MB)
테스트 2 〉	통과(0.01ms, 10.3MB)
테스트 3 〉	통과(0.04ms, 10.4MB)
테스트 4 〉	통과(0.06ms, 10.3MB)
테스트 5 〉	통과(0.05ms, 10.3MB)
테스트 6 〉	통과(0.06ms, 10.2MB)
테스트 7 〉	통과(0.04ms, 10.3MB)
테스트 8 〉	통과(0.11ms, 10.3MB)
테스트 9 〉	통과(0.06ms, 10.3MB)
테스트 10 〉	통과(0.02ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과(4.19ms, 10.4MB)
테스트 2 〉	통과(1.38ms, 10.2MB)
테스트 3 〉	통과(1.48ms, 10.2MB)
테스트 4 〉	통과(2.41ms, 10.2MB)
테스트 5 〉	통과(1.63ms, 10.2MB)
테스트 6 〉	통과(3.27ms, 10.3MB)
테스트 7 〉	통과(1.51ms, 10.3MB)
테스트 8 〉	통과(2.86ms, 10.2MB)
테스트 9 〉	통과(3.37ms, 10.3MB)
테스트 10 〉	통과(2.25ms, 10.3MB)
 """