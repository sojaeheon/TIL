T = int(input())
for test_case in range(1, T+1):
    # data input 읽기
    data = list(map(int, input().split()))
    N = data[0]
    matrix = []
    # 데이터를 인접 행렬로 변환
    for i in range(1, N**2, N):
        mat_line = data[i:i+N]
        matrix.append(mat_line)

    # 인접하지 않은 두 노드를 무한으로 초기화
    max_value = max(max(i) for i in matrix) * (N ** 2)
    for i in range(N):
        for j in range(N):
            if i != j and matrix[i][j] == 0:
                matrix[i][j] = max_value

    # 플로이드 워셜 진행
    for m in range(N):
        for s in range(N):
            for e in range(N):
                matrix[s][e] = min(matrix[s][e], matrix[s][m] + matrix[m][e])

    # 네트워크가 가장 짧은 데이터를 뽑는다
    print(matrix)
    result = min(sum(i) for i in matrix)

    print(f'#{test_case} {result}')