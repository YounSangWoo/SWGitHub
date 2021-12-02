# https://www.acmicpc.net/problem/17404


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))

INF = int(1e9)
dp = [[INF]*3 for _ in range(N)]


def dfs(x, color ,flag):
    if x > N-1:
        return 0

    for i in range(3):  # 시작위치로부터 RGB탐방
        if color == i or (x ==N-2 and flag == i):  # 같은 색이라면
            continue
        dp[x][color] = min(dp[x][color], dfs(x+1, i , flag) + graph[x][color])
    return dp[x][color]





for i in range(3):
    a =i
    dfs(0, i, a)

print(min(dp[0]))
