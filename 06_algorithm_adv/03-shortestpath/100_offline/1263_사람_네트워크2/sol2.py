import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs(start_node, graph):
    visited = [0] * N
    q = deque([(0, start_node)])
    visited[start_node] = 1

    result = 0
    while q:
        weight, current = q.popleft()
        result += weight
        for next in range(N):
            if not visited[next] and graph[current][next]:
                q.append((weight + 1, next))
                visited[next] = 1

    return result

T = int(input())
for tc in range(1, T + 1):
    N, *input_line = list(map(int, input().split()))

    graph = []

    for row in range(N):
        graph.append(input_line[row*N:row*N+N])

    result = N * (N + 1)

    for i in range(N):
        result = min(result, bfs(i, graph))
    print(f"#{tc} {result}")