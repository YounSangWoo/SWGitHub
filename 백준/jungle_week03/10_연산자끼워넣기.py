# https://www.acmicpc.net/problem/14888

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
num_list = list(map(int, input().split()))
sum, sub, mul, div = list(map(int, input().split()))
maxv = -100000000
minv = 1000000000


def calc(num: int, index: int, sum, sub, mul, div):
    global N, maxv, minv
    if (N == index):
        maxv = max(num, maxv)
        minv = min(num, minv)
        return
    else:
        if sum:
            calc(num+num_list[index], index+1, sum-1, sub, mul, div)
        if sub:
            calc(num-num_list[index], index+1, sum, sub-1, mul, div)
        if mul:
            calc(num*num_list[index], index+1, sum, sub, mul-1, div)
        if div:
            calc(int(num/num_list[index]), index+1, sum, sub, mul, div-1)

calc(num_list[0],1,sum,sub,mul,div)

print(maxv)
print(minv)
