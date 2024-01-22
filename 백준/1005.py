import sys

def dfs(dest):
    if dp_table[dest] != -1:
        return dp_table[dest]

    if graph[dest] == []:
        return construct_time[dest]

    tmp = 0
    for ex_build in graph[dest]:
        tmp = max(tmp, dfs(ex_build))
    dp_table[dest] = tmp + construct_time[dest]


    return dp_table[dest]


t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    construct_time = list(map(int, sys.stdin.readline().split()))
    graph = [[] for _ in range(n)]
    dp_table = [-1] * n

    for _ in range(k):
        x, y = map(lambda x: int(x)-1, sys.stdin.readline().split())
        graph[y].append(x)

    dest = int(sys.stdin.readline()) - 1
    print(dfs(dest))