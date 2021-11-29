# https://www.acmicpc.net/problem/21606

""" 문제
아침 산책을 즐기는 서현이는 서울과학고에 입학해서도 아침 산책을 즐기려고 합니다.
서현이는 산책을 위해 서울과학고의 지리를 분석했고,
그 결과 서울과학고를 N개의 장소를 N-1개의 길이 잇는 트리 형태로 단순화시킬 수 있었습니다.
트리 구조이므로, 모든 장소를 몇 개의 길을 통해 오고갈 수 있습니다.

아침 산책은 시작점과 도착점을 정하고,
시작점에서 도착점까지 트리 위의 단순 경로(같은 점을 여러 번 지나지 않는 경로)를 따라 걷게 됩니다.
트리 위의 두 점 사이의 경로는 유일하므로 시작점과 도착점이 정해지면 경로는 유일하게 결정됩니다.

N개 장소 중에 일부 장소는 실내이며,
나머지 장소는 실외입니다.
서현이는 산책을 시작하기 전부터 운동을 하는 것을 원치 않기 때문에,
산책의 시작점과 끝점은 모두 실내여야 합니다.

또한, 산책 도중에 실내 장소를 만나면 산책을 그만두고자 하는 욕구가 생기기 때문에,
산책 경로 위에 시작점과 끝점을 제외하고 실내 장소가 있으면 안 됩니다.

서현이는 매일 다른 산책 경로를 걷고자 합니다. 서로 다른 산책 경로가 몇 가지 있는지 구해 봅시다.

입력
첫 줄에는 정점의 수 N이 주어집니다.

둘째 줄에는 1과 0으로 이루어진 길이 N의 문자열 A가 주어집니다.
i번째 문자 A_i가 1일 경우 i번 장소는 실내이며,
0인 경우 i번 장소는 실외입니다.

셋째 줄부터 N+1번 줄까지는 i+2번 줄에 트리의 각 간선을 나타내는 두 정수 u_i, v_i가 주어집니다.
이는 i번째 간선이 u_i번 정점과 v_i번 정점을 연결한다는 의미입니다.

5
10111
1 2
2 3
2 4
4 5

출력
가능한 서로 다른 산책 경로의 수를 출력합니다.

8

 """
#78점 코드
""" import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

v = int(input())
inout = [0]
num=list(map(int, input().strip()))
count = 0

for i in num:
    inout.append(i)

graph = [[] for i in range(v+1)]  # 빈 그래프 생성

for _ in range(v-1):
    a, b = map(int, input().split())
    graph[a].append(b)  # 무방향 그래프
    graph[b].append(a) 


def dfs(v, inout):
    global count
    visited[v] = 1 #방문체크
    for i in graph[v]:
        if visited[i] == 0 and inout[i] !=1:
            dfs(i, inout)
        elif visited[i]!=1 and inout[i]==1: 
            count +=1
            

for i in range(1, v+1):
    if inout[i] != 0:
        visited = [0] * (v+1)  # 방문한 정점 체크
        dfs(i,inout)

print(count) 
"""

#200점 !

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

v = int(input())
inout = [0]
num = list(map(int, input().strip()))
count = 0
x=0 #실외부모 실내자식의 경우
y = 0 
result =0

for i in num:
    inout.append(i)

graph = [[] for i in range(v+1)]  # 빈 그래프 생성

for _ in range(v-1):
    a, b = map(int, input().split())
    graph[a].append(b)  # 무방향 그래프
    graph[b].append(a)
    if inout[a] == 1 and inout[b] ==1:
        count +=2


def dfs1(v, inout):
    global x, y, count
    visited1[v] = 1  # 방문체크
    for i in graph[v]:
        if visited1[i] == 0 and inout[i] == 1: #방문안하고 실내인경우
            x+=1   
        elif visited1[i] == 0 and inout[i] == 0: #방문안하고 실외인경우
            dfs1(i, inout)


visited1 = [0] * (v+1)  # 실외 방문 체크

for i in range(1, v+1):
    if inout[i] == 0 and visited1[i] == 0:#실외이고 방문 안한경우
        x=0
        dfs1(i, inout)
        result += x**2-x
        

count += result
print(count)

""" import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

v = int(input())
inout = [0]
num = list(map(int, input().strip()))
count = 0
x = 0  # 실외부모 실내자식의 경우
y = 0  # 실내부모 실내자식의 경우

visited3 = [0] * (v+1)
visitedchild = [0] * (v+1)

for i in num:
    inout.append(i)

graph = [[] for i in range(v+1)]  # 빈 그래프 생성

for _ in range(v-1):
    a, b = map(int, input().split())
    graph[a].append(b)  # 무방향 그래프
    graph[b].append(a)
   


for i in range(1,len(graph)):
    if inout[i] ==0 and visited3[i]==0:
        visited3[i] = 1
        for i in graph[i]:
            if inout==1 and visitedchild[i]==0:
                visitedchild[i] = 1
                x+=1
    if inout[i]==1 and visited3[i]==0:
        visited3[i] =1
        for i in graph[i]:
            if inout ==1 and visitedchild[i]==0:
                visitedchild[i]=1
                y+=1


count = x**2-x+2*y
print(count)
 """