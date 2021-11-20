import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB


N= int(input())
edges =[]
parent = [0]*N+1
answer = []
#부모 초기화

for i in range(1, N+1):
    parent[i] = i


#간선정보입력
for i in range(N-1):
    a, b = map(int,input().split)
    edges.append((a,b))

edges.sort(key = lambda x: -x[0])

for edge in edges:
    a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함(=연결한다.)
    if find(parent, a) != find(parent, b)
