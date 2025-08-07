n = 4 
board = [[0] * n for _ in range(n)]  # 4*4 2차원 배열 생성
solutions = []  # 모든 솔루션을 저장할 리스트

n_queens(0, board)

for solution in solutions:
    print(solution)
