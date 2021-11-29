# https://www.acmicpc.net/problem/10830 행렬제곱

import sys
input = sys.stdin.readline


def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += (arr1[i][k] * arr2[k][j])
    return answer


def rest_1(A: list):
    for i in range(N):
        for n in range(len(A[i])):
            A[i][n] = A[i][n] % 1000
    return A


def rest(A: list, B):
    if B == 1:
        return A
    else:
        tmp = rest(A, B//2)
        if not B % 2:
            return rest_1(solution(tmp, tmp))
        else:
            return rest_1(solution(solution(tmp, tmp), A))


N, B = map(int, input().split())
A = [list(map(int, input().split()))for _ in range(N)]

A = rest_1(A)

Ans = rest(A, B)
for i in range(len(Ans)):
    for n in range(len(Ans[i])):
        print(int(Ans[i][n]), end=' ')
    print()
