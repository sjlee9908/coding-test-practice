import sys

N, M, R = map(int, sys.stdin.readline().split())
T = list(map(int, sys.stdin.readline().split()))
graph = [[sys.maxsize] * N for _ in range(N)]

for _ in range(R):
    A, B, L = map(int, sys.stdin.readline().split())
    graph[A-1][B-1] = L
    graph[B-1][A-1] = L

def fw():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][j] >= graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

for i in range(N):
    for j in range(N):
        if i == j: graph[i][i] = 1
        else:
            if graph[i][j] <= M: graph[i][j] = 1
            else: graph[i][j] = 0

v = 0
for i in range(N):
    tmp = 0
    for j in range(N):
        if graph[i][j] == 1:
            tmp += T[j]
    v = max(tmp, v)

print(v)




