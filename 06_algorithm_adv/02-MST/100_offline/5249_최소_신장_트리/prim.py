import sys
sys.stdin = open('input.txt')

import heapq


# 시작 노드 선택 (여기서는 0번 노드부터 시작)
def prim(start, acc):
    # 시작 노드와 연결된 간선을 저장할 우선순위 큐
    heap = [(W, next) for next, W in G[start]]
    # 시작점 방문표시
    visited[start] = 1

    heapq.heapify(heap)
    while heap:
        # 가장 작은 가중치의 간선 선택
        W, now = heapq.heappop(heap)
        # 아직 방문한 적 없다면
        if not visited[now]:
            acc += W
            visited[now] = 1
            # 새로운 노드와 연결된 간선을 우선순위 큐에 추가
            for next, W in G[now]:
                if not visited[next]:
                    heapq.heappush(heap, (W, next))
    return acc

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]

    visited = [0] * (V+1)
    G = [[] for _ in range(V+1)]
    for i in range(E):
        G[arr[i][0]].append([arr[i][1], arr[i][2]])
        G[arr[i][1]].append([arr[i][0], arr[i][2]])

    result = prim(0, 0)
    print(f'#{tc} {result}')