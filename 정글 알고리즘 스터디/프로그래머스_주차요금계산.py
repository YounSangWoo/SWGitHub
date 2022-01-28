from collections import defaultdict
import math


def solution(fees, records):
    answer = []

    #기록에서 시간, 분 ,차량번호, 입출결과를 분리
    #records 요소 구성 ["xx:xx yyyy zz"]

    parking_list = defaultdict(lambda: 0)
    #1. 출차관리를 위한 리스트 생성 key 값으로 차량번호 Value로 체류시간
    for i in records:
        time = int(i[0:2])*60+int(i[3:5])  # 시간을 분으로 환산
        #차량 정보에 관한 값을 하나씩 빼본다.
        if i[11:] == 'IN':
            parking_list[i[6:10]] += (1439-time)
        #입차의 경우 안나갈 수도있으니 우선 23:59출차 기준 누적시간 기록
        elif i[11:] == 'OUT':
            #출차가 되었다면 23:59분 출차 기록은 삭제 새로 들어온 time을 빼준다.
            parking_list[i[6:10]] -= (1439-time)

    print(parking_list)
    #2 이제 어느차량이 얼마나 있었는지 알았으니 돈을 계산해 보자.
    #fees[0] = 기본시간 fees[1] = 기본요금  fees[2] = 단위시간 fees[3] = 단위시간당 요금
    #요금 계산 방법 : 기본요금 if 누적 시간-기본시간< 0 else 기본요금+(누적시간-기본시간)*단위시간별요금
    #그전에 차량관리 리스트에 있는 아이들의 key값에 대한 정렬이 필요 딕셔너리는 정렬이 안되므로 key들만 정렬을 해보자
    car_list = []
    for key in parking_list.keys():
        car_list.append(key)
    car_list.sort()  # 차들의 정렬 완료

    for car in car_list:  # 요금을 순차대로 꺼내어 답에 저장해보자
        used_time = parking_list[car]-fees[0]
        if used_time <= 0:
            answer.append(fees[1])
        else:
            answer.append(fees[1]+(math.ceil(used_time/fees[2])*fees[3]))

    return answer

print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))