""" import sys
def solution(n, s, a, b, fares):
    answer = sys.maxsize
    cost = [([sys.maxsize]*n) for _ in range(n)]
    for A, B, costa in fares:
        cost[A-1][B-1] = min(cost[A-1][B-1], costa)
        cost[B-1][A-1] = min(cost[B-1][A-1], costa)

    for k in range(n):
        cost[k][k] = 0
        for i in range(n):
            for j in range(n):
                cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])

    for start in range(n):
        tmp = cost[start][a-1]+cost[start][s-1]+cost[start][b-1]
        if answer >= tmp:
            answer = tmp

    return answer """

import sys


def solution(n, s, a, b, fares):
    answer = sys.maxsize
    cost = [([sys.maxsize]*n) for _ in range(n)]
    for A, B, costa in fares:
        cost[A-1][B-1] = min(cost[A-1][B-1], costa)
        cost[B-1][A-1] = min(cost[B-1][A-1], costa)

    for k in range(n):
        cost[k][k] = 0
        for i in range(n):
            for j in range(n):
                cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])

    for start in range(n):
        tmp = cost[start][a-1]+cost[start][s-1]+cost[start][b-1]
        if answer >= tmp:
            answer = tmp

    return answer


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [
      5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]), '82')
