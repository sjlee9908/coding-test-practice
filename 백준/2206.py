import collections
import sys

N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    li = sys.stdin.readline().rstrip()
    graph.append(li)

diff = [
    [1, 0],[-1, 0],[0, 1],[0, -1]
]
que = collections.deque([(0, 0, 0, 1)])
visited = [[[sys.maxsize] * M for _ in range(N)] for _ in range(2)]

while len(que) != 0:
    x, y, wall_broken, dist = que.popleft()

    if x == N - 1 and y == M - 1:
        print(dist)
        exit(0)

    if visited[wall_broken][x][y] == True:
        continue

    visited[wall_broken][x][y] = True

    for dx, dy in diff:
        if  0 <= x + dx < N and 0 <= y + dy < M:
            if wall_broken == 1:
                if graph[x + dx][y + dy] == "0":
                    que.append((x + dx, y + dy, 1, dist + 1))
            else:
                if graph[x + dx][y + dy] == "0":
                    que.append((x + dx, y + dy, 0, dist + 1))
                else:
                    que.append((x + dx, y + dy, 1, dist + 1))



print(-1)