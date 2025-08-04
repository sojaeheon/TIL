import sys
sys.stdin = open("sample_input.txt", "r")

def postorder_traversal(idx):
    if idx <= n:
        if tree[idx] == None:
            x = postorder_traversal(idx*2) 
            y= postorder_traversal(idx*2+1)
            x = x if x != None else 0
            y = y if y != None else 0
            tree[idx]= x+y
            return tree[idx]
        else:
            return tree[idx]
        

T = int(input())

for tc in range(1, T + 1):
    # n 노드의 개수, m 리프 노드의 개수, l 값을 출력할 노드 번호
    n, m, l = map(int,input().strip().split())
    tree = [None] * (n+1)
    
    for _ in range(m):
        idx, val = map(int,input().split())
        tree[idx] = val

    postorder_traversal(1)

    print(f'#{tc} {tree[l]}')
    