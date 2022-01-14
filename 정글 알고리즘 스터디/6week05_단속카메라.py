from collections import deque
""" def solution(routes):
    answer = 0
    routes.sort()
    visit_route = [0]*len(routes)
    for i in range(len(routes)):
        if visit_route[i] == 0:
            visit_route[i] = 1
            a, b = routes[i]
            answer += 1
            for j in range(len(routes)):
                if visit_route[j] == 0:
                    c, d = routes[j]
                    if a <= c and c <= b:
                        visit_route[j] = 1

    return answer """


def solution(routes):
    answer = 0
    camera = -30001

    routes.sort(key=lambda x: x[1])

    for start, end in routes:
        if start > camera:
            answer += 1
            camera = end

    return answer

# print(solution([[-2,-1], [1,2],[-3,0]])) #2
# print(solution([[0,0],])) #1
# print(solution([[0,1], [0,1], [1,2]])) #1
# print(solution([[0,1], [2,3], [4,5], [6,7]])) #4
# print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])) #2
# print(solution([[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2