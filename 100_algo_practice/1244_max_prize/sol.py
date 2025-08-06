import sys
sys.stdin = open("input.txt", "r")

def dfs(result, n):
    global max_result, visited

    if n == 0:
        result_int = int(''.join(result))
        max_result = max(max_result, result_int)
        return

    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            result[i], result[j] = result[j], result[i]
            
            key = (n - 1, tuple(result))
            if key not in visited:
                visited.add(key)
                dfs(result, n - 1)

            result[i], result[j] = result[j], result[i]  # 백트래킹

T = int(input())

for tc in range(1, T + 1):
    num_board, n = input().strip().split()
    num_board = list(num_board)

    max_result = float('-inf')
    visited = set()

    dfs(num_board, int(n))

    print(f'#{tc} {max_result}')
