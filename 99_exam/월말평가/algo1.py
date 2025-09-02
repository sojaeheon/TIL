import sys
sys.stdin = open('algo1_sample_in.txt')

import heapq

def MST(start):
    global result
    # PRIM 알고리즘
    hq = [(cost, start, end) for cost, end in adj_list.get(start, [])]
    heapq.heapify(hq)
    visited = set()
    visited.add(start)
    acc = 0
    while hq and len(visited) < N:
        cost, x, y = heapq.heappop(hq)
        if y in visited: continue
        visited.add(y)
        acc += cost
        for weight, end in adj_list.get(y, []):
            if end not in visited:
                heapq.heappush(hq, (weight, y, end))
    result = acc
    return len(visited) == N



T = int(input())
for tc in range(1, T+1):
    # N: 노드수, M: 간선 수
    N, M = map(int, input().split())
    # X, Y, cost
    data = [list(map(int, input().split())) for _ in range(M)]
    data.sort(key=lambda x: x[2])
    adj_list = {}
    for x, y, cost in data:
        adj_list[x] = adj_list.get(x, []) + [(cost, y)]
        adj_list[y] = adj_list.get(y, []) + [(cost, x)]
    result = 0
    print(f'#{tc} {result}') if MST(data[0][0]) else print(f'#{tc} -1')
