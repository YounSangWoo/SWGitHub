# https://www.acmicpc.net/problem/2098
""" 
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
 """
import sys
input =sys.stdin.readline
N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

INF = int(1e9)
dp = [[INF] * (1 << N) for _ in range(N)]


def dfs(x, visited): 
    if visited == (1 << N) - 1: # 10000 -> 01111 #모든 도시 방문
        if graph[x][0]:
            return graph[x][0]
        else:                       # 출발점으로 가는 경로가 없을 때
            return INF
    
    if dp[x][visited] != INF:       # 이미 최소비용이 계산되어 있다면
        return dp[x][visited]

    for i in range(1, N):           # 모든 도시를 탐방
        if not graph[x][i]:         # 가는 경로가 없다면 skip
            continue
        if visited & (1 << i):      # 이미 방문한 도시라면 skip
            continue
        dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1 << i)) + graph[x][i])
    
    return dp[x][visited]

print(dfs(0,1))

    
