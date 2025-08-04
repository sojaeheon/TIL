import sys
sys.stdin = open("sample_input.txt", "r")

# 이진탐색트리 만들기
def make_bst(n):
    tree = [None]*(n+1)

    for num in range(1,n+1):
        if num == 1:
            tree[num] = num
        else:
            # 삽입하는 노드가 부모노드보다 클 경우
            if tree[num//2] < num:
                parent_idx = num//2
                while tree[parent_idx]
                tree[num//2], tree[num] = num, tree[num//2]
            else:
                tree[num] = num
            


T = int(input())

for tc in range(1, T+1):
    n = int(input())

    result = make_bst(n)
