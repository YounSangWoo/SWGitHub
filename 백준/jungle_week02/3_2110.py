""" 도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.

도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다.
최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고
가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

C개의 공유기를 N개의 집에 적당히 설치해서, 
가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

입력
첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 
둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.
5 3
1
2
8
4
9

                                                              


출력  : 첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.
3
힌트 
공유기를 1, 4, 8 또는 1, 4, 9에 설치하면 가장 인접한 두 공유기 사이의 거리는 3이고, 이 거리보다 크게 공유기를 3개 설치할 수 없다.


아이디어 :

home의 처음과 끝의 의 길이를 재고 = H
초기 공유기의 설치 간격(dist)은 H(N/2-1) 로 잡는다.

처음 간격(dist) 간격으로 공유기를 설치하며 공유기 설치 갯수보다 적게 설치될 경우  mid/2 


 """

#  3번https://www.acmicpc.net/problem/2110
import sys
input = sys.stdin.readline


def dist_router(N,c,home):
    pl = 1
    pr = home[N-1]
    curmax = 0
    before = home[0]
    c-=1 #공유기 하나는 무조건 설치되어있다고 가정

    while pl<=pr:
        cp = (pl+pr)//2
        count = 0
        before = home[0]
        for i in range(1,N):            
            if home[i]-before>=cp : 
                count+=1
                before = home[i]
                
        if count >= c:
            curmax = max(curmax,cp)
            pl = cp+1
        else :
            pr = cp-1

    print(curmax)


N, c = map(int, (input().split()))
home = []

for i in range(N):
    home.append(int(input()))
home.sort()
# print(home)
dist_router(N,c,home)        


