import sys
sys.stdin = open("input.txt", "r")

# 정점이 정수면 정점 번호와 양의 정수가 주어지고
# 정점이 연산자이면 정점 번호, 연산자, 해당 정점의 왼쪽 자식, 오른쪽자식의 정점 번호가 차례대로 주어진다

# 사칙연산 수행 함수
def operating(x,op,y):
    if op == '+':
        return x+y
    elif op == '-':
        return x-y
    elif op == '*':
        return x*y
    elif op == '/':
        return x//y

# 연산자 확인 함수
def oper_check(data):
    op = {'+','-','*','/'}
    return data in op

# 전위순회 함수
def preorder_traversal(idx):
    # 노드의 수만큼 실행
    if idx <= n:
        # 현재 값을 받을 변수
        value = tree[idx][1]
        # 현재값이 연산자일 때
        if oper_check(value):
            # 왼쪽 트리의 값 호출
            x = preorder_traversal(int(tree[idx][2]))
            # 오른쪽 트리 값 호출
            y = preorder_traversal(int(tree[idx][3]))
            # 연산 수행
            return operating(x,value,y)
        # 현재 값이 정수일대
        else:
            # 값 리턴
            return int(value)


for tc in range(1, 11):
    n = int(input())
    tree = [None]*(n+1)
    
    for idx in range(1,n+1):
        tree[idx] = list(input().strip().split())
    
    result = preorder_traversal(1)

    print(f'#{tc} {result}')

