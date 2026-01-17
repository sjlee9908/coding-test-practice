import collections
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[0] * N for _ in range(N)]
lookup_table = [N-1] * N


for _ in range(M):
    #[A][B] = 1 : A가 B보다 무겁다,[A][B] = -1 : A가 B보다 가볍다
    small, big = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    graph[small][big] = 1
    graph[big][small] = -1


def fw():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][j] == 0:
                    if graph[i][k] == graph[k][j]:
                        graph[i][j] = graph[k][j]

fw()

for i in range(N):
    print(collections.Counter(graph[i])[0]-1)