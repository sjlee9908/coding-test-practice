import sys

N, T = map(int, sys.stdin.readline().split())
graph = [[sys.maxsize] * N for _ in range(N)]
cities = []

for i in range(N):
    s, x, y = map(int, sys.stdin.readline().split())
    cities.append((s, x, y))

    for j, city in enumerate(cities):
        v = abs(x - city[1]) + abs(y - city[2])
        if s == 1 and city[0] == 1:
            graph[j][i] = graph[i][j] = min(T, v)
        else:
            graph[j][i] = graph[i][j] =  v

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]


M = int(sys.stdin.readline())
for _ in range(M):
    f, t = map(lambda x: int(x)-1, sys.stdin.readline().split())
    print(graph[f][t])