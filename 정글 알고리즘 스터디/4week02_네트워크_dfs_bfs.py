""" from collections import deque


def solution(n, computers):
    network = 0
    visit = [[0]*n for _ in range(n)]
    # 연결되었던거 확인한 네트워크 끼리는 다시 볼 필요 없음, 애초에 0이면 못감
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        q = deque()
        q.append([x, y])

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                    if (computers[nx][ny] == 1):
                        newlist = [(nx, ny), (nx, nx), (ny, nx), (ny, ny)]
                        for anx, bny in newlist:
                            visit[anx][bny] = 1  # 방문처리
                            if ([anx,bny]) not in q:
                                q.append([anx, bny])

    for j in range(n):
        flag = True
        for k in range(n):
            if visit[j][k] == 0 and computers[j][k] == 1:
                visit[j][k] = 1
                bfs(j, k)
                if flag:
                    network += 1
                    flag = False

    # 연결을 찾아들어갈때 네트워크 수 1증가 시키고 연결된 돗을 찾으며 들어 가다 끊기면 다른 네트워크 시작 그 네트워크는 방문 안한 곳이어야한다.
    return network


print(solution(3, [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
 """
#홍정이형 풀이
import sys
sys.setrecursionlimit(2000000)


def solution(n, computers):

    def DFS(y):
        # (y, y) 값들을 방문여부로 한다. 미방문 1, 방문 -1
        computers[y][y] = -1
        for j in range(n):
            if computers[y][j] == 1:
                if computers[j][j] == 1:
                    DFS(j)
                computers[y][j] = -1

    cnt = 0
    for i in range(n):
        # DFS 발동하는 회수만큼 네트워크
        if computers[i][i] == 1:
            DFS(i)
            cnt += 1

    return cnt




#동진이 풀이
def dfs(computer, network, visited):
    for start in network[computer]:
        if start != computer and start not in visited:
		#방문할 곳이 자기자신이 아니고 방문체크 되어 있지 않으면 방문체크하고 방문
            visited.add(start)
            dfs(start, network, visited)
    return


def solution(n, computers):
    from collections import defaultdict
    network = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if computers[i][j] != 0:
                network[i].append(j)

		# defaultdict(<class 'list'>, {0: [0, 1], 1: [0, 1], 2: [2]})
    visited = set()  # 방문체크
    cnt = 0  # 탐색 새로 시작하면 네트워크 개수 +1

    for start in network:
        if start not in visited:
            visited.add(start)
            dfs(start, network, visited)
            cnt += 1

    answer = cnt
    return answer
#지윤누나 풀이


def solution(n, computers):
    visited = [[False]*n for i in range(n)]
    cnt = 0

    def dfs(i, j):
        for k in range(n):
            if visited[j][k] == False and computers[j][k] == 1:
                visited[j][k], visited[k][j] = True, True
                dfs(j, k)

    for i in range(n):
        for j in range(n):
            if visited[i][j] == False and computers[i][j] == 1:
                dfs(i, j)
                cnt += 1

    return cnt
