import sys
sys.stdin = open('input.txt')

def dijkstra():
    dist = [E * 100] * (N + 1)
    visited = [0] * (N + 1)

    dist[0] = 0

    for _ in range(N):
        min_idx = -1
        min_value = E * 100

        # 최소값 찾기
        for i in range(N + 1):
            if not visited[i] and min_value > dist[i]:
                min_idx = i
                min_value = dist[i]
        # print(min_idx)
        visited[min_idx] = 1

        # 갱신할수 있으면 갱신
        # print(dist)
        for i in range(N + 1):
            if not visited[i] and dist[i] > dist[min_idx] + data[min_idx][i]:
                dist[i] = dist[min_idx] + data[min_idx][i]
        # print(dist)
    return dist[N]


T = int(input())

for tc in range(1, T + 1):
    # N: 마지막 정점의 번호, E 간선 수
    N, E = map(int, input().split())

    data = [[E * 100] * (N + 1) for _ in range(N + 1)]

    for i in range(E):
        s, e, w = map(int, input().split())
        data[s][e] = w  # 유향 그래프니까
    # print(adj_arr)
    print(f'#{tc} {dijkstra()}')