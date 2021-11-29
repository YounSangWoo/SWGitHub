# https://www.acmicpc.net/problem/11047

N, M = map(int, input().split())
coin = []
for i in range(N):
    coin.append(int(input()))

count = 0
for i in range(N-1, -1, -1):
    if M-coin[i] >= 0:
        count += M//coin[i]
        M = M % coin[i]
        if M == 0:
            break

print(count)
