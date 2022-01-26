from collections import defaultdict, deque


def solution(n, wires):
    # 먼저 양방향 리스트 만든다.
    a = [[] for _ in range(n+1)]
    for j, k in wires:
        a[j].append(k)
        a[k].append(j)

    #key는 부모 value는 자식만 넣기위한 dictionary
    nodes = defaultdict(list)
    for i in range(1, n+1):
        nodes[i]

    answer = 100
    tmpanswer = 100  # n은 100 이하이므로 차이는 98보다 커질 수 없다.
    comp = n//2  # 근사값 비교변수(절반으로 나누어 졌을때가 가장 이상적)

    q = deque()
    q.append(1)

    wires_set = set(i for i in range(2, n+1))

    #부모가 가진 자식들만 딕셔너리에 넣어준다.
    while q:
        i = q.popleft()
        for j in a[i]:
            if j in wires_set:
                nodes[i].append(j)
                wires_set.remove(j)
                q.append(j)

#1부터 시작하여 각 노드의 위치를 루트로 변경해 보며 자식의 수를 세 보아 차이가 가장 적은 루트가 나올때까지 검사해 본다.
    for i in range(1, n+1):
        count = 1
        q.append(i)
        while q:
            k = q.popleft()
            if nodes[k]:
                count += len(nodes[k])
                for j in nodes[k]:
                    q.append(j)
        if tmpanswer >= abs(comp-(n-count)):
            tmpanswer = abs(comp-(n-count))
            answer = min(answer, abs(n-(2*count)))

    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [  4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(6, [[1, 4], [6, 3], [2, 5], [5, 1], [5, 3]]))
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))

