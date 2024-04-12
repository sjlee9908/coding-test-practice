import sys
sys.setrecursionlimit(10 ** 7)

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(sys.stdin.readline().rstrip())


def rg_not_same_dfs(x, y, color):
    if visited[x][y] == True:
        return

    if color == graph[x][y]:
        visited[x][y] = True
        for x_diff, y_diff in zip([-1, 0, 1, 0], [0, -1, 0, 1]):
            if 0 <= x+x_diff < N and 0 <= y+y_diff < N:
                rg_not_same_dfs(x+x_diff, y+y_diff, color)

def rg_same_dfs(x, y, color):
    if visited[x][y] == True:
        return

    if color == graph[x][y] or (color == "R" and graph[x][y] == "G") or (color == "G" and graph[x][y] == "R"):
        visited[x][y] = True
        for x_diff, y_diff in zip([-1, 0, 1, 0], [0, -1, 0, 1]):
            if 0 <= x+x_diff < N and 0 <= y+y_diff < N:
                rg_same_dfs(x+x_diff, y+y_diff, color)


rg_not_same_res = 0
visited = [[False] * N for _ in range(N)]
for x in range(N):
    for y in range(N):
        if visited[x][y] == False:
            rg_not_same_res += 1
            rg_not_same_dfs(x, y, graph[x][y])

rg_same_res = 0
visited = [[False] * N for _ in range(N)]
for x in range(N):
    for y in range(N):
        if visited[x][y] == False:
            rg_same_res += 1
            rg_same_dfs(x, y, graph[x][y])

print(rg_not_same_res, rg_same_res)

