""" # 실습 1c-1
name = input('이름을 입력해주세요:')
print(f'안녕하세요 {name}님')
 """

# 실습 1-2(정수의 최대값 구하기)
""" def max3(a,b,c):

    maximum = a
    if b > maximum : maximum =b
    if c > maximum : maximum =c
    return maximum
print(f'max3(1,2,3)={max3(1,2,3)}')
"""

#실습 1C-2(정수의 중앙값 구하기) 중앙값은 주어진 수를 정렬시 가장 중앙에 위치한 값으로 평균값과 헷갈리지 말자.

""" def med3(a,b,c):
    if a>=b: 
        if b>=c :
            return b
        elif a<=c :
            return a
        else :
            return c
    elif a > c:
        return a
    elif b > c :
        return c
    else : return b

print('세 정수의 중앙값을 구합니다.')
a = int(input('정수 a를 입력하세요:'))
b = int(input('정수 b를 입력하세요:'))
c = int(input('정수 c를 입력하세요:'))

print(f'중앙값은 {med3(a,b,c)} 입니다.') """

#실습1-7 1부터 n 까지 정수의 합 구하기`

""" n = int(input('n값을 입력하세요:'))
sum = 0
i=1

while i<=n:
     sum +=i
     i+=1
print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

print(f'current i : {i}') #n+ 1 이 출력됨
 """

# 1-8예제 for문으로 1부터 n 까지 정수의 합 구해보기(변수가 하나일 경우 wihle보다 for문을 사용하는 것이 좋다)
""" 
n=int(input('input n value : '))

sum = 0
for i in range(1,n+1):
    sum+=i

print(f'from 1 to {n} sum = {sum}')
print(f'current i : {i}') #n 값이 출력됨
 """
 
#가우스의 덧샘공식 nx(n+1)/2 공식으로 구하기

""" n=int(input('n 값을 입력하세요:'))
sum=n*(n+1)//2
print(f'1부터 n까지의 핪은 {sum}입니다') """

#실습 1-9 정수의 합을 구할때 1이 아닌 다른 정수로 시작한다면 range함수에 전달할 시작값 끝값을 오름차순으로정렬해야 한다.

""" print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('정수 a를 입력하세요.'))
b = int(input('정수 b를 입력하세요.'))

if a>b : # a와 b오름차순 정렬
    a,b = b,a
 
sum = 0

for i in range(a, b+1):
    sum+=i

print(f'{a}부터 {b}가지 정수의 합은 {sum}입니다.') """

# 1-10 위의 예제 합을 구하는 과정 출력해보기

""" print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('정수 a를 입력하세요.'))
b = int(input('정수 b를 입력하세요.'))

if a>b : # a와 b오름차순 정렬
    a,b = b,a
 
sum = 0

for i in range(a, b+1):

    if i<b:
        print(f'{i}+',end='')
    else : 
        print(f'{i}=',end='')
    sum+=i

print(f'{sum}') """

# 1-11 위의 예제 효율화 if 문 판단 없음 알고리즘의 효율을 높인 코딩
""" print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('정수 a를 입력하세요.'))
b = int(input('정수 b를 입력하세요.'))

if a>b : # a와 b오름차순 정렬
    a,b = b,a
 
sum = 0

for i in range(a, b):
 print(f'{i}+',end='')
 sum+=i

print(f'{b}=',end='')#for문의 반목문이 b-1번째 까지만 반복하므로 마지막b값을 한번 더 더한다.
sum+=b

print(sum) """

# + - 번갈아 연속 출력하기
""" 
print('+와 -를 번갈아 출력합니다')
n= int(input('몇 개를 출력할까요? : '))
for i in range(n):
    if i % 2 :  #홀수인 경우
        print('-',end='')
    else :
        print('+',end='')
print() """

# 1-13 위의 예제 효율화 하기
""" print('+와 -를 번갈아 출력합니다')
n= int(input('몇 개를 출력할까요? : '))
for _ in range(n//2): #n//2는 몫을 구하는 값으로 짝수일때 +- 한쌍씩 나오도록했음 for 문에 (_)를 사용한 이유는 for문에서 range()함수가 for문을 순환하며 반환하는 값을 사용할 필요가 없기 때문
    print('+-',end='')
if n%2:
    print('+',end='') #n이 홀수일때 +출력

print()
 """

#  *를 n개 출력하되 w개마다 줄바꿈하기1
""" 
n= int (input('*를 몇개 출력할까요?:'))
w= int (input('몇 개마다 줄바꿈할까요?:'))

for i in range(n):
    print('*',end='')
    if i%w == w-1:
        print()
if n%w :
    print() """

#예제 1-15 위의 예제 개선
""" n= int (input('*를 몇개 출력할까요?:'))
w= int (input('몇 개마다 줄바꿈할까요?:'))

for _ in range(n//w) : #n//w 까지 반복
    print('*'*w)
    
rest= n%w #0은 거짓 
if rest : 
    print('*'*rest)
 """

#1-16 양수만 입력받기
""" print('1부터 n까지 정수의 합을 구한다.')

while True: #while의 True 는 무한루프
    n=int(input('n값을 입력하세요'))
    if n>0:
        break #n 이 0보다 커질 때까지 반복 #n이 양수일경우 break을 반환하여 탈출

for i in range(1,n+1):
    sum+=i
   
print(f'1부터 {n}까지 정수의 합은 {sum}입니다.') """

#1-17 가로 세로 길이가 정수, 넓이는 area인 직사각형의 변의 길이 나열하기

""" area = int(input('직사각형의 넓이를 입렬하세요:'))

for i in range (1,area+1):
    if i*i>area : break #i 가 가장 긴 변의 길이가 되기때문에 
    if area % i : continue #continue 는 area 가 i로 나누어 떨어지지 않으면 for문의 다음 반복으로 진행되는것 print 넘어감 
    print(f'{i}x{area//i}') #i 가 area의 약수일때 i는 짧은변 area//i는 긴변

 """
# 1-18 10~99 n개의 난수생성하기
""" 
import random

n=int(input('원하는 난수의 개수를 입력하세요 : '))
for _ in range(n):
    r = random.randint(10, 99) #random.randit(a,b) a이상 b이하 정수 가운데 무작위로 1개를 뽑아 반환하는 함수입니다. 
    print(r,end=' ')
    if r==13:
        print('\n프로그램을 중단합니다.')
        break
else: #break이 실행되지 않았을때 실행된다.
    print('\n 난수 생성을 종료합니다.')
 """
# 1부터 12 까지 특정값(8)을 건너띄고 출력하기 
""" 
 for i in list(range(1,8)) + list(range(9,13)):
    print(i,end=' ')
print()
 """

#1c-3 2자리 양수 입력받기

""" print('2자리 양수를 입력하세요.')

while True:
    no=int(input('값을 입력하세요.:'))
    if no>=10 and no<=99: # == if 10<= no <=99
        break

print(f'입력받은 양수는 {no}입니다. ') """

##########################################
#1-21 다중루프 (구구단 곱셈표 출력하기)
#########################################
""" print('-'*27)

for i in range(1,10):
    for j in range(1,10):
        print(f'{i*j:3}',end='') #3자리수로 표현 
    print()#행 변경

print('-'*27)
 """

# 왼쪽 아래가 직각인 이등변 삼각형을 *로 출력하기
""" 
print('왼쪽 아래가 직각인 이등변 삼각형을 출력해 봅시다')
n=int(input('짧은 변의 길이를 입력하세요.:'))

for i in range(n):
    for _ in range(i+1):
        print('*',end='')
    print()

print('오른쪽 아래가 직각인 이등변 삼각형을 출력해 봅시다')
"""
p=int(input('짧은 변의 길이를 입력하세요.:'))

for i in range(p):
    for _ in range(p - i - 1):
        print(' ',end='')
    for _ in range(i + 1):
        print('*',end='')
    print()
 

 #파이썬의 은 데이터, 함수, 클래스, 모듈, 패키지 등을 객체로 취급하며 각 개체는 저장공간을 차지한다. 따라서 파이썬의 변수는 값을 갖지 않는다는 특성이 있다.
