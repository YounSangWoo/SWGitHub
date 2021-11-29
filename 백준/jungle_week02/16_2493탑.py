# https://www.acmicpc.net/problem/2493 탑
""" 
import sys
input = sys.stdin.readline


N = int(input())
top = list(map(int,input().split()))

A=[]
while N>0:
    a = top.pop()
    N-=1
    n = len(top)
    for i in range(n-1,-1,-1):
        if a<top[i]:
           A.append(i+1)
           break
        elif i==0:
            A.append(0)

A.append(0)


for i in range(len(A)-1,-1,-1):
    print(A[i],end=' ')

시간초과...
 """
""" import sys
input = sys.stdin.readline


N = int(input())
top = list(map(int, input().split()))
ans = [0]*N
A = []

for i in range(N):
    while len(A)>0 and top[A[-1]]<=top[i]:
        A.pop()

    if len(A)>0:
        ans[i] = A[-1]+1
    else:
        ans[i]=0
    A.append(i)

print(" ".join(map(str,ans)))
    
 """
from math import inf

def sol(ht) :
    ht.insert(0, inf)
    st = [0]
    res = []
    for i in range(1, len(ht)) :
        while ht[st[-1]] <= ht[i] :
            st.pop()
        res.append(st[-1])
        st.append(i)
    ht.pop(0)
    return res

n = int(input())
ht = [int(x) for x in input().split()]
res = sol(ht)
print(' '.join(str(x) for x in res))

