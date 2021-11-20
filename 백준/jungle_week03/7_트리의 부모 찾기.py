# https: // www.acmicpc.net/problem/11725
""" 
문제
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.
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



#간선정보입력
for i in range(N-1):
    a, b = map(int,input().split)
    edges.append((a,b))

edges.sort(key = lambda x: -x[0])

for edge in edges:
    a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함(=연결한다.)
    if find(parent, a) != find(parent, b)
