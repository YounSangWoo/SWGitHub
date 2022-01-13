# https://programmers.co.kr/learn/courses/30/lessons/42861

from collections import defaultdict

def solution(n, costs):
    answer = 0
    cost_list = defaultdict(set)
    for first, second, cost in costs:
        cost_list[first].add(cost)
        cost_list[second].add(cost)
    for i in range(n):
        answer += min(cost_list[i])

    return answer

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))