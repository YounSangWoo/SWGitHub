# https://programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    candi_list = []
    answer = []
    A = brown+yellow
    for i in range(1, A+1):
        if A % i == 0 and i >= A//i:
            candi_list.append([i, A//i])

    for i, j in candi_list:
        if((2*i)+(2*j-4) == brown):
            answer = [i, j]
        break

    return answer
