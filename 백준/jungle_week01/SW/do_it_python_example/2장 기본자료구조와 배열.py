# 리스트와 언팩
""" x=[1,2,3]
a,b,c=x
print(a)
print(b)
print(c)
print(a, b, c) """

# 2-2 78page 시퀀스 원소의 최댓값 출력하기

""" from typing import Any, Sequence #Any는 제약없는 임의의 자료형을 의미한다, Sequence는 시퀀스형을 의미한다.

def max_of(a: Sequence) -> Any: #건네받은 a의 자료형은 시퀀스형이며 반환값은 임의의 자료형이다.

    # 시퀀스형 a원소의 최댓값을 반환"
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

if __name__=='__main__': #__name__ 모듈이름(2장 기본자료구조와 배열) 이지만 최초로 실행된 스크립트 파일의 __name__에는 __main__ 이 들어가기때문에 참으로 판별 if를 실행한다.
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하세요.:'))
    x=[None]*num #원소 수가 num개인 리스트 생성 

    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요.:'))
    
    print(f'최댓값은{max_of(x)}입니다.')

 """

#  2-4 배열의 원소값을 난수로 결정하기

""" import random
from max import max_of

print('난수의 최댓값을 구한다.')

num = int(input('난수의 개수를 입력하시오.:'))
lo = int(input('난수의 최솟값을 입력하시오:'))
hi = int(input('난수의 최댓값을 입력하시오:'))

x = [None]*num

for i in range(num):
    x[i] = random.randint(lo, hi) #lo 이상 hi이하인 정수형 난수 반환

print(f'{(x)}')
print(f'이 가운데 최댓값은 {max_of(x)}입니다.') """

# 2C-1 리스트의 모든 원소를 스캔하기(원소 수를 미리 파악)
 
""" x=['snagwoo', 'Gorge', 'Yujin']

for i in range(len(x)):
    print(f'x[{i}] ={x[i]}')


y=['snagwoo', 'Gorge', 'Yujin']

for i, name in enumerate(x):         #enumerate() 함수는 인덱스와 원소를 짝찌어 튜플로 꺼내는 내장함수이다. 
    print(f'x[{i}] ={x[i]}')
 """

# 2-4 리스트 역순으로 정렬하기

""" x=[1,2,3]
x.reverse() #리스트 x의 원소를 역순으로 정렬
print(x)

y=list(reversed(x)) #다시 역순으로 정렬해 y로 참조
print(y) 

# 리스트 값의 위치(인덱스)찾기 """

""" x=[1,2,3,5,6,7]
print(x.index(3)+1) #단순히 인덱스만 찾으면 0부터 시작해서 1이 작음 """

# 2-7기수 변환(10진수 정숫값을 받아 2~32진수로 변환출력하기)

""" 
def card_conv(x:int,r:int)->str : #정수형 x를 입력받아 r로 변환하고 그 수를 문자열로 반환한다.

    d='' #변환 후의 문자열
    dchar = '0123456789ABCEEFGHIJKLMNOPQRSTUVWXYZ'

    while x>0: #x가 0이 될때까지 반복
        d += dchar[x % r] #해당하는 문자를 꺼내 결합
        x//=r #x를 r로 나눈값을 x에 저장 (x가 r보다 작아지면 나누었을때 0.xxr가되어 0반환)

    return d[::-1] #역순으로 반환

if __name__=='__main__':
    print('10진수를 n진수로 변환합니다.')

    while True: #무한루프
        while True : #음이아닌 정수입력
            no=int(input('변환할 값으로 음이 아닌 정수를 입력하시오.:'))
            if no>0:
                break
        
        while True: #2~36진수의 정수값을 입력받음
            cd = int(input('어떤 진수로 변환할까요?:'))
            if 2 <= cd <= 36:
                break
        
        print(f'{cd}진수로는 {card_conv(no,cd)}입니다.') #no=x, cd=r

        retry = input("한 번 더 변환할까요?:(Y--예/N--아니오):") 
        if retry in {'N', 'n'}:
            break 
"""
#2-9 1000이하의 소수 나열하기 (알고리즘 개선)

""" 
counter = 0 #나눗셈 카운트
ptr = 0 #이미 찾은 소수의 개수
prime = [None]*500 # 소수를 저장하는 배열

prime[ptr] = 2 #2는 소수이므로 초깃값 저장

ptr+=1

for n in range(3, 1001, 2): #홀수만을 대상으로 설정 3~1001까지 2씩 증가
    for i in range(1,ptr): # 이미 찾은 소수로 나누기
        counter += 1
        if n % prime[i] ==0: #prime[0]은 2라는 소수가 있으니 2로 우선 나눔
            break
    else :
        prime[ptr]=n #소수로 배열에 등록
        ptr += 1
    
for i in range(ptr): #ptr의 소수를 출력
    print(prime[i])
print(f'나눗셈 실행한 횟수 : {counter}')
 """

 #2-10 1000 이하의 소수 나열 알고리즘 개선

""" counter = 0 #나눗셈 카운트
ptr = 0 #이미 찾은 소수의 개수
prime = [None]*500 # 소수를 저장하는 배열

prime[ptr] = 2 #2는 소수이므로 초깃값 저장

ptr+=1

prime[ptr] = 3 #2는 소수이므로 초깃값 저장

ptr+=1

for n in range(5,1001,2):
    i=1
    while prime[i] *prime[i]<=n:
        counter +=2
        if n%prime[i]==0:
            break
        i+=1
    else :
        prime[ptr]= n
        ptr += 1
        counter += 1
for i in range(ptr):
    print(prime[i])
print(f'곱셈과 나눗셈을 실행한 횟수 : {counter}')

 """
N=5

for i in range(0,N,-1):
    print(' ',end='')
    for i in range(N)
