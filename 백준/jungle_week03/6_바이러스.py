# https://www.acmicpc.net/problem/2606


import sys
input = sys.stdin.readline


# 유니온 파인드 알고리즘을 이용한 풀이 틀렸다고 나옴
 
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    rootA = find(a)
    rootB = find(b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB


v = int(input())
e = int(input())
parent = [0] * (v + 1)
edges = []
virus = 0

for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a, b = map(int, input().split())
    edges.append((a, b))

edges.sort(key=lambda x: x[1])

for edge in edges:
    a, b = edge
    if find(a) != find(b):
        union(a, b)

for i in range(2, len(parent)):
    if parent[i] == parent[1]:
        virus += 1

print(virus)

#  dfs를 활용
# 1번을 시작으로 DFS하였을때 방문한 곳의 카운트를 센다.

""" 
def dfs(n):
  global visit_count
  visit_list[n] = 1
  visit_count += 1
  for i in range(1, v + 1):
    if visit_list[i] == 0 and graph[n][i] == 1:
      dfs(i)


v = int(input())
e = int(input())


graph = [[0] * (v + 1) for _ in range(v + 1)]
visit_list = [0] * (v + 1)
visit_count = -1

for _ in range(e):
  a, b = map(int, input().split())
  graph[a][b] = graph[b][a] = 1

dfs(1)

print(visit_count)
 """