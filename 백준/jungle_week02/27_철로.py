# https://www.acmicpc.net/problem/13334

import sys
import heapq
input = sys.stdin.readline

def subway(ho,d):
    i=0
    while i < len(ho):
        if abs(ho[i][1]-ho[i][0])>d :
            i+=1
        else : 
            ho[i].sort() #아닐경우 재정렬
            home_office.append(ho[i])
            i+=1
        
    if len(home_office)>0 :
        home_office.sort(key=lambda x: x[1])

        line = [] #heap
        count =0
        for i in home_office:    
            if len(line)>0:
                while True:
                    try:
                        if line[0][0]>=(i[1]-d):
                            break
                        else : heapq.heappop(line)
                    except: 
                        break
                
                heapq.heappush(line,i)
    
            else :
                heapq.heappush(line, home_office[0])
       
            count = max(count, len(line))

        return count
    else :
        return 0


N = int(input())
ho = [list(map(int, input().split()))for _ in range(N)]
home_office=[] # remove함수로  ho 의 값을 제거하려 했으나 그럴경우 시간초과가 나서 home_office 리스트에 새로 저장
d = int(input())

print(subway(ho,d))




 

