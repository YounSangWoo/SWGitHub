# https://www.acmicpc.net/problem/1005

from collections import deque
import sys
input = sys.stdin.readline


def topology_sort():  # 위상정렬 +dp
    dp = [-sys.maxsize] * (N+1)
    q = deque()
    for i in range(1, N+1):
        #진입차수가 0인 노드를 q에 담는다.
        if indegree[i] == 0:
            q.append(i)
            dp[i] = time[i]
    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[now] + time[i])
            if indegree[i] == 0:
                q.append(i)                
    return dp[final]



T = int(input())
for _ in range(T):
    N, M = map(int,input().rstrip().split())
    time = [0]+list(map(int, input().rstrip().split()))
    indegree = [0]*(N+1)
    graph = [[]for i in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        #a 이후 b건물이 만들어진다.
        indegree[b] += 1
        #b로 들어가는 진입차수 1 증가
    final = int(input().rstrip())
    
    print(topology_sort())

