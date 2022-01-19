from audioop import reverse
from collections import deque
def solution(info, query):
    answer = []
    info_list = [[None] for _ in range(len(info))]
   
    for i in range(len(info)):
        info_list[i] = list(map(str,info[i].split()))
        info_list[i][-1] = int(info_list[i][-1])

    info_list.sort(key = lambda x : x[-1],reverse=True)

    def find(s):
            c = []
            count = 0
            tmp = deque()
            for i in range(len(info_list)):
                tmp.append(info_list[i])
            c = list(map(str,s.split()))
            score = int(c[-1])

            for i in range(len(c)-1):
                if c[i] != 'and' and c[i] != '-':
                    N = len(tmp)
                    for _ in range(N):
                        k = tmp.popleft()
                        if c[i] in k:
                            tmp.append(k)
            for k in tmp:
                if k[-1]>=score:
                    count +=1
            return count

    for i in range(len(query)):
        answer.append(find(query[i]))

    return answer
   
"""     def find(s):
        c = []
        count = 0
        tmp = deque()
        for i in range(len(info_list)):
            tmp.append(info_list[i])
        c = list(map(str,s.split()))
        score = int(c[-1])

        for i in range(len(c)-1):
            if c[i] != 'and' and c[i] != '-':
                N = len(tmp)
                for _ in range(N):
                    k = tmp.popleft()
                    if c[i] in k:
                        tmp.append(k)
        for k in tmp:
            if k[-1]>=score:
                count +=1
        return count """

""" 정확성  테스트
테스트 1 〉	통과(0.15ms, 10.5MB)
테스트 2 〉	통과(0.15ms, 10.5MB)
테스트 3 〉	통과(0.91ms, 10.5MB)
테스트 4 〉	통과(10.23ms, 10.5MB)
테스트 5 〉	통과(28.83ms, 10.6MB)
테스트 6 〉	통과(69.97ms, 10.6MB)
테스트 7 〉	통과(32.38ms, 10.8MB)
테스트 8 〉	통과(149.75ms, 12.5MB)
테스트 9 〉	통과(184.78ms, 12.8MB)
테스트 10 〉	통과(149.30ms, 12.8MB)
테스트 11 〉	통과(41.75ms, 10.6MB)
테스트 12 〉	통과(67.40ms, 10.7MB)
테스트 13 〉	통과(34.47ms, 10.8MB)
테스트 14 〉	통과(145.24ms, 11.4MB)
테스트 15 〉	통과(143.80ms, 11.4MB)
테스트 16 〉	통과(28.82ms, 10.6MB)
테스트 17 〉	통과(92.85ms, 10.7MB)
테스트 18 〉	통과(176.03ms, 11.4MB)
효율성  테스트
테스트 1 〉	실패(시간 초과)
테스트 2 〉	실패(시간 초과)
테스트 3 〉	실패(시간 초과)
테스트 4 〉	실패(시간 초과) """

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))