from collections import deque

def solution(priorities, location):
    answer = 0
    priorities = deque(priorities) #popleft를 쓰기위해 deque로 형변환

    while True:
        maxpr = max(priorities)
        a=priorities.popleft()

        if a==maxpr: #왼쪽부터 순서대로 뽑은 값이 max라면?
            if location == 0:
                answer+=1
                break
            else :
                answer+=1
                location-=1
                
        else :
            location-=1
            priorities.append(a)
            if location<0:
                location = len(priorities)-1
            

    return answer