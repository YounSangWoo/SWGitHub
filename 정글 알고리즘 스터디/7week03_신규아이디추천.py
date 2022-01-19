def solution(new_id):
    answer = ''

    delete_list = [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44,
                   47, 58, 59, 60, 61, 62, 63, 64, 91, 92, 93, 94, 96, 123, 124, 125, 126]

    tmp = list(map(ord, new_id))  # 아스키 코드로 변환
    
    #1단계 대문자->소문자
    for i in range(len(tmp)):
        if tmp[i] >= 65 and tmp[i] <= 90:
            tmp[i] = tmp[i]+32
    
    #2단계 특수문자 제거
    k = 0
    while k < len(tmp):
        if tmp and tmp[k] in delete_list:
            del tmp[k]
        else:
            k += 1

    flag = False
    k = 0
    while k < len(tmp):
        if tmp and tmp[k] == 46 and flag != True:
            flag = True
            k += 1
        elif tmp and tmp[k] == 46 and flag == True:
            del tmp[k]
        else:
            flag = False
            k += 1

    def D(tmp):
        if tmp and tmp[0] == 46:
            tmp.remove(tmp[0])
        if tmp and tmp[-1] == 46:
            tmp.remove(tmp[-1])

    D(tmp)

    if not tmp:
        tmp.append(97)

    while len(tmp) >= 16:
        tmp.pop()

    D(tmp)

    while len(tmp) < 3:
        a = tmp[-1]
        tmp.append(a)

    tmp = list(map(chr, tmp))
    answer = ''.join(tmp)

    return answer


# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("z-+.^."))
# print(solution("=.="))
# print(solution("123_.def"))
# print(solution("abcdefghijklmn.p"))
print(solution("./././././abcd/././././."))
