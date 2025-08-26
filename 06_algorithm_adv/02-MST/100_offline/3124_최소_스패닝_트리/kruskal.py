import sys
sys.stdin = open("input.txt")

def find_set(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find_set(parent, parent[x])
    return parent[x]

def union_sets(parent, x, y):
    root_x = find_set(parent, x)
    root_y = find_set(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x
        return True
    return False

def kruskal():
    edges.sort()
    parent = list(range(V + 1))
    total_weight = 0
    edge_count = 0

    for weight, u, v in edges:
        if find_set(parent, u) != find_set(parent, v):
            union_sets(parent, u, v)
            total_weight += weight
            edge_count += 1
            if edge_count == V - 1:
                break
    
    return total_weight

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        n1, n2, weight = map(int, input().split())
        edges.append((weight, n1, n2))
    
    result = kruskal()
    print(f"#{tc} {result}")