import sys

n, m, r = map(int, sys.stdin.readline().split())
t = list(map(int, sys.stdin.readline().split()))
graph = [[sys.maxsize] * n for _ in range(n)]

for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    graph[a - 1][b - 1] = l
    graph[b - 1][a - 1] = l

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

maxt = t[:]
for i in range(n):
    for j in range(n):
        if i == j : continue
        if graph[i][j] <= m:
            maxt[i] += t[j]

# print(*graph)
# print(maxt)
print(max(maxt))








