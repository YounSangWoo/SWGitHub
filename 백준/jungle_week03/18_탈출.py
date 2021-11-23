# https://www.acmicpc.net/problem/3055

from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
visit = [[0]*C for _ in range(R)]
Sonic = deque()
Flood = deque()
graph= []
for _ in range(R):
  graph.append(list(map(str, input().strip())))

for i in range(R):
    for n in range(C):
        if graph[i][n]=='S':
            Sonic.append([i,n])
        if graph[i][n]=='*' :
            Flood.append([i,n])
        if graph[i][n]=='D' :
            da = i
            db = n #안전가옥 위치

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    while Sonic:
         #미리 소닉이 방문한 곳의 값을 저장해두어야 안빠져죽음
        for _ in range(len(Flood)):
            a,b = Flood.popleft()
            for i in range(4):
                na = a+dx[i]
                nb = b+dy[i]
                if 0 <= na < R and 0 <= nb < C:  #홍수 방문
                    if graph[na][nb]=='.' or graph[na][nb]=='S':
                        graph[na][nb] = '*'
                        Flood.append([na,nb])
        for _ in range(len(Sonic)):
            x, y = Sonic.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<R and 0<=ny<C  : #고슴도치의 방문
                    if (graph[nx][ny] == '.' or graph[nx][ny] == 'D') and visit[nx][ny]==0:
                        visit[nx][ny] = visit[x][y]+1
                        Sonic.append([nx,ny])
bfs()

if visit[da][db] ==0:
    print("KAKTUS")
else : print(visit[da][db])