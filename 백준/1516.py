import sys

n = int(sys.stdin.readline())
graph = [None for _ in range(n)]
time = []
dp_table = [-1] * n

for v in range(n):
    li = list(map(lambda x: int(x)-1, sys.stdin.readline().split()))
    time.append(li[0] + 1)
    graph[v] = li[1:-1:]


def dfs(dest):
    if dp_table[dest] != -1:
        return dp_table[dest]

    if len(graph[dest]) == 0:
        return time[dest]

    dp_table[dest] = max(list(map(dfs, graph[dest]))) + time[dest]

    return dp_table[dest]

for v in range(n):
    print(dfs(v))