from collections import deque

answer = ''
def solution(p):
#     '('=40  ')'=41
    p = deque(map(ord, p))
# "(()())()"
# [40, 40, 41, 40, 41, 41, 40, 41]

    def great(p):
        if p[0] == 40 and p[-1] == 41:
            return True
        return False

    def re(p):
        global answer
        u = deque()
        if not p:
            t = ''
            return t
      
        while True:
            for _ in range(2):
                u.append(p.popleft())
            if sum(u) % 81 == 0:  # 균형
                break

        if great(u):  # 올바르다면?
           
            answer = ''.join(list(map(chr, u)))+re(p)
            return answer

        else:  # 올바르지 않다면?
            tmp = ''
            tmp = ('('+ re(p) + ')')
            u.pop()
            u.popleft()
            for i in range(len(u)):
                if u[i] == 40:
                    u[i] = 41
                else:
                    u[i] = 40
            answer = tmp +''.join(list(map(chr, u)))  # 바꿔줘서 추가
            return answer
     
    re(p)

    return answer


# print(solution("))()(("), "result = ()()()")
# print(solution("(()())()"), "result = (()())()")
print(solution("()))((()"), "resutlt = ()(())()")
