# https://www.acmicpc.net/problem/7569 토마토
""" 
입력
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N과 쌓아올려지는 상자의 수를 나타내는 H가 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100 이다. 둘째 줄부터는 가장 밑의 상자부터 가장 위의 상자까지에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄에는 하나의 상자에 담긴 토마토의 정보가 주어진다. 각 줄에는 상자 가로줄에 들어있는 토마토들의 상태가 M개의 정수로 주어진다. 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다. 이러한 N개의 줄이 H번 반복하여 주어진다.

토마토가 하나 이상 있는 경우만 입력으로 주어진다.

출력
여러분은 토마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산해서 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.

예제 입력 2 
5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0

예제 출력 2 
4

예제 입력 1 

5 3 1
0 -1 0 0 0
-1 -1 0 1 1
0 0 0 1 1

예제 출력 1 

-1
 """

from collections import deque
import sys
input = sys.stdin.readline

dy = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

N, M, H = map(int, input().split())
box = [[] for _ in range(H)]
de = deque()
vis = [[[0]*N for _ in range(M)] for _ in range(H)]

for h in range(H):
    for m in range(M):
        box[h].append(list(map(int, input().strip().split())))
for h in range(H):
    for m in range(M):
        for n in range(N):
            if box[h][m][n]==1:
                de.append([h,m,n]) #미리 익은 사과들을 저장.
noneripe = False #안익은 사과가 있다면 True로 바뀜

def bfs():
    while de :
        z,y,x = de.popleft()
        vis[z][y][x] = 1
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]

            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
                if vis[nz][ny][nx] == 0: #방문 전이면
                    if box[nz][ny][nx] == 0:
                        vis[nz][ny][nx]= 1
                        box[nz][ny][nx]=box[z][y][x]+1 #가장 바깥쪽 0이 1이 될때 누적된 숫자가  일수 
                        de.append([nz,ny,nx])


bfs()
max_num = 0
for h in range(H):
    for m in range(M):
        for n in range(N):
            if box[h][m][n]==0: #안익은 사과가 남았다면
                noneripe = True
            max_num = max(max_num,box[h][m][n])
if noneripe :
    print(-1)
else :
    print(max_num - 1)#익은사과가 기본값이 1이므로 -1



    