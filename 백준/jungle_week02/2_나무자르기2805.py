#2번 https://www.acmicpc.net/problem/2805 나무자르기

""" 상근이는 나무 M미터가 필요하다.
근처에 나무를 구입할 곳이 모두 망해버렸기 때문에, 정부에 벌목 허가를 요청했다. 
정부는 상근이네 집 근처의 나무 한 줄에 대한 벌목 허가를 내주었고, 상근이는 새로 구입한 목재절단기를 이용해서 나무를 구할것이다.

목재절단기는 다음과 같이 동작한다. 
먼저, 상근이는 절단기에 높이 H를 지정해야 한다.
높이를 지정하면 톱날이 땅으로부터 H미터 위로 올라간다. 
그 다음, 한 줄에 연속해있는 나무를 모두 절단해버린다. 

따라서, 높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않을 것이다.
예를 들어, 한 줄에 연속해있는 나무의 높이가 20, 15, 10, 17이라고 하자. 상근이가 높이를 15로 지정했다면,
나무를 자른 뒤의 높이는 15, 15, 10, 15가 될 것이고, 상근이는 길이가 5인 나무와 2인 나무를 들고 집에 갈 것이다.
(총 7미터를 집에 들고 간다) 절단기에 설정할 수 있는 높이는 양의 정수 또는 0이다.

상근이는 환경에 매우 관심이 많기 때문에, 나무를 필요한 만큼만 집으로 가져가려고 한다.
이때, 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오. 

입력: 
4 7 나무의수 N, 상근이가 필요한 나무의 길이 M
20 15 10 17 나무들의 길이

출력 : 
상근이가 나무를 가져가기위해 설정해야 하는 높이의 최댓값 
15
"""

import sys
input = sys.stdin.readline

def H(Tree:list ,N:int ,M:int)->int:

    pl = 0
    pr = max(Tree)
    C =[]
    
    while True:
        pc = (pr+pl)//2
        count = 0

        for i in range(N):
           
            if Tree[i]-pc >0 :
                count += Tree[i] - pc

        if count > M : #상근이가 필요한 길이보다 많다? 그럼 H가 적다는 소리
            pl=pc+1
            C.append(pc)
        elif count < M :
            pr=pc-1
        elif count == M :                                                                                                                                                                                                   
            print(pc)
            return
        if pl>pr:
            print(max(C))
            return
    
N, M = map(int,(input().split()))
Tree = list(map(int, input().split()))
Tree.sort(reverse=True)  


H(Tree,N,M)




