import sys

N = int(sys.stdin.readline())
graph = []
min_dp = [-1] * N
max_dp = [-1] * N
for _ in range(N):
    graph.append("".join(list(sys.stdin.readline().split())))


def max_dfs(n, pos):
    if n == -1 or pos <= -1 or pos >= N:
        return 0

    if dp_table[n][pos] != -1:
        return dp_table[n][pos]

    dp_table[n][pos] = max(max_dfs(n-1, pos - 1), max_dfs(n-1, pos), max_dfs(n-1, pos + 1)) + int(graph[n][pos])

    return dp_table[n][pos]


def min_dfs(n, pos):
    if pos <= -1 or pos >= N:
        return sys.maxsize

    if n == -1:
        return 0

    if dp_table[n][pos] != -1:
        return dp_table[n][pos]

    dp_table[n][pos] = min(min_dfs(n-1, pos - 1), min_dfs(n-1, pos), min_dfs(n-1, pos + 1)) + int(graph[n][pos])

    return dp_table[n][pos]

max_v = -1
dp_table = [[-1] * N for _ in range(N)]
for i in range(N):
    max_v = max(max_v, max_dfs(N-1, i))


min_v = sys.maxsize
dp_table = [[-1] * N for _ in range(N)]
for i in range(N):
    min_v = min(min_v, min_dfs(N-1, i))

print(max_v, min_v)