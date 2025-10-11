import sys
sys.stdin = open("input.txt", "r")



for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int,input().strip().split())) for _ in range(100)]
    
    max_result = 0

    for i in range(100):
        row_sum = 0
        col_sum = 0
        for j in range(100):
            row_sum += arr[i][j]
            col_sum += arr[j][i]

        max_result = max(row_sum,col_sum,max_result)

    cross_sum = 0
    cross2_sum = 0
    for i in range(100):
        cross_sum += arr[i][i]
        cross2_sum += arr[i][99-i]

    max_result = max(cross_sum,cross2_sum,max_result)
    
    print(f'#{tc} {max_result}')
    
    
