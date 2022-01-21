# from itertools import permutations, combinations
# from collections import Counter


# def solution(orders, course):
#     answer = []

#     for i in course:
#         reorders = []
#         for j in range(len(orders)):
#             a = list(orders[j])
#             a.sort()
#             reorders += [''.join(i) for i in combinations(a, i)]

#         if reorders:
#             cnt = Counter()
#             for word in reorders:
#                 cnt[word] += 1
#             max_value = max(list(cnt.values()))

#             if max_value >= 2:
#                 for key in list(cnt.keys()):
#                     if cnt[key] == max_value:
#                         answer.append(key)
#     answer.sort()
#     return answer


from itertools import combinations


def solution(orders, course):
    answer = []
    for j in course:
        all_com = []
        for i in orders:
            i = list(i)
            i.sort()
            all_com.extend(list(combinations(i, j)))
        
        if all_com:
            tmp = set(all_com)
            comb_dict = dict()
            for i in tmp:
                comb_dict[i] = all_com.count(i)
            sorted_max = max(comb_dict.values())

            for key in comb_dict.keys():
                if comb_dict[key] == sorted_max and sorted_max>=2:
                    answer.append("".join(key))
    return answer


# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2, 3, 4]))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
