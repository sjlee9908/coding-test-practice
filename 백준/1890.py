import collections
import sys

N = int(sys.stdin.readline())
graph = [[] for _ in range(N)]
for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    graph[i] = line

dp_table = [[0] * N for _ in range(N)]
dp_table[0][0] = 0

def dfs(y, x):
    if y >= N or x >= N:
        return 0
    if y == N-1 and x == N-1:
        return 1
    if graph[y][x] == 0:
        return 0

    if dp_table[y][x] != 0:
        return dp_table[y][x]

    dp_table[y][x] = dfs(y, x + graph[y][x]) + dfs(y + graph[y][x], x)
    return dp_table[y][x]

print(dfs(0, 0))