import sys
sys.setrecursionlimit(10**5)

N, R, Q = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]
dp_table = [0] * (N)

for _ in range(N-1):
    U, V = map(lambda x: int(x)-1, sys.stdin.readline().split())
    graph[U].append(V)
    graph[V].append(U)

def dfs(from_node, now_node):
    if dp_table[now_node] != 0:
        return dp_table[now_node]

    tmp = 1
    for next_node in graph[now_node]:
        if next_node != from_node:
            tmp += dfs(now_node, next_node)

    dp_table[now_node] = tmp
    return tmp

dfs(-1, R-1)
#print(*dp_table)
for _ in range(Q):
    node = int(sys.stdin.readline())-1
    print(dp_table[node])
