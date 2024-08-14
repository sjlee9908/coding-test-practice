import sys
sys.setrecursionlimit(10 ** 5)

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    li = list(map(int, sys.stdin.readline().split()))
    graph.append(li)

diff = [
    [1, 0], [0, 1], [-1, 0], [0, -1]
]

max_v = -sys.maxsize
visited = [[False] * N for _ in range(N)]
dp_table = [[0] * N for _ in range(N)]

def dfs(x, y):
    if dp_table[x][y] != 0:
        return dp_table[x][y]

    visited[x][y] = True

    tmp = 0
    for dx, dy in diff:
        if 0 <= x + dx < N and 0 <= y + dy < N and graph[x][y] < graph[dx+x][dy + y] and visited[dx+x][dy+y] == False:
            tmp = max(tmp, dfs(x + dx, y + dy))

    dp_table[x][y] = tmp + 1
    visited[x][y] = False

    return dp_table[x][y]

ans = 0
for x in range(N):
    for y in range(N):
        ans = max(ans, dfs(x, y))

print(ans)
