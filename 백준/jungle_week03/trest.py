import sys
from collections import deque


n, m = map(int, sys.stdin.readline().split())
h_graph = [[] for _ in range (n+1)]
l_graph = [[] for _ in range (n+1)]
for _ in range(m):
    h, l = map(int, sys.stdin.readline().split())
    h_graph[l].append(h)
    l_graph[h].append(l)

def dfs(num, g):
    stack = deque()
    stack.append(num)
    visitied = [False for _ in range(n+1)]
    cnt = 0
    while stack:
        cur = stack.pop()
        visitied[cur] = True
        for item in g[cur]:
            if visitied[item] == False:
                stack.append(item)
                cnt += 1
    return cnt
limit = n//2#n은 홀수  2
limit_over=0
for i in range(1, n+1):
    if dfs(i, h_graph) > limit: # 절반 + 1 보다 클경우
        limit_over += 1
    if dfs(i, l_graph) > limit:
        limit_over += 1

print(limit_over)