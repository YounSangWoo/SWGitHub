# https://www.acmicpc.net/problem/11054
""" 예제 입력 1
10
1 5 2 1 4 3 4 5 2 1
예제 출력 1
7
 """
N = int(input())
array = list(map(int,input().split()))

dp1 = [0]*N
dp2 = [0]*N
for i in range(N):
    for j in range(i):
        if array[i] > array[j] and dp1[j]>dp1[i]:
            dp1[i] = dp1[j]
    dp1[i] = dp1[i]+1

for i in range(N-1,-1,-1):
    for j in range(N-1,i,-1):
        if array[i] > array[j] and dp2[j] > dp2[i]:
            dp2[i] = dp2[j]
    dp2[i] = dp2[i]+1

# print(dp1, dp2)
dpsum = []

for i in range(N):
    dpsum.append(dp1[i]+dp2[i])

print(max(dpsum)-1)