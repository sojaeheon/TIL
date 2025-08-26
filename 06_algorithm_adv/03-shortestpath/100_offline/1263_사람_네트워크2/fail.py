import sys
sys.stdin = open('input.txt')


import heapq

def dijkstra(start):
    distances = [max_value] * N
    distances[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    visited = set()

    while heap:
        weight, current = heapq.heappop(heap)

        if current in visited or weight > distances[current]: continue
        visited.add(current)

        for next in range(N):
            acc = weight + adj_matrix[current][next]

            if adj_matrix[current][next] and acc < distances[next]:
                distances[next] = acc
                heapq.heappush(heap, (acc, next))

    return distances

T = int(input())
for tc in range(1, T+1):
    N, *input_line = list(map(int, input().split()))
    max_value = float('inf')
    result = max_value
    adj_matrix = []
    for row in range(N):
        adj_matrix.append(input_line[row*N:row*N+N])

    for i in range(N):
        for j in range(N):
            if i == j: continue
            if not adj_matrix[i][j]:
                adj_matrix[i][j] = max_value

    # 모든 노드에 대해서 다익스트라
    for i in range(N):
        dist = dijkstra(i)
        result = min(result, sum(dist))

    print(f"#{tc} {result}")