import sys

sys.stdin = open('input.txt')

import heapq, math


# 다익스트라 함수
def dijkstra(graph, start):
    distances = {v: math.inf for v in graph}
    distances[start] = 0
    # 다음에 조사할 후보군 삽입 리스트
    heap = []  # 최소 힙
    heapq.heappush(heap, [0, start])  # 거리, 시작 정점 추가
    visited = set()  # 방문 확인

    # 힙이 빌 때까지
    while heap:
        # 거리 , 현재 정점
        dist, current = heapq.heappop(heap)

        # 방문했거나, 기존 거리보다 갱신 거리가 크면 필요없음
        if current in visited or distances[current] < dist: continue

        visited.add(current)

        # 연결된 이웃 정점 확인
        for next, weight in graph[current]:  # 강사님 코드 : graph[current].items()
            next_distance = dist + weight  # 현재 거리 + 다음 거리

            # 더 짧은 경로 발견 시 거리 갱신 후 추가
            if next_distance < distances[next]:
                distances[next] = next_distance
                heapq.heappush(heap, [next_distance, next])
    return distances


# 입력
T = int(input())

for test_case in range(1, T + 1):
    # 번호, 도로 구간 개수
    N, E = map(int, input().split())

    # 인접리스트 형태
    graph = {v: [] for v in range(N + 1)}

    # print(graph)

    # 인접리스트에 start : (end,weight) 입력
    for i in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))

    # 다익스트라 함수 결과를 저장
    result = dijkstra(graph, 0)

    # 마지막 지점의 값 출력
    print(f"#{test_case} {result[N]}")

    '''
    강사님께서 그래프 불러온 형태 -> 딕셔너리 내부 딕셔너리
        graph = {
        'a': {'b': 3, 'c': 5},
        'b': {'c': 2},
        'c': {'b': 1, 'd': 4, 'e': 6},
        # 'c': {'b': -4, 'd': 4, 'e': 6},
        'd': {'e': 2, 'f': 3},
        'e': {'f': 6},
        'f': {}
    }
    '''