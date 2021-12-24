""" def solution(operations):
    que = []
    answer = []
    for i in operations:
        if i[0] == "I":
            que.append(int(i[2:len(i)]))
        else:
            que.sort()
            if i[2] == "1":
                que.pop()
            else:
                que.pop(0)
    if len(que)>1:
        que.sort()
        answer.append(que.pop())
        answer.append(que.pop(0))
    else:
        answer=[0,0]
    
    return answer

print(solution(["I 7","I 5","I -5","D -1"])) """

from heapq import nlargest, nsmallest
def solution(operations):
    que = []
    answer = []
    for i in operations:
        if i[0] == "I":
            que.append(int(i[2:len(i)]))
        else:
            que.sort()
            if i[2] == "1" and len(que):
                que.pop()
            elif len(que):
                que.pop(0)
    if len(que) >= 1:
        answer.append(nlargest(1, que)[0])
        answer.append(nsmallest(1, que)[0])
    else:
        answer = [0, 0]
    return answer
