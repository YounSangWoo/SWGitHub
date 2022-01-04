from collections import defaultdict, deque


def solution(n, edge):
    answer = 0
    edge.sort()
    q = deque()
    graph = defaultdict(list)
    depth = [0]*(n+1)
    visited = [0]*(n+1)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    visited[1] = 1
    for i in graph[1]:
        visited[i] = 1
        depth[i] += 1
        q.append(i)

    while q:
        j = q.popleft()
        if graph[j]:
            for i in graph[j]:
                if visited[i] == 0:
                    visited[i] = 1
                    depth[i] = depth[j]+1
                    q.append(i)

    maxdepth = max(depth)
    for i in range(len(depth)):
        if depth[i] == maxdepth:
            answer += 1

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
