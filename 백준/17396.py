import heapq
import sys

N, M = map(int, sys.stdin.readline().split())
is_watched = list(map(int, sys.stdin.readline().split()))
is_watched[N-1] = 0
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, t = map(int, sys.stdin.readline().split())
    if is_watched[a] == 0 and is_watched[b] == 0:
        graph[a].append((b, t))
        graph[b].append((a, t))

def dijkstra():
    h = [(0, 0)]
    dist = [sys.maxsize] * (N+1)

    while h != []:
        now_dist, now = heapq.heappop(h)

        if now_dist >= dist[now]:
            continue

        dist[now] = now_dist

        for nt, next_dist in graph[now]:
            if next_dist + now_dist < dist[nt]:
                heapq.heappush(h, (next_dist + now_dist, nt))


    return dist

dist = dijkstra()

if dist[N-1] == sys.maxsize:
    print(-1)
else:
    print(dist[N-1])




