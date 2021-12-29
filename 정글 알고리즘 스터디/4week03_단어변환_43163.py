from collections import deque
def solution(begin, target, words):
    answer = 0
    n = len(begin)
    count = 0
   
    if target not in words:
         return 0;
    else :
        for words_A in words:
            if begin == words_A:
                            

    def dfs(begin,words_A):
        for i in range(n):
            if begin[n] != words_A[n]:
                count +=1
            if count==1: #다른점이 한가지
                begin = words_A
                dfs(begin, words_A)




    answer = min(depth_list)
    return answer

""" 다른분 풀이 """


def compare(compare_word, words):
    a = list()
    for word in words:
        if sum((1 if a != b else 0) for a, b in zip(word, compare_word)) == 1:
            a.append(word)
    return a


def solution(begin, target, words):
    ch = set([begin])
    dq = deque([(begin, 0)])
    if target not in words:
        return 0
    while dq:
        start, cnt = dq.popleft()
        if start == target:
            return cnt
        for word in compare(start, words):
            if word not in ch:
                ch.add(word)
                dq.append([word, cnt+1])

    return 0
