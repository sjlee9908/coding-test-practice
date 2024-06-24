import sys

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
dp_table = [0] * (N + 1)

for _ in range(M):
    pre, post = map(int, sys.stdin.readline().split())
    graph[post].append(pre)

def dfs(n):
    if graph[n] == []:
        dp_table[n] = 1

    if dp_table[n] != 0:
        return dp_table[n]

    tmp = 0
    for next_n in graph[n]:
        tmp = max(tmp, dfs(next_n))

    dp_table[n] = tmp + 1

    return dp_table[n]

for n in range(N+1):
    dfs(n)
print(*dp_table[1:])

