# https://www.acmicpc.net/problem/5639

""" 
50
30
24
5
28
45
98
52
60
 """

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

A = []
while True:
    try:
        a = input()
        A.append(int(a))
    except : break


def pretopost(A: list):
    if len(A) <= 1:
       return A
    else :
         for i in range(1,len(A)):
            if A[i] > A[0]:
                I = i
                return pretopost(A[1:I]) + pretopost(A[I:]) + [A[0]]

    return pretopost(A[1:]) + [A[0]]


ans = pretopost(A)

for i in range(len(ans)):
    print(ans[i])