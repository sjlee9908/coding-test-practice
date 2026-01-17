import collections
import heapq
import sys

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
table = [[sys.maxsize] * N for _ in range(N)]

table[0][0] = 0

for i in range(N):
    for j in range(N):
        if 0 <= i - 1 < N and 0 <= j - 1 < N:
            table[i][j] = min(
                table[i-1][j] + (0 if graph[i][j] < graph[i-1][j] else graph[i][j] - graph[i-1][j] + 1),
                table[i][j-1] + (0 if graph[i][j] < graph[i][j-1] else graph[i][j] - graph[i][j-1] + 1)
            )
        elif 0 <= i - 1 < N and not(0 <= j - 1 < N):
            table[i][j] = table[i-1][j] + (0 if graph[i][j] < graph[i-1][j] else graph[i][j] - graph[i-1][j] + 1)
        elif not(0 <= i - 1 < N) and 0 <= j - 1 < N:
            table[i][j] = table[i][j-1] + (0 if graph[i][j] < graph[i][j-1] else graph[i][j] - graph[i][j-1] + 1)

# print(*table, sep = "\n")
print(table[N-1][N-1])