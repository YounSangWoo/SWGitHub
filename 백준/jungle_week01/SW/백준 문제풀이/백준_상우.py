""" import sys
input = sys.stdin.readline """

# 1번 2557 문제
""" print('Hello World!') """

# 2번 10869 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.
# 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)

"""
A, B = input().split() #split 으로 a와 b를 한번에 입력받을경우 나누어 저장
A = int(A)
B = int(B)

print(A+B, A-B, A*B, A//B, A%B, sep='\n') #sep \n 으로 줄바꾸어 표기
"""

# 3번 2558 (첫재 줄에 세자리 자연수 둘째줄에 세자리 자연수가 주어질때 각 세자리 곱셈의 연산과정 보여주기)
"""
A=int(input()) #입력값을 정수로 저장
B=str(input()) #입력값을 문자열로 저장
#문자열인 B를 int형으로 변환하여 A와 곱한다.
print(A*int(B[-1]), A*int(B[-2]), A*int(B[-3]), A*int(B), sep='\n')
 """

# 4번 9498 (시험성적)

"""
A= int(input())

if 100>=A>=90:
    print('A')
elif 89>=A>=80:
    print('B')
elif 79>=A>=70:
    print('C')
elif 69>=A>=60:
    print('D')
else :
    print('F')

 """

# 5번 2753(윤년)

"""
year=int(input())

if ((year%4==0)and(year%100 != 0))or(year%400==0):
    print(1)
else: print(0)

"""
# 6번 1085(직사각형 탈출)

""" x, y, w, h = input().split()
x = int(x)
y = int(y)
w = int(w)
h = int(h)
a = (w-x)
b = (h-y)

short_box = [x, y, w, h, a, b]

short = min(short_box)
print(short) """

# 7번 2739(구구단)

""" N=int(input())
for i in range(1,10):
    print(f'{N} * {i} = {N*i}') """


# 8번 10950(A+b-3) 두 정수를 입력받아 덧셈 표현

""" N = int(input())
A=[None]*N
B=[None]*N
for i in range(N):
    a, b=input().split()
    a=int(a)
    b=int(b)
    A[i]=a
    B[i]=b

for i in range(N):
    print(A[i]+B[i])
 """
# 9번 2438 별찍기

""" N=int(input())

for i in range(N):
    for _ in range(i+1):
     print('*',end='')
    print() """

# 10번 10871 x보다 작은수 찾기
"""
N, X = map(int,input().split())
L = list(map(int,input().split())) #list(map(함수, 리스트)

for i in range(N):
    if L[i] <X:
        print(L[i],end=' ')
 """

# 11번 8958 최댓값 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오

""" from typing import Sequence

def max(a:Sequence):

    maximum = a[0]

    for i in range(1, len(a)):
        if a[i]>maximum:
            maximum = a[i]
    return maximum

A=[None]*9

for i in range(9):
    A[i]=int(input())

print(max(A), A.index( max(A) )+1, sep='\n') """

# 12번 8958 ox퀴즈
"""
N=int(input())
test=[None]*N

def OXscore(A):
    a=len(A)
    i=0
    Ocount = 0
    score =0

    while i<=a-1:
     if A[i]=='O':
        Ocount +=1
        score += Ocount
        i += 1
     else:
        Ocount = 0
        i+= 1
    return score

for i in range(N):
   test[i]=input('')
for i in range(N):
    print(OXscore(test[i]))

 """

# 13번 4344 평균은 넘겠지

""" cls = int(input())
SCORE = [None]*cls

for i in range(cls):
    SCORE[i]=list(map(int,input().split()))

def avg(a):
    sum =0
    for i in range(1,len(a)):
        sum += a[i]

    average=sum/a[0]

    return average
def per(a):
    count=0
    for i in range (1,len(a)):
        if a[i]>avg(a):
            count+=1
    percentage = round(count/a[0]*100,3)
    return percentage

for i in range(cls):
 print(f'{format(per(SCORE[i]),".3f")}%')
 """

# 14번 2577 숫자의 개수

""" a=int(input())
b=int(input())
c=int(input())

# 숫자를 문자열로 쪼개기
D=list(str(a*b*c))
# print(a*b*c)
# print(D[0])
N=['0','1','2','3','4','5','6','7','8','9']
n=0
while n<10:
    count = 0
    for i in range(len(D)):
         if D[i]==N[n]:
             count+=1
    else:
        print(count)
        n+=1
 """

# 15번 15596번 정수 N개의 합
"""
a = [1,2,3]

def solve(a: list) -> int:
    sum=0
    for i in range (len(a)):
        sum += a[i]
    return sum

print(solve(a)) """

# 16번 11654 아스키코드
"""
n = input()
print(ord(n)) #ord() 입력된 문자를 아스키 코드값으로 반환, chr() 아스키코드를 문자로 반환
 """

# 17번 2675 문자열 반복

""" case = int(input())
test = [None]*case

for i in range (case):
    test[i] = list(input().split())
    test[i][0]=int(test[i][0]) #split으로 나누면 숫자도 str로 들어가기때문에 int로 해당위치 변경

for n in range(case):
    a=len(test[n][1])

    for i in range(a-1):

        print(test[n][1][i]*test[n][0],end='')
    else: print(test[n][1][(a-1)]*test[n][0], sep='\n')
 """

# 18번 1152번 단어의 개수

""" a=input().split()
print(len(a))
 """

# 19번 2908번 상근이동생 상수

"""

a,b=input().split()
a=int(a[::-1])
b=int(b[::-1])

if a>b:
    print(a)
else :
    print(b)

"""

# 20번 2869 달팽이는 올라가고 싶다.

"""
A, B, V = map(int,input().split())
a = (V-A)%(A-B)
b = (V-A)//(A-B)

if(a==False):
    print(b+1)
else:
    print(b+2)     """

# 21번 1987번 소수찾기
"""

n = int(input())
y=list(map(int,input().split()))
count = 0

def prime(a):
    if a==1:
        return False
    for i in range(2,a):
        if a%i == 0 :
           return False
    else: return True


for i in range(n):
    if prime(y[i])==True:
        count +=1
print(count) """


# 리스트 안에서 값의 갯수를 찾기
""" x = [1, 1, 2, 4, 5, 6, 6, 6, 7, 6, 7, 8, 9]
y = [6,7,1]
print()
count = 0
for i in range(len(y)):
    a=x.count(y[i])
    if a != 0:
     count += a
print(count) """

# 22 9020 골드바흐의 추측 https://www.acmicpc.net/problem/9020


"""

def prime(p):
    if p==1:
        return False
    for i in range(2,p):
        if p%i==0:
            return False
    return True

a = int(input())
even = list(int(input().strip()) for _ in range(a)) #list 에  a개 만큼 int형 값을 저장


for i in even:
    x=i//2
    y=i//2
    while True:
        if prime(x) and prime(y) :
           break
        else :
            x-=1
            y+=1
    print(x,y)
 """

# 23번 한수 https://www.acmicpc.net/problem/1065

"""


def hansu(N):
    count = 0

    for i in range(1, N+1):
        n = list(map(int, str(i)))

        if 1 <= i < 100:
            count += 1
        elif n[1] == (n[2]+n[0])/2:
            count += 1
    return count


N = int(input())
print(hansu(N))
 """

# 24번 종이자르기 https://www.acmicpc.net/problem/2628
"""
def max(a:list):
    max =0
    for i in range(1, len(a)):
        if a[i]-a[i-1]>max:
            max = a[i]-a[i-1]
    return max

x,y= map(int,input().split())
N = int(input())
X = [0, x] #가로
Y = [0, y] #세로

for i in range (N):
    a=list(map(int,input().split()))
    if a[0] == 0 :
        Y.append(a[1])
    else :
        X.append(a[1])

X.sort()
Y.sort()

print(max(X)*max(Y)) """

# 25번 팩토리얼https://www.acmicpc.net/problem/10872


""" def fac(a: int):
    n = 1
    c = 1
    if a == 0:
        n = 1
    else:
         for i in range(1,a+1):
            n*=i
    return n


a = int(input())
print(fac(a))
 """

# 재귀함수로 구하기 재귀함수의 예를 들뿐 효율적이진 않다.
"""
def fac(n:int)->int:
    if n>0:
        return n*fac(n-1)
    else:
        return 1

n= int(input())
print(fac(n)) """

# 26번 하노이 탑 https://www.acmicpc.net/problem/1914
"""

def move(N, x, y):

    if N > 1:
        move(N-1, x, 6-x-y)

    print(f'{x} {y}')

    if N > 1:
        move(N-1, 6-x-y, y)


N = int(input())
count = 2**N - 1
print(count)

if N <= 20:
    move(N, 1, 3)

 """
# 27번 N-Queen https://www.acmicpc.net/problem/9663
"""
N=int(input())

pos = [0]*N  #각 열에 배치한 퀸의 위치
flag_a = [False]*N #각 행에 퀸 배치 체크
flag_b = [False]*(N*2-1) #오른위아래 대각선 배치 체크
flag_c = [False]*(N*2-1) #왼쪽위아래 대각선 배치 체크
count = 0

def set(i:int)->None:
    global count

    for j in range(N): #0행부터 놓는다.   # i 열 j 행
        if(not flag_a[j] and not flag_b[j+i]and not flag_c[i-j+(N-1)]):   #행이 비어 있다면 True가 아니라면?
            pos[i] = j
            if i ==(N-1):
                count+=1
            else:
                flag_a[j] = flag_b[j+i] = flag_c[i-j+(N-1)] = True
                set(i+1) #다음열에 퀸 배치
                flag_a[j] = flag_b[j+i] = flag_c[i-j+(N-1)] = False

set(0)
print(count) """


""" def promising(i):
    for j in range(0, i):
        # 새로운 퀸과 기존의 퀸이 같은 행에 있거나 대각선에 있을 경우
        if row[j] == row[i] or abs(row[j]-row[i]) == (i-j):
            return False
    return True


def N_queen(i):
    global count
    if i == N:
        count += 1
    else:
        for j in range(N): #i열 0행부터 N-1행까지 퀸 배열
            row[i] = j
            if promising(i):
                N_queen(i+1)


N = int(input())
row = [0]*(N*2-1)
count = 0
N_queen(0)
print(count) """
# 28번 Z https://www.acmicpc.net/problem/1074
""" N,r,c=map(int,input().split())

def Z(s,N,r,c):

    size = 2**(N-1)

    if N==0:
        return s
    return Z( s + ( (r//size)*2 + (c//size) ) * pow(4,N-1)
    ,N-1
    ,r%size
    ,c%size)

print(Z(0,N,r,c))  """

# 29번 수 정렬하기 https://www.acmicpc.net/problem/2750
""" n= int(input())
a=[None]*n

for i in range(n):
    a[i]=int(input())

a = sorted(a)
for i in range(n):
    print(a[i])
 """


""" import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline



def Qsort(a:list,lt, rt):
    pl =lt
    pr = rt
    x = nums[(lt+rt)//2] #Pivot

    while pl<=pr: # pl 이 pr보다 커지거나 같아질 떄는 피벗을 기준으로 정렬이 끝났음을 의미
        while a[pl] < x :
            pl+=1
        while a[pr] > x :
            pr-=1
        if pl<=pr:
            a[pl],a[pr]=a[pr],a[pl]  #pr 은  피벗보다 작아지면서 끝났을것이고 pl 은 피벗보다 커지면서 끝났을것이다.
            pl+=1 #피벗보다 작은값이 기존 pl에 들어갔으므로 그 다음 인덱스로 검색
            pr-=1

    if lt<pr : Qsort(a,lt,pr)  #피벗을 기준 왼쪽과 오른쪽을 똑같이 또 정렬반복
    if pl < rt : Qsort(a,pl,rt)


n = int(input())
nums = list(int(input()) for _ in range(n))

Qsort(nums,0,n-1) #퀵정렬을 이용 정렬
for i in nums:
    print(i) """

# 30번 수 정렬하기2 https://www.acmicpc.net/problem/2751 쉘 사용
"""
def shell(a:list):

    n=len(a)
    h=n//2
    while h>0:
        for i in range(h,n):
            j=i-h
            tmp = a[i]
            while j>=0 and a[j] > tmp :
                a[j +h] = a[j]
                j-=h
            a[j+h] = tmp
        h//=2


x=int(input())
a = [None]*x

for i in range(x):
    a[i] = int(input())

shell(a)
for i in range(x):
    print(a[i]) """


# 31번 수 정렬하기3 https://www.acmicpc.net/problem/10989 도수정렬 후명이꺼 참조
"""

N = int(input())
a = [0] * 10001
for i in range(N):
    b = int(input().strip())
    a[b] += 1 #입력과 동시에 해당 위치에 카운트

for j in range(10001):
    if a[j]: #j번째에 숫자가 있다면?
        for k in range(a[j]): #해당위치가 카운트 된 수만큼 반복하여 프린트
            print(j + 1) #다시 숫자로 변환

 """

# 32번 단어정렬 https://www.acmicpc.net/problem/1181
"""

def lensort_char(a:list):
    a.sort()
    n=len(a)

    for i in range(1,n):
        j=i
        tmp = a[j] #문자의 길이
        while j>0 and len(a[j-1]) > len(tmp): #앞의 수가 뒤의 수보다 크다면?
                a[j]=a[j-1] #뒤의를 앞의수로 바꾸고
                j-=1
                a[j]=tmp #앞자리의 수는 미리 빼두었던 뒷자리수로 바꾼다.

    for i in range(n-1):
        if a[i] != a[i+1]:
            print(a[i])

    print(a[n-1])


n=int(input().strip())
a=[None]*n

for i in range(n):
    a[i]=str(input().strip())

lensort_char(a)

 """
# 함수이용
""" a=set(a) #set 은 단순히 리스트를 set으로 바꿔줄 뿐
a=list(a)
a.sort(key=len)
 """
""" for i in range(len(a)):
    print(a[i]) """
# 33번 일곱난쟁이 https://www.acmicpc.net/problem/2309
# 백설공주에게 위기가! 일과를 마치고 돌아온 난쟁이가 아홉명?? 일곱난쟁이의 키의합은 100이다. 난쟁이를 찾아라

""" a=[None]*9

for i in range(9):
    a[i]=int(input().strip())

Spyheight_sum = int(sum(a)-100)

def findspy(a:list)->None:
    n=9
    while n>=2:
        for i in range(n-1):
            if (a[n-1]+a[i])==Spyheight_sum: #9번째 난쟁이를 첫번째 난쟁이부터 더해본다.
                a.pop(n-1)
                a.pop(i)
                return
        else : n-=1

    return


findspy(a)
a.sort()

for i in range(7):
    print(a[i]) """

# 34번 차이를 최대로 https://www.acmicpc.net/problem/10819
# N개의 정수로 이루어진 배열 A, 이 안에 들어있는 정수의 순서를 적절히 바꿔 인접한 수끼리의 차이의 절댓값을 최대로?

""" 
from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

B = list(permutations(A))
for i in range(len(B)):
    a=0
    for n in range(N-1):
        a += abs(B[i][n]-B[i][n+1])
    B[i]=a

print(max(B))

"""

# 35번 외판원 순회 https://www.acmicpc.net/problem/10971
""" 
import sys
input = sys.stdin.readline

def dfs(start, next, value, visited:list):
    global cost

    if len(visited)==N:
        if Route[next][start] !=0:
            cost = min(cost, value + Route[next][start])
        return
    
    for i in range(N):
        if Route[next][i] != 0 and i != start and i not in visited:
            visited.append(i)
            dfs(start, i, value + Route[next][i], visited)
            visited.pop()

N = int(input().strip())
Route = [None]*N
cost = sys.maxsize
for i in range(N):
    Route[i]=list(map(int,input().strip().split()))

for i in range(N):
    dfs(i, i, 0, [i])

print(cost)
    
"""
# 36 안전영역 https://www.acmicpc.net/problem/2468
from collections import deque
import sys
input = sys.stdin.readline


N = int(input().strip())
area = []
max_rain = 0

for i in range(N):
    area.append(list(map(int, input().rstrip().split())))

for i in range(N):
    for j in range(N):
        if area[i][j] > max_rain:
            max_rain = area[i][j]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, visit,rain):
    q = deque()
    q.append((x, y))
    visit[x][y] = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= ny < N and 0 <= nx < N and not visit[nx][ny]:
                if area[nx][ny] > rain:
                    q.append((nx, ny))
                    visit[nx][ny] = 1


maxarea = -sys.maxsize
for i in range(max_rain-1, -1, -1):
    visit = [[0]*(N) for _ in range(N)]
    safearea = 0
    for j in range(N):
        for k in range(N):
            if visit[j][k] == 0 and area[j][k] > i:
                bfs(j, k, visit, i)
                safearea += 1
    maxarea = max(maxarea, safearea)

print(maxarea)
