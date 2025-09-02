# 출발지(S)에서 도착지(G)까지 가기 위한 도로 복구 작업을 빠른 시간 내에 수행하려고 한다
# 도로가 파여진 깊이에 비례해서 복구시간은 증가한다
# 출발지에서 도착지까지 가는 경로 중에 복구 시간이 가장 짧은 경로에 대한 총 복구 시간을 구하시오.

import sys
sys.stdin = open('1249_보급로\input.txt','r')


import heapq
from collections import deque

INF = 10**9

d_row = [-1,1,0,0]
d_col = [0,0,-1,1]

def bfs_dijkstra(row,col):
    dist = [[INF]*n for _ in range(n)]
    # 시작 위치 비용을 grid[0][0]로 초기화 (다른 방식으로 0으로 시작하고 이웃으로부터 더해도 됨)
    dist[0][0] = arr[0][0]

    min_heap = []
    heapq.heappush(min_heap,(dist[0][0],0,0))

    while min_heap:
        distance, c_row, c_col = heapq.heappop(min_heap)
        if distance > dist[c_row][c_col]: continue

        if c_col == n-1 and c_row == n-1 : break

        for i in range(4):
            n_row = c_row + d_row[i]
            n_col = c_col + d_col[i]
            
            if not(0<=n_row<n and 0<=n_col<n): continue

            next_distance = distance + arr[n_row][n_col]
            if next_distance < dist[n_row][n_col]:
                dist[n_row][n_col] = next_distance
                heapq.heappush(min_heap,(next_distance,n_row,n_col))
    
    return dist[n-1][n-1]

T = int(input())

for tc in range(1,T+1):
    # n * n (0<=n<=100)
    n = int(input())
    arr=[list(map(int, list(input().strip()))) for _ in range(n)]
    
    
    result = bfs_dijkstra(0,0)

    print(f'#{tc} {result}')