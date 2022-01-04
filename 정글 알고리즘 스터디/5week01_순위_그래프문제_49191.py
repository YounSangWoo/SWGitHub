# from collections import defaultdict
""" from collections import defaultdict, deque
def solution(n, results):
    answer = 0
    graph = defaultdict(list)
    q = deque()
    
    for a,b in results:
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1,n+1):
        not_visited = [1]*n
        not_visited[i-1] = 0
        for j in graph[i]:
            q.append(j)
        while q:
            k = q.popleft()
            if not_visited[k-1]:
                not_visited[k-1] =0
                for z in graph[k]:
                    if not_visited[k-1] != 0:
                        q.append(z)
        if sum(not_visited)==0 :
            answer+=1      

    return answer


print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])) """

""" 
def solution(n, results):
    answer = 0
    graph = [0]*(n+1)
    indegree = [0]*(n+1)
    outdegree = [0]*(n+1)

    for a, b in results:
        # graph[a].append(b)
        outdegree[a] += 1
        if indegree[a] <= 1:
            indegree[b] += 1
        else:
            indegree[b] += (indegree[a]+1)

    for i in range(1, n+1):
        if indegree[i]+outdegree[i] == n-1:
            answer += 1

    return answer
 """
""" 

def solution(n, results):
    answer = 0
    graph = defaultdict(list)
    parents = defaultdict(list)
    indegree = [0]*(n+1)
    outdegree = [0]*(n+1)

    for a, b in results:
        graph[a].append(b)
        parents[b].append(a)
        indegree[b] += 1
        outdegree[a] += 1

    for i in range(1, n+1):
        for j in graph[i]: 
            #i가 자식 j가 부모, 내 자식이 가진 인디그리 부모가 더한다.
            indegree[j] += indegree[i]
            #outdegree는 자식의 자식수
            outdegree[i] += len(graph[j])

    for i in range(1, n+1):
        if indegree[i]+outdegree[i] == n-1:
            answer += 1

    return answer
print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])) """




from collections import defaultdict
def solution(n, results):
    win = defaultdict(set)  # 해당 노드가 이긴 노드
    lose = defaultdict(set)  # 해당 노드가 진 노드

    for winner, loser in results:
        win[winner].add(loser)
        lose[loser].add(winner)

    for i in range(1, n+1):
        for loser in win[i]:  # i에게 진 애들 : loser
            lose[loser].update(lose[i])  # i를 이긴 애들은 역시 loser를 이겼다.
        for winner in lose[i]:  # i를 이긴 애들
            win[winner].update(win[i])  # i한테 진 애들은 winner한테도 졌다.

    count = 0
    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n-1:
            count += 1

    return count
