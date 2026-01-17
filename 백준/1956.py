import sys

V, E = map(int, sys.stdin.readline().split())
graph = [[sys.maxsize] * V for _ in range(V)]
for _ in range(E):
    a, b, c= map(lambda x: int(x) - 1, sys.stdin.readline().split())
    graph[a][b] = c + 1

for k in range(V):
    for i in range(V):
        for j in range(V):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]


min_e = sys.maxsize
for i in range(V):
    for j in range(V):
        if i != j:
            min_e = min(min_e, graph[i][j] + graph[j][i])

if min_e == sys.maxsize:
    print(-1)
else:
    print(min_e)