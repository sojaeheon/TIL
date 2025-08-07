import sys
sys.stdin = open('input.txt')

from collections import deque
#     상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_road_move_time(row, col):
    # 너비 우선 탐색 -> queue
    # deque의 첫번째 인자는 iterable 객체이고,
    # 내가 지금 queue에 넣고 싶은 후보군은? (0, 0)
    # queue = deque((0, 0))  # -> queue = deque[0, 0]
    # queue = deque([(0, 0)])  # 이렇게해야 올바르게 (0, 0)
    queue = deque()
    queue.append((0, 0))    # 시작 정점 후보군에 삽입
    distance[0][0] = 0      # 시작 위치까지 이동거리는 0

    # BFS 탐색
    while queue:    # 후보군이 있는 동안
        row, col = queue.popleft()
        # 이 위치에서 4방향에 대한 탐색
        # for k in [(-1, 0), (1, 0)....]
        for k in range(4):
            nx = row + dx[k]
            ny = col + dy[k]
            # 이제 그 다음 탐색지 data[nx][ny] 번째가 이동 가능한지 판별
            # 그럴려면 리스트의 범위를 벗어나지 않아야한다.
            # 그리고, 이전에 방문한 적 없어야 한다.    -1로 초기화 해 두었음
            # 그리고, 그 위치가 길 이어야한다. -> 1은 길 0은 벽
            if 0 <= nx < N and 0 <= ny < M and distance[nx][ny] == -1 and data[nx][ny]:
                # 위 조건을 모두 만족하면 후보군에 들 수 있다.
                queue.append((nx, ny))
                # 다음 위치까지 도달하는 비용은, 내 위치 보다 1 증가한 값이다.
                distance[nx][ny] = distance[row][col] + 1
                # 도착지점에 도착하면, BFS 특성상 가장 빠르게 도착한 길이니
                # 그떄까지의 비용을 할당하고 종료
                if nx == N-1 and ny == M-1: # 도착지다.
                    return
    # 모든 후보군을 다 탐색했지만, return되어서 함수가 종료된 적이 없이
    # 코드가 이곳까지 도달했다면? 도착할 수 없다는 의미다.
    return -1



# 데이터 입력
# row: N, col: M
N, M = map(int, input().split())
data = [list(map(int, input())) for _ in range(N)]
# 방문 표시를 할거다. -> 우리의 최종 목적이 무엇이냐?
# 해당 위치까지 도달하는데 걸린 비용이 얼만지를 기록!
distance = [[-1] * M for _ in range(N)]

get_road_move_time(0, 0)
print(distance[N-1][M-1])
for dis in distance:
    print(*dis)
