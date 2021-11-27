def Greedy(k, data):
    target, coin_list = k, data
    sum, total_count = 0, 0

    while len(coin_list) != 0:
        coin = coin_list.pop()

        if coin + sum > k:
            continue
        else:
            coin_count = int(target / coin)
            target = target % coin
            sum += coin_count * coin
            total_count += coin_count

        if sum == target:
            break
    print(total_count)


N, K = list(map(int, input().split()))
A = []
for _ in range(N):
    A.append(int(input()))

Greedy(K, A)
