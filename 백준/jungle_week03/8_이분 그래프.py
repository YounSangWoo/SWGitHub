# https://www.acmicpc.net/problem/1707
""" 
문제
그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 
그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

그래프가 입력으로 주어졌을 때,
 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 구성되어 있는데,
첫째 줄에 테스트 케이스의 개수 K가 주어진다.
각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V와 간선의 개수 E가 빈 칸을 사이에 두고 순서대로 주어진다.
각 정점에는 1부터 V까지 차례로 번호가 붙어 있다.
이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데,
각 줄에 인접한 두 정점의 번호 u, v (u ≠ v)가 빈 칸을 사이에 두고 주어진다. 
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2

출력
K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.
YES
NO

제한
2 ≤ K ≤ 5
1 ≤ V ≤ 20,000
1 ≤ E ≤ 200,000 

"""
""" 
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(v, color):
    visit_list[v] = color
    for i in graph[v]:
        if visit_list[i] == 0 and graph[v][i] == 1:
        dfs(i)



ans =[]


T = int(input())
for _ in range(T):
    v, e = map(int, input().split())
    visit_list = [0] * (v + 1)
    graph = [[] for _ in range(v + 1)]

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    difcolor = True

    for i in range(1, v+1 ):
         if visit_list[i] == 0:
             difcolor = dfs(i,1)
             if not difcolor:
                break

    ans.append(dfs(1,graph, difcolor))

for i in range(len(ans)):
    print(ans[i]) """

# dfs


def dfs(v, color):
    visited[v] = color  # 방문한 노드에 color 할당 
    for i in graph[v]:
        if visited[i] == 0:  # 아직 안 가본 곳이면 방문
            k = dfs(i, -color)  #color change
            if not k:
                return False
        elif visited[i] == visited[v]:  # 방문한 곳인데, 그룹이 동일하면 False
            return False
    return True

""" 
시작노드와 시작 컬러를 받는다
방문리스트에 시작노드의 컬러를 할당
시작노드와 연결된 자식들을 검사
자식들이 방문한 노드라면 자식을 시작노드로 다시 dfs 이때 자식노드의 컬러는 부모와 반대가 되도록
방문한 곳의 컬러가 인접노드컬러와 동일하다면? 이분그래프가 아님  

"""


T = int(input())
for _ in range(T):

    V, E = map(int, input().split())
    graph = [[] for i in range(V+1)]  # 빈 그래프 생성
    visited = [0] * (V+1)  # 방문한 정점 체크

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)  # 무방향 그래프
        graph[b].append(a)  # 무방향 그래프

    bipatite = True

    for i in range(1, V+1):
        if visited[i] == 0:  # 방문한 정점이 아니면, dfs 수행
            bipatite = dfs(i, 1)
            if not bipatite:
                break

    print('YES' if bipatite else 'NO')
