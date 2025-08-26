import sys
sys.stdin = open('input.txt')


def find_set(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find_set(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    root_x = find_set(parent, x)
    root_y = find_set(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x
        return True
    return False

def kruskal_algorithm(N, xs, ys, E):
    # Kruskal 알고리즘을 사용하여 최소 신장 트리의 총 비용을 계산
    edges = []
    # 모든 가능한 간선 생성 및 비용 계산
    for i in range(N):
        for j in range(i + 1, N):
            dx = xs[i] - xs[j]
            dy = ys[i] - ys[j]
            cost = dx * dx + dy * dy
            edges.append((cost, i, j))
    
    # 간선을 비용 기준으로 정렬
    edges.sort()

    parent = list(range(N))
    total_cost_squared = 0.0
    edge_count = 0

    # 정렬된 간선들을 순회하며 MST 구성
    for cost, u, v in edges:
        if union(parent, u, v):
            total_cost_squared += cost
            edge_count += 1
            if edge_count == N - 1:
                break
    
    return round(total_cost_squared * E)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    E = float(input())
    
    ans = kruskal_algorithm(N, xs, ys, E)
    print(f"#{tc} {ans}")