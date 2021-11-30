# https://www.acmicpc.net/problem/1149


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
graph = []

for i in range(N):
    graph.append(list(map(int,input().split())))

INF = int(1e9)
dp = [[INF]*3 for _ in range(N)]

def dfs(x,color):
    if x>N-1:
        return 0
    
    if dp[x][color] != INF:       # 이미 최소비용이 계산되어 있다면
        return dp[x][color]
    
    for i in range(3):  #시작위치로부터 RGB탐방
        if color == i: #같은 색이라면
            continue
        dp[x][color] = min(dp[x][color], dfs(x+1, i) + graph[x][color])
    return dp[x][color]

for i in range(3):
    dfs(0,i)

print(min(dp[0]))