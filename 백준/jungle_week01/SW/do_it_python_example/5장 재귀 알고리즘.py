# 5-2 유클리드 호재법 gcd 최대공약수 구하기

""" def gcd(x:int,y:int)->int:
    if y==0:
        return x
    else :
        return gcd(y,x%y)

x,y = map(int,input().split())

print(gcd(x,y))
 """

# 5-3 하노이탑

""" def move(N, x, y):

    if N > 1:
        move(N-1, x, 6-x-y)

    print(f'{x} {y}')

    if N > 1:
        move(N-1, 6-x-y, y)


N = int(input())

print(move(N, 1, 3,))
 """

 # 5-9 8-Queen

pos = [0]*8  #각 열에 배치한 퀸의 위치
flag_a = [False]*8 #각 행에 퀸 배치 체크
flag_b = [False]*15 #오른위아래 대각선 배치 체크
flag_c = [False]*15 #왼쪽위아래 대각선 배치 체크
""" 
def put()->None:
    #각 열에 배치한 퀸의 위치 출력#
    for i in range(8):
        print(f'{pos[i]:2}', end=''})
    print()
 """
def put()->None:
    for j in range(8):
        for i in range(8):
            print('O' if pos[i]== j else 'x', end='')
        print()
    print()

def set(i:int)->None:
    #i 열의 알맞은 위치에 퀸 배치"

    for j in range(8):
        if(not flag_a[j] and not flag_b[j+1]and not flag_c[i-j+7]):
            pos[i] = j
            if i ==7:
                put()
            else:
                flag_a[j] = flag_b[i+j] = flag_c[i-j+7] = True
                set(i+1) #다음열에 퀸 배치
                flag_a[j] = flag_b[i+j] = flag_c[i-j+7] = False

set(0)