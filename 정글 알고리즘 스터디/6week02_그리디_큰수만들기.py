
# 시간초과
""" def solution(number, k):
    answer = ''
    nlist = []
    for i in range(len(number)):
        nlist.append(number[i])

    while k:
        for i in range(0,len(nlist)-1):
            if nlist[i]<nlist[i+1]:
                k-=1
                del nlist[i]
                break
            else :
                continue
    answer = ''.join(nlist)

    return answer """


def solution(number, k):
    answer = ''
    nlist = []

    for i in range(len(number)):
        while k > 0 and nlist and nlist[-1] < number[i]:
            nlist.pop()
            k -= 1
        nlist.append(number[i])

    answer = ''.join(nlist[:len(nlist)-k])#k가 남았을 수 있음
    return answer


print(solution("98512", 4))
