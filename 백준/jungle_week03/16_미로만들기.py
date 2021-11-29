# https://www.acmicpc.net/problem/2665

""" 
예제 입력 1
8
11100110
11010010
10011010
11101100
01000111
00110001
11011000
11000111

예제 출력 1
2

"""

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().strip()))for _ in range(N)]
ch = [[-1]*N for _ in range(N)]

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    de = deque()
    de.append([0,0])
    ch[0][0]=0

    while de:
        x,y = de.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<N and 0<=ny<N:
                if ch[nx][ny]==-1:
                    if graph[nx][ny]==0:
                        ch[nx][ny] = ch[x][y]+1
                        de.append([nx, ny])
                    else :
                        ch[nx][ny] = ch[x][y]
                        de.appendleft([nx,ny])

bfs()
print(ch[N-1][N-1])