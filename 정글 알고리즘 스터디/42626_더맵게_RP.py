import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort()

    while len(scoville)>1:
        if scoville[0] < K :
            rescovile = heapq.heappop(scoville) + (heapq.heappop(scoville)*2)
            heapq.heappush(scoville,rescovile)
            answer +=1
        else :
            return answer   
    if scoville[0]<K:
       return -1
    else : 
       return answer

print(solution([1,1],5))