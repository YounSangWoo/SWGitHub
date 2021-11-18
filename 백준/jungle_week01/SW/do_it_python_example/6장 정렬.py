#6-1 버블 정렬 알고리즘 구현
""" from typing import MutableSequence

def bubble_sort(a:MutableSequence)->None:
    n=len(a)

    for i in range(n-1):
        exchange = 0
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                exchange +=1
        if exchange == 0:
            break


if __name__=='__main__':
    print('버블 정렬을 수행합니다.')
    
    num=int(input('원소 수를 입력하세요.: '))

    x=[None]*num #원소 수가 num 인 배열을 생성

    for i in range(num):
        x[i]=int(input(f'x[{i}]:'))
    
    bubble_sort(x)

    print('오름차순으로 정렬했습니다.')

    for i in range(num):
        print(f'x[{i}] = {x[i]}') """

#6-11퀵 정렬 알고리즘 (재귀적)
""" 
from typing import MutableSequence

def qsort(a : MutableSequence, left:int, right:int) ->None:

    pl = left
    pr = right
    x= a[(left + right)//2] #피벗(가운데 원소)

    while pl<=pr:
        while a[pl] < x : pl+=1
        while a[pr] > x : pr-=1

        if pl<=pr:
            a[pl],a[pr]=a[pr],a[pl]
            pl+=1
            pr-=1
    #위의 반복문을 마친 pr은 반을 넘어온 (left + right)//2-1의 값 pl은 반대로 반을 넘은값
    if left<pr : qsort(a,left,pr) # 좌우 각 그룹을 다시 나누기 위해 재귀호출
    if pl<right: qsort(a,pl,right)

def quick_sort(a:MutableSequence)->None:
    qsort(a,0,len(a)-1)


if __name__ == '__main__':

    num = int(input('원소 수를 입력하세요.: '))

    x = [None]*num  # 원소 수가 num 인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]:'))

    quick_sort(x)

    print('오름차순으로 정렬했습니다.')

    for i in range(num):
        print(f'x[{i}] = {x[i]}')

 """

 #6-17 도수 정렬 알고리즘

import sys
input = sys.stdin.readline


def fsort(a:list , max:int):

    n=len(a) #정렬할 배열
    f=[0] * (max +1) #누적 도수 분포표 배열
    b=[0] * n #작업용배열

    for i in range(n): f[a[i]] +=1
    for i in range(1,max+1): f[i]+=f[i-1]
    for i in range(n-1,-1,-1):
        f[a[i]] -=1
        b[f[a[i]]] = a[i]
    for i in range(n): a[i]=b[i]


def count_sort(a:list):
    fsort(a,max(a))



N = int(input())
x = [None]*N

for i in range(N):
    while True:
        x[i] = int(input())
        if x[i]>=0:
            break

count_sort(x)

for i in range(len(x)):
    print(x[i])

 

"""  import sys

N = int(sys.stdin.readline())
a = [0] * 10000
for i in range(N):
    b = int(sys.stdin.readline().rstrip())
    a[b - 1] += 1

for j in range(10000):
    if a[j]:
        for k in range(a[j]):
            print(j + 1) """