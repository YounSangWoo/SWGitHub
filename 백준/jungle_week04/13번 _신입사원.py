# https://www.acmicpc.net/problem/1946

""" 예제 입력 1
2
5
3 2
1 4
4 1
2 3
5 5
7
3 6
7 3
4 2
1 4
5 7
2 5
6 1
예제 출력 1
4
3 """

import sys
input = sys.stdin.readline

test = int(input())

for i in range(test):
    N = int(input())
    newface = []
    for j in range(N):
        newface.append(list(map(int,input().rstrip().split())))
    
    newface = sorted(newface, key=lambda x: x[0])
    count = 1
    A = newface[0][1]
    for k in range(N-1):
        if A>newface[k+1][1]:
            count+=1
            A = newface[k+1][1]
    print(count)



