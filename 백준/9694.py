import sys
import heapq


def dijkstra():
    heap = [(0, 0)]
    path = []

    while len(heap) != 0:
        n, c = heapq.heappop(heap)
        path.append(n)

        for nextn, costc in enumerate(graph[n]):





T = int(sys.stdin.readline())
for t in range(T):
    N, M = map(int, sys.stdin.readline().split())
    graph = [[sys.maxsize] * M for _ in range(M)]
    for _ in range(N):
        x, y, z = map(int, sys.stdin.readline().split())
        graph[x][y] = min(graph[x][y], z)
        # graph[y][z] = min(graph[z][y], z)

    print(f'Case #{t+1}: {*}')