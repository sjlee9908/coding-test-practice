import heapq
import sys

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    heapq.heappush(graph[a], (c+1, b))
    heapq.heappush(graph[b], (c+1, a))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist = [sys.maxsize] * N
    dist[start] = 0

    while q != []:
        w, v = heapq.heappop(q)

        if dist[v] < w:
            continue

        for to_w, to_v in graph[v]:
            if dist[to_v] > w + to_w:
                dist[to_v] = w + to_w
                heapq.heappush(q, (dist[to_v], to_v))

    return dist



print(dijkstra(0)[N-1])