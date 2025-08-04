# 완전 이진 트리 기준 순회

# 전위 순회
def preorder_traversal(idx):
    # 어디까지 순회해야하나?
    # 순회 대상이 범위를 벗어나지 않았다면!
    if idx<=N:
        # 전위 순회는 부모 노드를 먼저 조사한다
        print(tree[idx])
        # 이제 왼쪽 서브 트리에 대해서도 동일한 조건
        preorder_traversal(idx*2)
        # 이제 오른쪽 서브 트리에 대해서도 동일한 조건
        preorder_traversal(idx*2+1)

# 중위 순회
def inorder_traversal(idx):
    if idx <=N:
        inorder_traversal(idx*2)
        print(tree[idx])
        inorder_traversal(idx*2+1)

# 후위 순회
def postorder_traversal(idx):
    
    if idx<=N:
        postorder_traversal(idx*2+1)
        postorder_traversal(idx*2)
        print(tree[idx])

N = 5
tree = [0, 'A', 'B', 'C', 'D', 'E']


'''
    트리 구조
        'A'
      /   \
   'B'    'C'
  /   \
'D'    'E'
'''

print('전위 순회')
preorder_traversal(1)  # 'A' 'B' 'D' 'E' 'C'
print('중위 순회')
inorder_traversal(1)  # 'D' 'B' 'E' 'A' 'C'
print('후위 순회')
postorder_traversal(1)  # 'D' 'E' 'B' 'C''A'