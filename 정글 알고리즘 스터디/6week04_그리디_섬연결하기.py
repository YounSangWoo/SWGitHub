# https://programmers.co.kr/learn/courses/30/lessons/42861

from collections import deque
def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x:x[2])#가중치 순으로 간선 정렬
    costs = deque(costs)

    mst = []
    p=[]# 상호 배타적 집합
    
    for i in range(0,n):
        p.append(i) #각 정점 자신이 집합의 대표
    
    def find(u):
        if u != p[u]:
            p[u] = find(p[u]) #경로 압축
        return p[u]

    def union(u,v):
        root1 = find(u)
        root2 = find(v)
        p[root2] = root1 #임의로 root2가 root1의 부모
    
    legs = 0 #간선의 수
    mst_cost = 0 #가중치 합
    
    while True:
        if legs == n-1:
            break
        u,v,cost = costs.popleft()
        if find(u) != find(v): #u와 v가 서로 다른 집합에 속해 있다면?
            union(u,v)
            mst.append((u,v))
            mst_cost += cost
            legs += 1
    
    answer = mst_cost
            
    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
