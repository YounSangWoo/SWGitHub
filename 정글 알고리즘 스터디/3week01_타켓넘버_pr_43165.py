from collections import deque
def solution(numbers, target):
    n = len(numbers)
    answer = 0
    q = deque([0])

    for i in numbers:
        n -=1
        count = 0
        Q = len(q)
        while count < Q :
            count+=1
            k = q.popleft()
            a = k+i
            b = k-i
            q.append(a)
            q.append(b)
            if n == 0 and (a==target or b == target):
                answer+=1

    return answer


solution([1, 1, 1, 1, 1],3)

