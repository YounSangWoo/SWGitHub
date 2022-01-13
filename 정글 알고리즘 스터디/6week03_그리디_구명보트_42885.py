
# https://programmers.co.kr/learn/courses/30/lessons/42885
from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while people:
        a = limit
        p = people.pop()  # 제일 무거운사람
        a -= p
        if people and a >= people[0]:  # 제일 가벼운사람
            people.popleft()

        answer += 1

    return answer
""" 
정확성  테스트
테스트 1 〉	통과 (1.49ms, 10.3MB)
테스트 2 〉	통과 (0.71ms, 10.3MB)
테스트 3 〉	통과 (0.64ms, 10.2MB)
테스트 4 〉	통과 (0.57ms, 10.3MB)
테스트 5 〉	통과 (0.51ms, 10.3MB)
테스트 6 〉	통과 (0.21ms, 10.3MB)
테스트 7 〉	통과 (0.36ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
테스트 9 〉	통과 (0.08ms, 10.3MB)
테스트 10 〉	통과 (0.70ms, 10.3MB)
테스트 11 〉	통과 (0.49ms, 10.3MB)
테스트 12 〉	통과 (0.71ms, 10.2MB)
테스트 13 〉	통과 (0.62ms, 10.2MB)
테스트 14 〉	통과 (1.25ms, 10.3MB)
테스트 15 〉	통과 (0.07ms, 10.1MB)
효율성  테스트
테스트 1 〉	통과 (9.28ms, 10.7MB)
테스트 2 〉	통과 (10.12ms, 10.8MB)
테스트 3 〉	통과 (10.20ms, 10.8MB)
테스트 4 〉	통과 (11.00ms, 10.8MB)
테스트 5 〉	통과 (9.21ms, 10.7MB) """
