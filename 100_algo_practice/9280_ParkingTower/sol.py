# 1부터 n까지 번호가 매겨진 n개의 주차 공간
# 차가 주차장에 도착하면, 진용이는 비어있는 주차 공간이 있는지 검사
# 빈 주차 공간이 있으면 진용이는 곧바로 주차를 시키며,
# 주차 가능한 공간 중 "번호가 가장 작은 주차 공간에 주차"하도록 한다
# 주차를 기다리는 차량이 여러 대라면, 입구의 대기 장소에서 자기 차례를 기다려야 한다.(deque)
# 운전자들은 새치기를 하지 않는다

# 주차 요금 = 차량의 무게 * 책정된 단위 무게당 금액
# 이용 시간은 고려하지 않는다

# 오늘 들어올 m 대의 차량
# 진용이의 주차장이 오늘 하루 벌어들일 "총 수입"을 계산하는 프로그램 작성

import sys
import heapq
from collections import deque
sys.stdin = open("sample_input.txt", "r")


T = int(input())

for tc in range(1, T + 1):
    n,m = map(int,input().strip().split())
    # i 번재 주차 공간의 단위 무게당 요금 Ri
    ri = [int(input()) for _ in range(n)]
    # 차량 i 의 무게 wi
    wi = [int(input()) for _ in range(m)]

    waiting_car = deque()
    parking_remain = [i for i in range(n)]
    parking = set()

    result = 0
    

    for _ in range(2*m):
        car = int(input())

        if car>0:
            if len(parking) == n:
                waiting_car.append(car)
            else:
                parking.add((heapq.heappop(parking_remain),car))
        else:
            for out_idx, out_car in parking:
                if out_car == abs(car):
                    parking.remove((out_idx,out_car))
                    heapq.heappush(parking_remain,out_idx)
                    result+= (ri[out_idx]*wi[out_car-1])
                    break
            if waiting_car:
                parking.add((heapq.heappop(parking_remain),waiting_car.popleft()))

    print(f'#{tc} {result}')

    

    

