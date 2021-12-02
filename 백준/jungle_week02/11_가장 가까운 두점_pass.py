# https://www.acmicpc.net/problem/2261

import sys
input = sys.stdin.readline
n = int(input())
pl = [list(map(int,input().split()))for _ in range(n)]

pl.sort()


def getDist(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def dac(start,end):
    if start == end:
        return float('inf')

    if end - start ==1:
        return getDist(pl[start], pl[end])
    
    mid = (start+end)//2
    minDist = min(dac(start,mid),dac(mid,end))
    

    ############### 중앙에서 가까운 점이 있는지 찾음 ################
    target_pl = []
    for i in range(start, end+1):
        if (pl[mid][0]-pl[i][0])**2<minDist:
            target_pl.append(pl[i])

    target_pl.sort(key = lambda x:x[1])

    t = len(target_pl)
    for i in range(t-1):
        for j in range(i+1,t):
            if (target_pl[i][1]-target_pl[j][1])**2<minDist:
                minDist = min(minDist, getDist(target_pl[i],target_pl[j]))
            else:
                break
    return minDist

print(dac(0,n-1))
    

