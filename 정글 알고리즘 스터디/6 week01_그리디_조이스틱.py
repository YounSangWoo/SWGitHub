# A B C D E F G H I J K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
# 기본 이름 A
""" from collections import defaultdict


def solution(name):
    A = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
         'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    dic = defaultdict(list)

    answer = 0
    cnt = 12
    for i in range(14):
        dic[A[i]] = i
    for i in range(14, 26):
        dic[A[i]] = cnt
        cnt -= 1
    forward = dic[name[0]]
    backward = dic[name[0]]
    # forward
    tmp = 0
    for i in range(1, len(name)):
        tmp += 1
        if dic[name[i]] != 0 :
            forward += (dic[name[i]]+tmp)
            tmp = 0
    # backward
    tmp = 0
    for i in range(len(name)-1, 0, -1):
        tmp += 1
        if dic[name[i]] != 0 :
            backward += (dic[name[i]]+tmp)
            tmp = 0
        

    answer = min(forward, backward)
    return answer
 """
# 다른 블로그 풀이

def solution(name):
    alpha = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]  # 상하 최소 거리 구하여 저장
    
    i, answer = 0, 0

    # 조이스틱을 움직여 글자 완성하기
    while True:
        answer += alpha[i]
        alpha[i] = 0  # 이동이 끝났으면 값을 0으로 만듬

        # 모든 값이 0이 되면 글자가 완성되었으므로 답을 리턴해줌
        if sum(alpha) == 0:
            return answer

        left, right = 1, 1  # 왼쪽과 오른쪽으로 움직일 거리
        # 이동해야 할 글자가 나올 때까지 반복
        while alpha[i - left] == 0:
            left += 1
        while alpha[i + right] == 0:
            right += 1

        # left, right 중 최소거리 구하여 다음 위치로 이동
        if right > left:
            answer += left
            i -= left
        else:
            answer += right
            i += right


print(solution("ABAAB"))
print(ord('A'))
