# https://www.acmicpc.net/problem/13911
import collections
import heapq
import sys

V, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(V+3)]
for i in range(E):
    u, v, e = map(int, sys.stdin.readline().split())
    graph[u].append((v, e))
    graph[v].append((u, e))
M, x = map(int, sys.stdin.readline().split())
M_vertex = list(map(int, sys.stdin.readline().split()))
S, y = map(int, sys.stdin.readline().split())
S_vertex = list(map(int, sys.stdin.readline().split()))

macV = V+1
starV = V+2
for i in M_vertex:
    graph[macV].append((i, 0))
    graph[i].append((macV, 0))
for i in S_vertex:
    graph[starV].append((i, 0))
    graph[i].append((starV, 0))

V += 3
def dijkstra(start, limit):
    hq = []
    cost = [sys.maxsize] * V
    cost[start] = 0
    heapq.heappush(hq, [0, start])

    while hq:
        dist, u = heapq.heappop(hq)
        if cost[u] != dist: continue
        if dist > limit: break

        for v, e in (graph[u]):
            if v == macV or v == starV: continue

            if cost[v] > dist + e:
                cost[v] = dist + e  # nx비용 초기화
                heapq.heappush(hq, [cost[v], v])

    return cost

M_list = dijkstra(macV, x)
S_list = dijkstra(starV, y)

mind = sys.maxsize
for i in range(1, V-3+1):
    if i in M_vertex: continue
    if i in S_vertex: continue
    if M_list[i] <= x and S_list[i] <= y:
        mind = min(mind, M_list[i] + S_list[i])

if mind == sys.maxsize:
    print(-1)
else:
    print(mind)