import sys
sys.stdin = open('s_input.txt','r')

# n 명의 사람

# 1번부터 n번까지 번호가 붙어있다

# 몇 개의 무리가 존재하는 지 계산하는 프로그램

def find_set_pc(x):
    if parent[x]==x:
        return x
    parent[x] = find_set_pc(parent[x])
    return parent[x]

def union(x,y):
    root_x = find_set_pc(x)
    root_y = find_set_pc(y)

    if root_x != root_y:
        parent[root_y] = root_x

T = int(input())

for tc in range(1,T+1):
    
    # 사람의 수 n, 서로 알고 있는 사람의 관계 수 m
    # 1<=n<=100, 0<= M <= N(N-1)2
    n,m = map(int,input().split())

    parent = [i for i in range(n+1)]
    
    for i in range(m):
        x,y = map(int,input().split())
        union(x,y)
        
    for i in range(1,n+1):
        find_set_pc(i)
    
    
    result = len(set(parent)) - 1

    print(f'#{tc} {result}')

