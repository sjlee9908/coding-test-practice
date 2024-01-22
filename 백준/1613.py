# https://www.acmicpc.net/problem/1613
import sys

n, k = map(int, sys.stdin.readline().split())
graph = [[False] * n for _ in range(n)]

for i in range(k):
    u, v = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    graph[u][v] = True

def fw():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] == False:
                    graph[i][j] = (graph[i][k] and graph[k][j])

fw()

test_case = int(sys.stdin.readline())
for i in range(test_case):
    u, v = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    if graph[u][v] == True: print(-1)
    elif graph[v][u] == True: print(1)
    else: print(0)
