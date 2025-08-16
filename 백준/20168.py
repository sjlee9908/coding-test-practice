import heapq
import sys

N, M, A, B, C = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    src, dst, cost = map(int, sys.stdin.readline().split())
    graph[dst].append((src, cost))
    graph[src].append((dst, cost))

def dijkstra(start, end, budget):
    visited = [False] * (N + 1)
    heap = [(0, 0, start)]
    now_cost = 0

    while len(heap) != 0:
        mc, nowc, src = heapq.heappop(heap)

        if nowc > budget: continue
        if src == end: return mc

        visited[src] = True

        for dst, c in graph[src]:
            if visited[dst] == False:
                heapq.heappush(heap, (
                    max(mc, c),
                    nowc + c,
                    dst
                ))
    return -1

print(dijkstra(A, B, C))














