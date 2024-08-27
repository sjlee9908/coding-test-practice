import sys

N = int(sys.stdin.readline())
colors = list(sys.stdin.readline().split())
M, K  = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(M)]
for _ in range(K):
    A, B, C  = sys.stdin.readline().split()
    A, B = int(A)-1, int(B)-1
    graph[A].append((B, C))
    graph[B].append((A, C))

dp_table = [[-1] * N for _ in range(K)]

def dfs(pos, n):
    if n >= len(colors):
        return 0

    if dp_table[pos][n] != -1:
        return dp_table[pos][n]

    tmp_dp= 0
    for next_pos, color in graph[pos]:
        tmp = 0
        if color == colors[n]:
            tmp = 10
        tmp_dp = max(dfs(next_pos, n+1) + tmp, tmp_dp)

    dp_table[pos][n] = tmp_dp

    return dp_table[pos][n]

print(dfs(0, 0))