import sys
sys.stdin = open('input.txt')


def prim_algorithm(N, xs, ys, E):
    # Prim 알고리즘 초기화
    visited = [False] * N
    min_edge_cost = [float('inf')] * N
    min_edge_cost[0] = 0.0
    total_cost_squared = 0.0

    # 모든 섬을 MST에 포함할 때까지 반복
    for _ in range(N):
        u = -1
        min_val = float('inf')
        
        # 아직 방문하지 않은 섬들 중 최소 비용의 섬 선택
        for i in range(N):
            if not visited[i] and min_edge_cost[i] < min_val:
                min_val = min_edge_cost[i]
                u = i
        
        # 선택된 섬이 없으면 (연결되지 않은 경우) 종료
        if u == -1:
            break

        visited[u] = True
        total_cost_squared += min_edge_cost[u]

        # 선택한 섬 u와 다른 미방문 섬들 사이의 비용 갱신
        for v in range(N):
            if not visited[v]:
                dx = xs[u] - xs[v]
                dy = ys[u] - ys[v]
                cost = dx * dx + dy * dy
                if cost < min_edge_cost[v]:
                    min_edge_cost[v] = cost
    
    return round(total_cost_squared * E)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    E = float(input())
    
    ans = prim_algorithm(N, xs, ys, E)
    print(f"#{tc} {ans}")