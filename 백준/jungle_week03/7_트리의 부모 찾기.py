# https://www.acmicpc.net/problem/11725
""" 
문제
루트 없는 트리가 주어진다.
 이때, 트리의 루트를 1이라고 정했을 때,
  각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 
둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.
7
1 6
6 3
3 5
4 1
2 4
4 7

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

4
6
1
3
1
4
 """
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
edges = []
N = int(input())
graph = [[] for _ in range(N + 1)]
parents = [0 for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    edges.append((a, b))
    # graph[a][b] = graph[b][a] = 1
    graph[a].append(b)
    graph[b].append(a)


def dfs(start, graph, parents):
    for i in graph[start]:  # start = 부모
        if parents[i] == 0:
            parents[i] = start
            dfs(i, graph, parents)


dfs(1, graph, parents)

for i in range(2, len(parents)):
    print(parents[i])
