import heapq
import sys

V, E, P = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    graph[A].append((B, C))
    graph[B].append((A, C))


def dijkstra(start):
    heap = [(0, start)]
    dist = [sys.maxsize] * (V+1)
    path = [0] * (V+1)

    while len(heap) != 0:
        w, n = heapq.heappop(heap)

        if dist[n] < w:
            continue

        dist[n] = w

        for next_n, next_w in graph[n]:
            if w + next_w < dist[next_n]:
                heapq.heappush(heap, (w + next_w, next_n))
                path[next_n] = n

    return dist


from_1 = dijkstra(1)
from_P = dijkstra(P)

if from_1[P] + from_P[V] <= from_1[V]:
    print("SAVE HIM")
else:
    print("GOOD BYE")