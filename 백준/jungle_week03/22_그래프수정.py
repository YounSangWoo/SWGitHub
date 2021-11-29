# https://www.acmicpc.net/problem/1432

""" 
문제
N개의 정점이 있는 그래프가 주어지면, 
다음과 같은 방법에 의해서 정점의 번호를 다시 매기고 싶다.

모든 그래프의 번호는 1보다 크거나 같고 N보다 작거나 같은 번호를 가져야 한다.

만약 V1에서 V2로 연결된 간선이 있다면, V2의 번호는 V1보다 커야 한다.

위와 같은 조건을 이용해서 그래프의 번호를 다시 매긴 후에, 
1번 정점의 새로 고친 번호를 M1, 2번 
정점의 새로 고친 번호를 M2, ..., N번 
정점의 새로 고친 번호를 MN이라고 하면, N개의 수열이 만들어진다.

이 수열을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N이 주어진다. 
둘째 줄부터 N개의 줄에는 인접행렬 형식으로 입력이 주어진다. 
0은 연결되지 않았음을 의미하고, 
1은 연결되었다는 것을 의미한다. 
N은 50보다 작거나 같은 자연수이다.

출력
첫째 줄에 수열의 각 원소를 차례대로 공백을 사이에 두고 출력한다. 
만약 그래프의 번호를 수정할 수 없다면 -1을 출력한다. 
답이 여러 개일 경우에는 사전 순으로 제일 앞서는 것을 출력한다.


예제 입력 1
.....
5
00001
00010
00000
00001
00100

예제 출력 1 
1 2 5 3 4
"""

import sys,heapq
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
outdegree = [0]*(N+1)
result = [0]*(N+1)
v_info = [list(map(int, input().strip()))for _ in range(N)]

for i in range(N):
    for n in range(N):
        if v_info[i][n] == 1:
            graph[n+1].append(i+1)
            outdegree[i+1] += 1

def topology_sort(N):
    q = []
    for i in range(1, N+1):
        if outdegree[i] == 0:
            heapq.heappush(q, -i)# 답이 여러개인경우 사전순 출력을 위해 max heap이 되어야 하므로 -로 넣어준다.
    while q:
        now = -heapq.heappop(q)
        result[now]=N #outdegree가 0이란 말은 그보다 큰값이 없다는 뜻이므로 최대값인 N 을 부여한다.
        for i in graph[now]:
            outdegree[i] -=1
            if outdegree[i] == 0:
                heapq.heappush(q,-i)
        N-=1 #그다음 최대값을 부여하여야 하므로 N-1해준다.

topology_sort(N)


if 0 in result[1:]:
    print(-1)
else:
    for i in range(1,N+1):
        print(result[i], end=' ')



