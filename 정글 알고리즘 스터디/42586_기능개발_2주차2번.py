# https: // programmers.co.kr/learn/courses/30/lessons/42586
import math

def solution(progresses, speeds):
    n = len(progresses)
    i = 0
    answer = []
    
    while i<n:
        count = 0
        A = 100-progresses[i]
        B = math.ceil(A/speeds[i]) #올림함수 math.ceil
        for j in range(n):
            progresses[j]+=speeds[j]*B #앞쪽의 기능이 개발되는 일수동안 다른 개발들도 진행이 된다.
        
        for k in range(i,n):
            #앞쪽 부터 개발된 것들 중 100이상인 기능을 카운트하고 이 기능들은 다음에 검사하지 않도록 i도 증가시킨다.
            if (progresses[k]>=100):
                count+=1
                i+=1
            else:
                break
                
        answer.append(count)
        
    return answer