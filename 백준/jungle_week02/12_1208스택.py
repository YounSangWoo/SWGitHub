# https://www.acmicpc.net/problem/10828 스택
""" import sys
input = sys.stdin.readline

N = int(input())

stack=[]
print_a=[]
for _ in range(N):
    word = input().split()
    word[0] = word[0]

    if word[0] =="push":
        value = word[1]
        stack.append(value)

    elif word[0] =="pop":
        if len(stack)==0:
            print_a.append(-1)
        else:
            print_a.append(stack.pop())
    elif word[0] =="size":
        print_a.append(len(stack))

    elif word[0] =="empty":
        if len(stack)==0:
            print_a.append(1)
        else : print_a.append(0)
    elif word[0]=="top":
        if len(stack)==0:
            print_a.append(-1)
        else : print_a.append(stack[-1])

for i in range(len(print_a)):
    print(print_a[i])
     """

    #  예외처리 이용
import sys
input = sys.stdin.readline


N = int(input())
stack = []
for _ in range(N):
    word = input().split()
    order = word[0]

    if order == "push":
        value = word[1]
        stack.append(value)

    elif order == "pop":
        try:
            print(stack.pop())
        except:
            print(-1)
    elif order == "size":
        print(len(stack))

    elif order == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order == "top":
        try:
            print(stack[-1])
        except:
            print(-1)
