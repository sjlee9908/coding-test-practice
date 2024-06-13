import heapq
import sys

N, E = map(int, sys.stdin.readline().split())
graph = [[sys.maxsize] * (N) for _ in range(N)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c
a, b = map(lambda x: int(x)-1, sys.stdin.readline().split())

def dijkstra(start):
    heap = []
    heap.append((0, start))
    dist = [sys.maxsize] * (N)
    path = [0] * N

    while heap != []:
        now_dist, now = heapq.heappop(heap)

        if dist[now] < now_dist:
            continue

        dist[now] = now_dist

        for to, to_dist in enumerate(graph[now]):
            if now != to and now_dist + to_dist < dist[to]:
                heapq.heappush(heap, (now_dist + to_dist, to))
                dist[to] = now_dist + to_dist
                path[to] = now

        return dist, path

def check_in(path, end, passby):
    while path[end] != 0:
        if end == passby:
            return True
        end = path[end]
    return False

simple_graph = [[sys.maxsize] * 4 for _ in range(4)]

from1_dist, from1_path = dijkstra(0)
froma_dist, froma_path = dijkstra(a)
fromb_dist, fromb_path = dijkstra(b)

inA = check_in(from1_path, b, a)
if inA:
    simple_graph[0][1] = from1_dist[a]
    simple_graph[1][2] = froma_dist[b]
else:
    simple_graph[0][1] = from1_dist[a]
    simple_graph[0][2] = from1_dist[b]

inB = check_in(from1_path, a, b)
if inB:
    simple_graph[0][2] = from1_dist[b]
    simple_graph[2][1] = fromb_dist[a]
else:
    simple_graph[0][1] = from1_dist[a]
    simple_graph[0][2] = from1_dist[b]

###########
inA = check_in(froma_path, N-1, a)
if inA:
    simple_graph[0][1] = from1_dist[a]
    simple_graph[1][2] = froma_dist[b]
else:
    simple_graph[0][1] = from1_dist[a]
    simple_graph[0][2] = from1_dist[b]

inB = check_in(froma_path, N-1, a)
if inB:
    simple_graph[0][2] = from1_dist[b]
    simple_graph[2][1] = fromb_dist[a]
else:
    simple_graph[0][1] = from1_dist[a]
    simple_graph[0][2] = from1_dist[b]


