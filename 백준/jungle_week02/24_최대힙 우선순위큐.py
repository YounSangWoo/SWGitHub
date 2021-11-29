# https://www.acmicpc.net/problem/11279
import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []
ans = []
for i in range(N):
    A = int(input())
    if A == 0:
        try:
            ans.append(heapq.heappop(heap)[1])
        except:
            ans.append(0)
    else:
        heapq.heappush(heap, (-A, A))


for i in range(len(ans)):
    print(ans[i])
