# https://www.acmicpc.net/problem/1719
import copy
import sys

N, M = map(int, sys.stdin.readline().split())
graph = [[sys.maxsize] * (N) for _ in range(N)]
path =  [[None] * (N) for _ in range(N)]
for _ in range(M):
    u, v, e = map(lambda x: int(x)-1, sys.stdin.readline().split())
    graph[u][v] = e+1
    graph[v][u] = e+1
    path[u][v] = v
    path[v][u] = u

def fw():
    dist = copy.deepcopy(graph)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = k

def print_path():
    for i in range(N):
        for j in range(N):
            if i == j: print("-", end =" ")
            else: print(path[i][j] + 1, end = " ")
        print()

def post_process_path():
    for i in range(N):
        for j in range(N):
            dst = j
            stopover = path[i][j]
            while dst != stopover:
                dst = stopover
                stopover = path[i][stopover]
            path[i][j] = stopover

fw()
post_process_path()
print_path()