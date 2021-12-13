def solution(citations):
    length = len(citations)  # 배열의 길이
    citations.sort()

    for i in range(length):
        if citations[i] >= length - i:
            return length - i  # 논문이 인용된 횟수 >= 인용된 논문의 개수
    return


##다른 풀이
"""
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
"""
