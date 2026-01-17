import sys
import heapq


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
roads = []
total_cost = 0
for _ in range(M):
    src, dst, cost = map(int, sys.stdin.readline().split())
    heapq.heappush(graph[src], (cost, dst))
    heapq.heappush(graph[dst], (cost, src))
    heapq.heappush(roads, (cost, src, dst))
    total_cost += cost

def prim(start):
    visited = [False] * (N+1)
    visited[0] = visited[start] = True
    heap = []
    mst_cost = 0

    for road in graph[start]:
        heapq.heappush(heap, road)

    while len(heap) != 0:
        cost, dst = heapq.heappop(heap)

        if visited[dst] == True:
            continue

        mst_cost += cost
        visited[dst] = True

        for road in graph[dst]:
            heapq.heappush(heap, road)

    if all(visited) == True:
        return mst_cost
    else:
        return total_cost + 1

def kruskal():
    mst_cost = 0
    union = list(range(0, N+1))
    union[0] = -1
    sel_road = 0

    while sel_road + 1 != N:
        if len(roads) != 0: cost, src, dst = heapq.heappop(roads)
        else: return total_cost + 1

        while union[src] != src:
            src = union[src]

        while union[dst] != dst:
            dst = union[dst]

        # 같은 집합에 속해있는지 검사 -> 속하지 않았으면 신장트리에 간선 추가, 속해있으면, pass
        if src != dst:
            union[dst] = src
            sel_road += 1
            mst_cost += cost

    return mst_cost

# print(total_cost - prim(1))
print(total_cost - kruskal())