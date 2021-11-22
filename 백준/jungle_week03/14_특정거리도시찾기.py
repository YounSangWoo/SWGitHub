# https://www.acmicpc.net/problem/18352

""" 
입력
첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다.
(2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N) 
둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 공백을 기준으로 구분되어 주어진다. 

이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미다. 
(1 ≤ A, B ≤ N) 단, A와 B는 서로 다른 자연수이다.

출력
X로부터 출발하여 도달할 수 있는 도시 중에서, 
최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.

이 때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력한다.

예제 입력 1 
4 4 2 1
1 2
1 3
2 3
2 4
예제 출력 1 
4

"""
# bfs
from collections import deque
import sys
input = sys.stdin.readline

n,m,k,x = map(int,input().strip().split())
graph = [[] for i in range(n+1)]
ans = [-1]*(n+1)
ans[x] = 0 #자기 자신까지의 최소거리
que = deque([x])

for _ in range(m):
    a,b = list(map(int,input().split()))
    graph[a].append(b)

while que:
    now = que.popleft()
    for next in graph[now]:
        if ans[next]== -1:
            ans[next]= ans[now]+1
            que.append(next)
for i in range(n+1):
    if ans[i]==k:
        print(i)
if k not in ans:
    print(-1)
