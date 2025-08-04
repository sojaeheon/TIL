'''
아래와 같은 이진 트리가 있다면,
        'A'
       /   \
    'B'     'C'
    /  
  'D'
  /
'E'
'''
# 1번 index를 root로 설정하였을 때,
# 'A'의 왼쪽, 오른쪽 자식은 각각 2, 3 index에 해당함
# 'B'의 왼쪽, 오른쪽 자식은 각각 4, 5 index에 해당함
# 'D'의 왼쪽, 오른쪽 자식은? 

# 위 이진트리를 리스트로 나타낸다면
tree = [None,'A','B','C','D',None,None,None,'E',None,None,None,None,None,None,None]

print('존재하는 모든 요소 출력하기')

for index in range(1,2**4):
    if tree[index]:
        print(tree[index])


print('부모 찾기')
# 'E' 노드를 기준으로, 조상 노드를 찾으로 간다.
idx = 8
# 2진 트리에서 부모는, 내 인덱스를 2로 나눈 몫이면 부모다.
while idx>1:
  parent = tree[idx//2]
  print(parent,end=' ')
  idx//=2
print()


print('왼쪽 or 오른쪽 자식 찾기')
idx = 1

while idx < 8:
   left_child = tree[idx*2]
   right_child = tree[idx * 2+1]
   print(left_child)
   print(right_child)
   idx *=2
