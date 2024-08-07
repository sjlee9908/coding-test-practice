import collections
import heapq
import sys

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

s, t = map(int, sys.stdin.readline().split())

def dijkstra(start, target):
    heap = [(0, start)]
    dists = [sys.maxsize] * (N+1)

    while len(heap) != 0:
        d, n = heapq.heappop(heap)

        if dists[n] < d:
            continue

        dists[n] = d

        for new_n, new_d in graph[n]:
            if dists[new_n] >= new_d + d:
                heapq.heappush(heap, (new_d + d, new_n))


    return dists[target]


print(dijkstra(s, t))













