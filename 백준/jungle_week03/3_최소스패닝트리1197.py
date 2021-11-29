# https://www.acmicpc.net/problem/1197
 
""" 
크루스칼 알고리즘 이용

정점 사이의 최소 가중치를 연결하되
사이클이 발생할경우 건너뛰고 다른 최소값의 가중치를 선택
모든 정점이 연결되면 종료 


 첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다. 
 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.\

3 3
1 2 1
2 3 2
1 3 3
"""

# 특정 원소가 속한 집합을 찾기
import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기 (간선 연결한다고 생각!)
def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA < rootB:
        parent[rootB] = rootA 
    else:
        parent[rootA] = rootB


# 입력받기
v, e = map(int, input().split())

parent = [0] * (v + 1)
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 오름차순 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함(=연결한다.)
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(result)
