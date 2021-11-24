# https://www.acmicpc.net/problem/1948

""" 
예제 입력 1 
7
9
1 2 4
1 3 2
1 4 3
2 6 3
2 7 5
3 5 1
4 6 4
5 6 2
6 7 5
1 7

예제 출력 1 

12
5
"""
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[]for _ in range(N+1)]
backgraph = [[]for _ in range(N+1)]
indegree= [0]*(N+1)
max_v = [0]*(N+1)
visit = [0]*(N+1)



for _ in range(M):
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))
    backgraph[b].append((a, cost))
    indegree[b]+=1

start, end = map(int,input().split())

def topology_sort(start):
    q = deque()
    q.append(start)
    count = 0
    while q: #indegree
        now = q.popleft()
        for i,cost in graph[now]:
            indegree[i]-=1
            max_v[i]= max(max_v[i], max_v[now]+cost)
             #해당 노드까지 가는데 드는 코스트의 max를 갱신
            if indegree[i]==0:
                q.append(i)
    
    ##최장거리 출력##
    print(max_v[end])
    
    #back tracking
    q.append(end)
    while q:
        now = q.popleft()
        for i, cost in backgraph[now]:
            if  max_v[now]==max_v[i]+cost:
                count+=1
                if visit[i]==0:
                    visit[i]=1
                    q.append(i)

        
    ##쉬지않고 달려야 하는 edge 출력 ##
    print(count)
    
topology_sort(start)

        

