# https://www.acmicpc.net/problem/2504 괄호의 값

import sys
input = sys.stdin.readline


def Bra(A:list):
    S = []
    S.append(A[0])
    ans = 0
    mul = 0
    
    
    if A[0][0] == ')'or A[0][0] == ']'or A[len(A)-1][1]=='(' or A[len(A)-1][1]=='[':
        return 0


    j = 1
    while j<len(A):

        for i in range(j-1,len(S)):
            if S[i][0]==A[j][0]:
                S.append(A[j])
                j+=1
            
            elif S[i][1]==A[j][1] or S[i-1][0]==2: 
                S.pop()
                
                if A[i][1]==2:
                    S.append([2,2])
                elif A[i][1]==3:
                    S.append([2,3])

        
A = []
bracket = input().strip()
S = list(bracket)

for i in S:
    if i == '(':
        A.append([0, 2])
    elif i == ')':
        A.append([1, 2])
    elif i == '[':
        A.append([0, 3])
    elif i == ']':
        A.append([1, 3])
