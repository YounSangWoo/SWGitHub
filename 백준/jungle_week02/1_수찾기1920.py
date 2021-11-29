# 수 찾기 https://www.acmicpc.net/problem/1920 이진법 사용


N = int(input())
A = [None]*N
A = list(map(int, (input().split()[:N])))   # N개 이상 입력을 해도 N번째 입력까지만 A에 저장 된다.

M = int(input())
B = [None]*M
B = list(map(int, input().split()[:M]))
A.sort()
for i in B:
    pl = 0
    pr = N-1
    while True:
        pc = (pl+pr)//2
        if A[pc] == i:
            print(1)
            break
        elif A[pc] < i:
            pl = pc+1
        else:
            pr = pc-1
        if pl > pr:
            print(0)
            break
