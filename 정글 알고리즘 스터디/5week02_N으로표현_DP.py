def solution(N, number):
    dp = [[]]
    for i in range(1, 9):
        temp = set()
        for j in range(1, i):
            for k in dp[j]:
                for l in dp[i - j]:
                    temp.add(k + l)
                    if k - l >= 0:
                        temp.add(k - l)
                    temp.add(k * l)
                    if l != 0 and k != 0:
                        temp.add(k // l)
        temp.add(int(str(N) * i))
        if number in temp:
            return i
        dp.append(list(temp))

    return -1
print(solution(5,12))

# N, number = 5, 12라는 예제에서,
# N = 1: [5]
# N = 2: [10(5+5), 0(5-5), 25(5*5), 1(5//5), 55('5'*2)]
# N = 3: [15(5+10), 50(5*10), 5(5+0), 0(5*0), 5(5-0), 30(5+25), 125(5*25), 6(5+1), 5(5*1)...]
# ....
# 다음과 같이 N에 따라 값들이 나오는 것을 확인할 수 있다.
# N = 2에서는 N = 1일때의 원소들을 가지고 사칙연산을 진행한다.
# N = 3에서는 N = 1과 N = 2의 원소들을 가지고 사칙연산을 진행한다.
# 여기서 얻어낼 수 있는 규칙은 다음과 같다.

# 2 = 1+1
# 3 = 1+2, 2+1
# 어떤 N에 대한 원소들을 고르려면, 더해서 N이 되는 두 정수 값의 배열들이 사칙연산의 대상이 된다는 것이다.
