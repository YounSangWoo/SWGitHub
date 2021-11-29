# https://www.acmicpc.net/problem/1931

""" 예제 입력 1
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
예제 출력 1
4
 """
import sys
input = sys.stdin.readline
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input().rstrip().split())))

graph = sorted(graph, key = lambda x:(x[1],x[0]))
count = 1
time = graph[0][1]
for i in range(1,n):
    if time<=graph[i][0]:
        time = graph[i][1]
        count +=1
    
print(count)



