# https://www.acmicpc.net/problem/1715

import sys, heapq 


N = int(sys.stdin.readline())
card=[]
card_sum = 0

for _ in range(N):
    A = int(sys.stdin.readline())
    heapq.heappush(card, A)

while True:
    try:
        first = heapq.heappop(card)
        second = heapq.heappop(card)

        card_sum += first+second

        heapq.heappush(card,first+second)
    except:
        break

print(card_sum)
