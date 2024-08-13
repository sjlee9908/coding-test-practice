import sys

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    li = list(map(int, sys.stdin.readline().split()))
    graph.append(li)

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 1 and graph[i][k] == 1 and graph[k][j]:
                graph[i][j] = 1




for i in range(N):
    for j in range(N):
        print(graph[i][j], end = " ")
    print()
