import itertools
def solution(numbers):
    a = numbers
    b =[]
    c = set()
    for i in range(1,len(a)+1):
        b = (list(map(''.join,itertools.permutations(a,i))))
        for i in b:
            c.add(int(i))
    
    answer = 0
    for i in c:
        if i>1:
            #for문에서 break가 발생하지 않았을 경우”의 동작을 else문에 적어주는 것
            #자기자신 이외에 나누어지는 수가 발생하면 소수가 아님(break) 이 경우가 아니라면 -> 소수
            for j in range(2,i):
                if i%j == 0:
                    break
            else: answer +=1

    return answer