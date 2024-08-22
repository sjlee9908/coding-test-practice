import sys

N, M, K = map(int, sys.stdin.readline().split())
graph = []


for _ in range(N):
    graph.append(sys.stdin.readline().rstrip())
word = sys.stdin.readline().rstrip()


diff = [
    [1, 0], [0, 1], [-1, 0], [0, -1]
]
dp_table = [[[-1] * len(word) for _ in range(M)] for _ in range(N)]
def dfs(x, y, length):

    if dp_table[x][y][length] != -1:
        return dp_table[x][y][length]

    if length == len(word) - 1 and word[length] == graph[x][y]:
        return 1

    if graph[x][y] != word[length]:
        return 0

    tmp = 0
    for i in range(1, K + 1):
        for dx, dy in diff:
            nx = dx * i + x
            ny = dy * i + y

            if 0 <= nx < N and 0 <= ny < M:
                tmp += dfs(nx, ny, length + 1)

    dp_table[x][y][length] = tmp
    return tmp

tmp = 0
for i in range(N):
    for j in range(M):
        tmp += dfs(i, j, 0)

print(tmp)