import heapq
import sys

diff = [
    [1, 0],[-1, 0],[0, 1],[0, -1]
]


def dijkstra():
    heap = [(graph[0][0], 0, 0)]
    dist = [[sys.maxsize] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    while len(heap) != 0:
        w, x, y = heapq.heappop(heap)

        if visited[x][y] == True:
            continue

        dist[x][y] = w
        visited[x][y] = True

        for dx, dy in diff:
            if 0 <= x + dx < N and 0 <= y + dy < N:
                if dist[x + dx][y + dy] > w + graph[x + dx][y + dy]:
                    heapq.heappush(heap,(w + graph[x + dx][y + dy], x + dx, y + dy))

    return dist

i = 1
while True:
    N = int(sys.stdin.readline())
    if N == 0: break
    graph = []

    for _ in range(N):
        li = list(map(int, sys.stdin.readline().split()))
        graph.append(li)

    dist = dijkstra()

    print(f"Problem {i}: {dist[N-1][N-1]}")
    i += 1