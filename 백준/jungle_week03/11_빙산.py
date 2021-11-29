# https://www.acmicpc.net/problem/2573
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def check():
    global iceberg_count, flag
    for i in range(1,N-1):
        for j in range(1, M-1):  # 배열의 첫 번째 행과 열, 마지막 행과 열에는 항상 0으로 채워진다.
            if iceberg[i][j] and visited[i][j]==0:
                flag = 0
                iceberg_count +=1
                if iceberg_count >1:
                    return
                visited[i][j]=1
                dfs(i,j,0)

def dfs(r,c,count):
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        if nr>=N or nr<0 or nc>=M or nc<0: #범위를 벗어나는경우
            continue
        if iceberg[nr][nc]==0 and visited[nr][nc]==0:
            count += 1
        if iceberg[nr][nc] and visited[nr][nc]==0: #빙산이 연결된경우 (방문을 안했고 빙산이 있다면?)
            visited[nr][nc] = 1
            dfs(nr,nc,0) #바다 count 는 초기화
    if count>0:
        iceberg[r][c]-=count
        if iceberg[r][c]<0:
            iceberg[r][c]=0


N, M = map(int, input().split())

iceberg = [list(map(int, input().split())) for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
year = 0

while True:
    flag = 1 #빙산 여부 체크
    iceberg_count = 0
    visited = [[0] * M for _ in range(N)]
    check() 
    if iceberg_count > 1:
        break
    if flag: 
        year = 0
        break
    year += 1

print(year)


""" 
import sys
input = sys.stdin.readline
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def bfs(y, x, visit):
    q = deque()
    melt = deque()
    q.append((y, x))
    visit[y][x] = 1
    while q:
        y, x = q.popleft()
        cnt = 0

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= ny < N and 0 <= nx < M and not visit[ny][nx]:
                if not Map[ny][nx]: cnt += 1
                elif Map[ny][nx]:
                    visit[ny][nx] = 1
                    q.append((ny, nx))
        if cnt:
            melt.append((y, x, cnt))
    for _ in range(len(melt)):
        y, x, c = melt.popleft()
        Map[y][x] = max(0, Map[y][x] - c)

N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
t = 0

while 1:
    zone = 0
    visit = [[0] * M for _ in range(N)]
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if Map[i][j] and not visit[i][j]:
                zone += 1
                bfs(i, j, visit)
    if zone == 0:
        print(0); break
    elif zone >= 2: 
        print(t); break
    t += 1;
 """