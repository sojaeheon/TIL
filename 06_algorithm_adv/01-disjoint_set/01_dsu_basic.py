"""
기본적인 서로소 집합 자료구조
- 각 집합은 트리 형태로 표현
- parent[i] = j는 'i의 부모는 j'를 의미
- 자기 자신이 부모인 경우 그 원소가 집합의 대표자
"""

def make_set(n):
    '''
        n : 집합을 만든 원소의 개수
    '''
    # 우선은 자기 자신을 대표자(부모)로 하는 배열 반환
    return [i for i in range(n+1)]


def find_set(x):
    '''
        원소 x가 속한 집합의 대표자가 누구인지 반환한다.
    '''

    # 원소 x가 속한 집합의 대표자
    if x == parent[x]: 
        return parent[x]
    
    # 아닐때
    return find_set(parent[x])

def union(x,y):
    '''

        x, y : 합쳐질 두 집합의 원소
        union 과정에 삽입 대상 원소는 그 원소의 집합의 대표자가 아닐 수 있음

    '''
    root_x = find_set(x)
    root_y = find_set(y)
    # 두 집합을 합친다
    # 두 원소가 속한 집합의 대표자가 서로 다르다면?
    if root_x != root_y:
    # 원소 y가 속한 집합의 대표자를 x로 바꾸거나
        parent[root_y] = root_x
    # 아니야!
    # 두 원소의 대표자가 같으면 이미 원래 두 원소는 같은 집합 소속인거임

   

# 각 원소드이 가지고 있는 값이 중요하다면,
# 각 원소들이 가진 값들을 부모 정보를 기입할 배열과 동일한 크기로 미리 작성
    #    0  1   2   3   4   5   6
tree = [ 0,'a','b','c','d','e','f']

# 6개의 원소로 테스트
parent = make_set(6)
print(f"초기 상태: {parent}")

# 긴 트리를 만들어 비효율성 확인
union(5, 6)
print(f"연산 후 상태: {parent}")
union(4, 5)
print(f"연산 후 상태: {parent}")
union(3, 4)
print(f"연산 후 상태: {parent}")
union(2, 3)
print(f"연산 후 상태: {parent}")
union(1, 2)

print(f"연산 후 상태: {parent}")