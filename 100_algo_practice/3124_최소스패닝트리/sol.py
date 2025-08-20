import sys
sys.stdin = open("sample_input.txt",'r')

import heapq


# 최소신장트리 함수
def prim(vertices):
    # 가중치 합을 저장할 변수
    mst_weight = 0

    # 정점 방문처리 변수
    visited = set()

    # 시작할 정점 정해서
    start_vertex = vertices[0]

    # 현재 정점에서 방문할 수 있는 다음 정점을 가중치를 기준으로 우선순위 힙에 넣는다
    min_heap = [(w,e) for e,w in adj_list[start_vertex]]
    heapq.heapify(min_heap)

    # 현재 정점 방문처리
    visited.add(start_vertex)

    # 우선순위 힙이 있으면 반복
    while min_heap:
        # 다음 정점과 가중치를 뽑아서
        w,e = heapq.heappop(min_heap)

        # 다음 정점을 방문했으면 다른 정점 탐색
        if e in visited: continue

        #방문하지 않았으면 방문처리
        visited.add(e)
        mst_weight += w

        for next, weight in adj_list[e]:
            if next in visited: continue
            heapq.heappush(min_heap,(weight,next))

    return mst_weight

T = int(input())

for tc in range(1,T+1):

    # 정점의 개수 v, 간선의 개수 E
    v, e = map(int,input().split())

    # 현재 정점을 나타내는 변수
    vertices = [i for i in range(1,v+1)]

    # 그래프를 인접리스트로 저장
    adj_list = {
        v:[] for v in vertices
    }

    edges = []

    # 시작점, 끝 점, 가중치를 입력받아 인접리스트에 저장
    for _ in range(e):
        a,b,c = map(int,input().strip().split())
        edges.append([a,b,c])
        adj_list[a].append((b,c))
        adj_list[b].append((a,c))

    # prim알고리즘으로 최소 신장 트리의 가중치 합을 반환받기
    mst = prim(vertices)

    print(f'#{tc} {mst}')