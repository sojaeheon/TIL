import sys
sys.stdin = open('sample_input.txt','r')


# 한 사람이 여러 장의 종이를 제출하거나 여러 사람이 한 사람을 지목한 경우 모두 같은 조가 된다.


def make_set(n):
    return [ i for i in range(n+1)]


def find_set_pc(x):
    
    # 자기 자신이 대표이면
    if parent[x] == x:
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
    n, m = map(int,input().strip().split())
    student_pair = list(map(int,input().strip().split()))

    parent = make_set(n)
    
    for i in range(0,len(student_pair),2):
        x, y = student_pair[i], student_pair[i+1]
        union(x,y)

    for i in range(n+1):
        find_set_pc(i)

    count = len(set(parent))-1

    print(f'#{tc} {count}')