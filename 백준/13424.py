import sys
import heapq

def djikstra(start):
    heap = [(0, start)]
    visited = [False] * N
    dist = [sys.maxsize] * N

    while len(heap) != 0:
        w, n = heapq.heappop(heap)
        if visited[n] == True or dist[n] < w:
            continue

        visited[n] = True
        dist[n] = w

        for nxtn, nxtw in graph[n]:
            if visited[nxtn] == False:
                heapq.heappush(heap, (w + nxtw, nxtn))

    return dist

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(lambda x:int(x)-1, sys.stdin.readline().split())
        graph[a].append((b, c + 1))
        graph[b].append((a, c + 1))
    _ = int(sys.stdin.readline())
    starts = list(map(lambda x:int(x)-1, sys.stdin.readline().split()))
    dists = []
    for start in starts:
        dists.append(djikstra(start))

    dist = [(sum(column), idx) for idx, column in enumerate(zip(*dists))]
    heapq.heapify(dist)
    print(dist[0][1] + 1)






