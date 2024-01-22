import collections
import sys

N, E = map(int, sys.stdin.readline().split())
graph = [[None] * N for _ in range(N)]
for _ in range(E):
    u, v, e = map(lambda x: int(x)-1, sys.stdin.readline().split())
    graph[u][v] = e + 1

s = 1
t = 2
tree_

def bfs():
    que = collections.deque()
    que.append(t)

    while len(que) != 0:
        v = que.pop()






