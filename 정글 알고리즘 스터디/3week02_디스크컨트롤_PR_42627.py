from heapq import heappop, heappush
def solution(jobs):
    heap =[]
    answer = 0
    N = len(jobs)
    time, last, cnt = 0,-1,0
    
    while cnt<N:
        for start, work in jobs:
            if last<start<=time:
                heappush(heap,[work,start])
        if len(heap):
            work, start = heappop(heap)
            last = time 
            time+=work
            answer +=(time-start)
            cnt+=1
        else:
            time+=1
    answer //= N
    return answer

print(solution([[0, 3], [1, 9], [2, 6]]))
