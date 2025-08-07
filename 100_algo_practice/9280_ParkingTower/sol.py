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

    # 기다리는 차량을 저장할 큐(먼저온 차량을 먼저 주차시키기 위해 큐로 구현)
    waiting_car = deque()

    # 남아있는 주차 공간 번호를 저장할 힙 변수
    parking_remain = [i for i in range(n)]

    # 주차중인 차랑
    parking = set()

    # 결과를 저장할 변수
    result = 0

    # 현재 들어올 차량 받기
    for _ in range(2*m):
        car = int(input())

        # 들어오는 차량일 경우
        if car>0:
            # 주차할 공간이 없다면
            if len(parking) == n:
                # 기다리는 차량에 저장
                waiting_car.append(car)
            # 주차할 수 있는 공간이 있다면
            else:
                parking.add((heapq.heappop(parking_remain),     car))

        # 나가는 차량일 경우
        else:
            # 주차중인 차량 집합에서 하나씩 뽑으며 현재차량과 같으면 출차시킨다.
            for out_idx, out_car in parking:
                # abs로 양수로 바꾼다
                if out_car == abs(car):
                    parking.remove((out_idx,out_car))
                    # 출차를 했으니 현재 주차공간을 다시 남아있는 주차 힙에 넣는다
                    heapq.heappush(parking_remain,     out_idx)
                    # 정산된 금액을 결과값에 더해준다.
                    result+= (ri[out_idx]*wi[out_car-1])
                    # 집합 탐색 중단
                    break
            # 기다리는 주차 차량이 있으면
            if waiting_car:
                # 번호가 제일 작은 주차공간에 넣기
                parking.add((heapq.heappop(parking_remain),   waiting_car.popleft()))
                
    print(f'#{tc} {result}')

    

    

