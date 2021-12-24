def solution(distance, rocks, n):
    rocks.sort()
    rocks = [0]+rocks+[distance]
    answer = 0

    left = 0
    right = distance
    while right >= left:
        count = 0
        mid = (left+right)//2
        sub = rocks[0]
        for i in range(1, len(rocks)):
            if rocks[i]-sub < mid:
                sub = sub
                count += 1
            else:
                sub = rocks[i]
        if count > n:
            right = mid-1
        else:
            answer = mid
            left = mid+1

    return answer
