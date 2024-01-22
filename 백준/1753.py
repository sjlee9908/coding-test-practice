import heapq
import sys

v, e = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for _ in range(v+1)]
dist = [9999999999] * (v+1)

for _ in range(e):
    from_n, to_n, w = map(int, sys.stdin.readline().split())
    graph[from_n].append((to_n, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q != []:
        w, v = heapq.heappop(q)
        if dist[v] < w:
            continue
        for u, next_w in graph[v]:
            new_w = w + next_w
            if new_w < dist[u]:
                dist[u] = new_w
                heapq.heappush(q, (new_w, u))

dijkstra(start)

for i in range(1, v+1):
    if i == start:
        print(0)
    elif dist[i] != 9999999999:
        print(dist[i])
    else:
        print("INF")




