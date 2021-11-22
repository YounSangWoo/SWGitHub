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