from collections import deque


def solution(bridge_length, weight, truck_weights):

    answer = 0
    bridge = deque([0]*bridge_length)
    sum = 0
    truck_weights = deque(truck_weights)

    while bridge:
        tmp = bridge.popleft()
        sum -= tmp
        answer += 1
        if len(truck_weights):
            truck = truck_weights.popleft()
            if truck + sum <= weight:
                bridge.append(truck)
                sum += truck
            else:
                truck_weights.appendleft(truck)
                bridge.append(0)

    return answer
