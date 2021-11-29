# https://www.acmicpc.net/problem/8983 사냥꾼


""" 

1.사대의 위치를 정렬한다.

2.동물들의 좌표를 돌려 동물이 잡히는지 안잡히는지 판단 잡히면 카운트 아니면 노카운트
해당 작업을 이분탐색을 통해 찾는다.

중앙에 있는 사대의 위치를 처음 시작으로
동물의 x좌표와 비교  동물의 x좌표가 더 크다면 오른쪽으로 사대찾기 이동 : 사대가 오름차순으로 정렬되어 있어서
동물의 a b 좌표가 L 안에들어오면 count

""" 


import sys
input = sys.stdin.readline

m, n, L = map(int,input().split())          #사대갯수, 동물수, 사격거리 입력

sr = list(map(int,input().split()))
sr.sort()

animal = [list(map(int,input().split() ))for _ in range(n)]

count = 0
for a,b in animal:
    pl = 0
    pr = len(sr)-1 #인덱스
   
    while pl<pr:  #동물의 위치는 항상 사대의 범위 안에 있음, 따라서 사대안에서 동물의 위치 와 가장 가까이 있는 사대를 이분탐색으로 찾는다
        pc = (pl+pr)//2
        if a>sr[pc]:   #사대의 위치가 동물의 위치보다 작아?
            pl = pc+1  
        else:  #동물의 위치가 사대와 일치하거나 큰경우다. 따라서 같은경우가 있으므로 pr = pc
            pr = pc # 왜? -1을 하면 5가 나온다
    #while  을 같지 않은 경우 나왔다면? pr은 pc 혹 은 사로의 끝 사로의 끝으로 나온경우는 동물이 끝사로에 가깝다는 뜻

    
    if (abs(sr[pr]-a))+b <= L or (abs(sr[pr-1]-a))+b <= L: #따라서 사로의 끝으로 검사하거나 끝에서 가장 가까운 사로를 검사
            count +=1

print(count)





