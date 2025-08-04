import sys
sys.stdin = open("input.txt", "r")

def inorder_traversal(idx,n):
    if idx <= n:
        inorder_traversal(idx*2,n)
        print(tree[idx][1],end='')
        inorder_traversal(idx*2+1,n)

for tc in range(1,11):
    n = int(input())
    tree=[None]+[list(input().strip().split()) for _ in range(n)]
    print(f'#{tc}',end=' ')
    inorder_traversal(1,n)
    print()
