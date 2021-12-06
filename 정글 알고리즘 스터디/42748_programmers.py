# 배열이 들어오면 commands 에서 주어지는 범위대로 자르고 정렬후 주어진 인덱스의 원소를 출력하는 문제

def solution(array, commands):
    answer = []
    tmp = []
    for i in commands:
        tmp = array[i[0]-1:i[1]]
        tmp.sort()
        answer.append(tmp[i[2]-1])
    return answer
