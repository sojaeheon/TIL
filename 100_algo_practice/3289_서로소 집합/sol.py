

def find_set(x):

    if parent[x] == x:
        return x
    parent[x] =find_set(parent[x])
    return parent[x]

def union(x,y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        parent[root_y] = root_x
    
T = int(input())

for tc in range(1,T+1):

    # 1 <= n <= 1,000,000, 1 <= m <= 100,000
    # m은 입력으로 주어지는 연산의 개수
    n,m = map(int,input().split())

    parent = [i for i in range(n+1)]

    result = ''

    for _ in range(m):
        command = list(map(int,input().split()))
        if command[0] == 0:
            union(command[1],command[2])
            find_set(command[1])
        else:
            root_x = find_set(command[1])
            root_y = find_set(command[2])
            if root_x == root_y:
                result = result+'1'
            else:
                result = result+'0'

    print(f'#{tc} {result}')
    