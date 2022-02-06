# https://www.acmicpc.net/problem/11653
""" 문제
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

출력
N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.
 """
import sys
import math
input = sys.stdin.readline

N = int(input())
# 에라토스 테네스의 채 로 소수들을 찾는다.
def prime_num(n):
    arr = [True]*(n+1)
    prime_arr = []

    for i in range(2, int(math.sqrt(n)+1)):
        if arr[i]==True:
            j=2
            while(i*j)<=n:
                arr[i*j]=False
                j+=1
    
    for i in range(2,len(arr)):
        if arr[i] :
            prime_arr.append(i)

    return prime_arr

prime_Arr = prime_num(N)

for i in prime_Arr:
    while 1:
        A = N%i
        if A:
            break
        else:
            N = N//i
            print(i)
            

