import sys

#input
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = [[99999999] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(lambda x: int(x)-1, sys.stdin.readline().split())
    #도시간 여러 버스가 주어질 수 있음
    graph[a][b] = min(graph[a][b], c+1)

#process
def fw(graph):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

fw(graph)

#output
for i in range(n):
    for j in range(n):
        if i == j or graph[i][j] == 99999999:
            print(0, end = " ")
        else:
            print(graph[i][j], end = " ")
    print()
