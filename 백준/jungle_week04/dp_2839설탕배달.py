# https://www.acmicpc.net/problem/2839

N = int(input())

if not (N % 5//3):
    print(N//5 + N % 5//3)
else:
    print(-1)
