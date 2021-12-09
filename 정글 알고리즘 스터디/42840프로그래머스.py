# https://programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    A = [1, 2, 3, 4, 5]
    B = [2, 1, 2, 3, 2, 4, 2, 5]
    C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    a = 0
    b = 0
    c = 0
    for i in range(len(answers)):
        if A[i % 5] == answers[i]:
            a += 1
        if B[i % 8] == answers[i]:
            b += 1
        if C[i % 10] == answers[i]:
            c += 1
    if a >= b and a >= c:
        answer = [1]
        if b == a:
            answer.append(2)
        if c == a:
            answer.append(3)
    elif b >= a and b >= c:
        answer = [2]
        if b == a:
            answer.append(1)
        if c == b:
            answer.append(3)
    elif c >= a and c >= b:
        answer = [3]
        if b == c:
            answer.append(2)
        if c == a:
            answer.append(1)
    answer.sort()
    return answer


""" 
# enumerate 사용한 사른사람 풀이

def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result



"""