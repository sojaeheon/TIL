import sys
sys.stdin = open('input.txt')

# 가장 영향력이 높다는 것을,
# 모든 사람들과 가장 가까운 것으로 표현
# 모든 노드들에서 특정 노드로 가는 거리들의 누적 값이 가장 적어야 함
def flowyd_washall():
    for k_node in range(N):
        for start in range(N):
            for end in range(N):
                via = adj_matrix[start][k_node] + adj_matrix[k_node][end]
                adj_matrix[start][end] = min(adj_matrix[start][end], via)


T = int(input())
for tc in range(1, T+1):
    # N: 노드의 개수
    # CC(i): i노드로 도달하는 모든 노드들의 최단 경로의 합
        # 즉 CC(2): 4의 의미는
        # 1~5번 노드들 에서 2번 노드로 도달하는 최단경로들의 합이 4라는 뜻.

    # 간선 정보
        # 단, 자기 자신으로 돌아가는 간선 없음.
    # 노드의 개수 N, 이후 한 줄로 N개의 값이 N번 반복
    N, *input_line = list(map(int, input().split()))
    max_value = float('inf')
    # 인접 행렬 초기화
    adj_matrix = []
    # N번 마다 행 정보를 인접 행렬에 반복 삽입
    for row in range(N):
        adj_matrix.append(input_line[row*N:row*N+N])

    # for m in adj_matrix:
    #     print(m)
    # 자기 자신을 제외한 도달 불능 지점 최대값으로 초기화
    for i in range(N):
        for j in range(N):
            if i == j: continue
            if not adj_matrix[i][j]:
                adj_matrix[i][j] = max_value

    flowyd_washall()

    result = max_value
    for m in adj_matrix:
        result = min(result, sum(m))
    print(f"#{tc} {result}")