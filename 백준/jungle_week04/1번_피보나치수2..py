# https://www.acmicpc.net/problem/2748
""" 
문제
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

n = 17일때 까지 피보나치 수를 써보면 다음과 같다.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n이 주어진다. n은 90보다 작거나 같은 자연수이다.

출력
첫째 줄에 n번째 피보나치 수를 출력한다.

예제 입력 1
10
예제 출력 1
55 

"""
#bottom up방식
fib_array = [0, 1]

def fib_dp(n):
    if n==0:
        return print(0)
    elif n==1:
        return print(1)
    for i in range(2, n+1):
        num =  fib_array[i-2]+fib_array[i-1]
        fib_array.append(num)
    
    return print(fib_array[n])

n = int(input())
fib_dp(n)


# reculsive DP 
# 큰 숫자가 들어갈경우 recursion depth exceeded 에러가 뜬다. 
#n=10000이라면 재귀적으로 call stack의 리밋을 초과한다. 
# 탑다운방식
"""  
def fib_recur_dp(n):
    if n<len(fib_array):
        return fib_array[n]
    else:
        fib = fib_recur_dp(n-1) + fib_recur_dp(n-2)
        fib_array.append(fib)
        return print(fib)

 """

# naive한 방식 직관적이나 느리다.

""" 
def fib_naive(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else :
        fib = fib_naive(n-1) + fib_naive(n-2)
        return fib
 """