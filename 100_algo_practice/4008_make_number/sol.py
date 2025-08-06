import sys
sys.stdin = open("sample_input.txt", "r")

def change_oper(op):
    arr = []
    for _ in range(op[0]):
        arr.append('+')
    for _ in range(op[1]):
        arr.append('-')
    for _ in range(op[2]):
        arr.append('*')
    for _ in range(op[3]):
        arr.append('/')
    return arr

def dfs(depth,result,n):
    global min_number,max_number
    
    
    
    if depth == len(numbers):
        min_number = min(min_number,result)
        max_number = max(max_number,result)
        return

    for i in range(n):
        if visited[i] and oper_arr[i] == '+':
            visited[i] = False
            dfs(depth+1,result+numbers[depth],n)
            visited[i] = True

        if visited[i] and oper_arr[i] == '-':
            visited[i] = False
            dfs(depth+1,result-numbers[depth],n)
            visited[i] = True

        if visited[i] and oper_arr[i] == '*':
            visited[i] = False
            dfs(depth+1,result*numbers[depth],n)
            visited[i] = True

        if visited[i] and oper_arr[i] == '/':
            visited[i] = False
            dfs(depth+1,int(result/numbers[depth]),n)
            visited[i] = True


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    oper_arr = change_oper(list(map(int,input().strip().split())))
    numbers = list(map(int,input().strip().split()))

    oper_num = len(oper_arr)
    visited = [True] * oper_num

    max_number = float('-inf')
    min_number = float('inf')

    dfs(1,numbers[0],oper_num)

    print(f'#{tc} {max_number-min_number}')



    