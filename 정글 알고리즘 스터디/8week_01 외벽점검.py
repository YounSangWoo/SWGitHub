# from itertools import combinations
# from collections import defaultdict

# def solution(n, weak, dist):
#     answer = 0
#     weak.sort()
#     dis_list = defaultdict(list)
#     a = list(combinations(weak, 2))

#     for i in range(len(a)):
#         dis_list[a[i]].append(a[i][1]-a[i][0])
#         dis_list[a[i]].append(a[i][0]-a[i][1]+12)

#     del_key_list = []
#     for key in dis_list.keys():
#         flag = False
#         for dis in dist:
#             if dis >= dis_list[key][0] or dis >= dis_list[key][1]:
#                 flag = True
#                 break
#             else:
#                 flag = False
#         if flag:
#             continue
#         else:
#             del_key_list.append(key)

#     for key in del_key_list: #인부들이 갈 수 있는 후보 weak 쌍만 남긴다.
#         del(dis_list[key])

#     print(dis_list)


#     # 위중에 골라야 하는데...
#     tmp_answer = 0
#     for i in dist:
#         for key in dis_list.keys():
#             print(dis_list[key][0])
#             if i >= dis_list[key][1] and (key[0] in weak):
#                 tmp_answer += 1
#                 for k in range(key[1], key[0]-1, -1):
#                     if k in weak:
#                         weak.remove(k)
#             elif i>= dis_list[key][0] and (key[0] in weak):
#                 tmp_answer+=1
#                 for k in range(key[0],key[1]+1):
#                     if k in weak:
#                         weak.remove(k)

#             if not weak:
#                 break
#         if not weak:
#             break
#     if weak:
#         tmp_answer = 0

#     if tmp_answer <= answer :
#         answer = tmp_answer

#     if answer ==0:
#         answer = -1

#     return answer

from itertools import permutations, combinations


def solution(n, weak, dist):
    answer = len(dist)+1  # 점검이 불가능한 겨우 가정
    weak_length = len(weak)

    # 1. 길이를 두배로 늘리면 방향을 고려 안해도 된다.
    for i in range(weak_length):
        weak.append(weak[i]+n)

    dist_combin = list(map(list, permutations(dist, len(dist))))
    # 2. dist의 모든 경우이 수를 구한다.
    for i in range(weak_length):
        start = [weak[j] for j in range(i, i+weak_length)]
        # 시작점을 하나씩 바꾸면서, weak의 길이만큼 잘라 사용
        for dist_p in dist_combin:
            result = 1  # 활용되는 dist의 친구수 추가
            dist_distance = 0  # 거리
            check_len = start[0] + dist_p[0]  # dist의 친구가 확인할 수 있는 최대 거리

            for k in range(weak_length):
                if start[k] > check_len:  # 확인 가능한 최대 거리를 넘었을 경우
                    result += 1  # 활용되는 dist의 친구 수 추가
                    # 더이상 투입 인원이 없을 경우
                    if result > len(dist_p):
                        break
                    dist_distance += 1  # 다음친구들 투입
                    # 친구가 확인할 수 있는 거리 업테이트
                    check_len = start[k]+dist_p[dist_distance]
            answer = min(answer, result)  # 작은 값을 선택한다.
    if answer > len(dist):  # 만약 weak를 다 체크 못한다면 -1 리턴
        return -1
    return answer


# print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 5, 6, 10], [1, 2]))
