'''
0. N개의 노드로 구성된 유향 그래프에 대해 인접 노드로 이동하는 비용을 기록한 인접 행렬
1.모든 노드 i에 대해 모든 노드 j로 이동하는 경로가 있는 경우, 최소 이동 비용 구했을 때, 가장 큰 값을 출력
2. i -> j , 다른 모든 노드를 지날 필요 없음 (= 바로 이동도 가능하다. )
3. 노드 사이 비용이 음수인 경우가 있다 = 벨만-포드 / 플로이드 위셜 사용해야한다.
    -> 한 개의 노드가 아닌 모든 노드에 대해 고려한다. = 플로이드 위셜 사용해야 한다.
4. 1<=T<=50, 3<=N <=100, -99<=aij<=99 (단 i != j 면서 aij==0인 경우는 인접하지 않음을 나타낸다.) -> 조건 처리 필요.
5. 마지막에 행렬을 순회하면서, 가장 비용이 큰 값을 출력해야 한다.
'''

def floyd_warshall(graph):
    n = len(graph)  # 전체 노드의 수
    for k_node in range(n):  # 모든 정점 = 경유 노드
        for start in range(n):  # 시작 노드
            for end in range(n):  # 도착 노드
                dik = graph[start][k_node]  # 시작 노드 -> 경유노드
                dkj = graph[k_node][end]    # 경유노드 -> 도착 노드
                dij = graph[start][end]     # 시작 노드 -> 도착 노드

                if dik + dkj < dij:     # 만약, 경유해서 가는 값이 더 작으면
                    graph[start][end] = dik + dkj  # 경유한 거리로 갱신(최단 거리 갱신)


INF = float('inf')  # 무한대 처리

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 인접 행렬 만들기
    adj_matrix = [list(map(int, input().split())) for _ in range(N)]

    # 인접하지 않은 값에 대한 처리 필요 (단 i != j 면서 aij==0인 경우는 인접하지 않음을 나타낸다.)
    for i in range(N):
        for j in range(N):
            # 나자신이 아니면서, 값이 0이면 = 인접하지 않음
            if i != j and adj_matrix[i][j] == 0:
                adj_matrix[i][j] = INF

    # 플로이드 워셜을 사용하여 모든 노드에 대한 거리 계산
    result = floyd_warshall(adj_matrix)

    # 가장 큰 값을 출력하기
    ans = 0
    # 순회하면서 큰 값으로 갱신
    for lst in adj_matrix:
        for num in lst:
            ans = max(ans, num)

    print(f'#{tc} {ans}')