import sys
sys.stdin = open("input.txt")


import heapq

def prim():
    visited = [False] * (V + 1)
    heap = [(0, 1)]  # (가중치, 정점)
    total_weight = 0
    edge_count = 0

    while heap and edge_count < V:
        weight, current_node = heapq.heappop(heap)

        if visited[current_node]:
            continue

        visited[current_node] = True
        total_weight += weight
        edge_count += 1

        for next_weight, next_node in graph[current_node]:
            if not visited[next_node]:
                heapq.heappush(heap, (next_weight, next_node))
    
    return total_weight

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        n1, n2, weight = map(int, input().split())
        graph[n1].append((weight, n2))
        graph[n2].append((weight, n1))

    result = prim()
    print(f"#{tc} {result}")