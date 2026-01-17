import sys

N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

def fw():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

fw()
for _ in range(M):
    A, B, C = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    if graph[A][B] <= C+1:
        print('Enjoy other party')
    else:
        print('Stay here')