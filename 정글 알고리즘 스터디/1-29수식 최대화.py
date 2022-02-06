import re
from collections import deque


def solution(expression):
    answer = 0
    op_list = deque()
    num_list = re.split('\*', expression)

    for i in range(len(expression)):
        if expression[i] in ['+', '-', '*']:
            op_list.append(expression[i])

    print(num_list, op_list)

    return answer

print(solution("100-200*300-500+20"))