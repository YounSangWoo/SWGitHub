import bisect


""" def solution(n, times):
    answer = 0
    timeslist = []
    temp = []
    for k in range(1, n+1):
        for i in times:
            bisect.insort(timeslist, i*k)
        temp.append(timelist.pop(0))

    answer = timeslist[n-1]
    print(answer)

    return answer
 """


""" def solution(n, times):
    answer = 0 
    times.sort()
    timeslist =[]
    count = 0
    while True:
        count += 1
        for i in range(len(times)):
            bisect.insort(timeslist, times[i]*count)

        k = timeslist[-1]//timeslist[0]

        if k>=n-1 and len(timeslist)>=n-1:
            answer = timeslist[n-1]
            break
    return answer

print(solution(6,[1,8]))
 """

def solution(n, times):
    answer = 0

    left = 1
    right = min(times) * n
    # 가장 입국심사가 빨리 끝나는 심사원에게 n명 모두 간 시간보다는 적게 걸리는 것이 효율적일 것

    while left <= right:
        mid = (left+right) // 2
        people = n

        for time in times:
            people -= mid // time
            if people <= 0:
                answer = mid
                right = mid - 1
                break
        if people > 0:
            left = mid + 1

    return answer
print(solution(6,[7,10]))