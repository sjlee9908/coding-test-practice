########################PRIM########################a
import heapq
import sys

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    graph[A - 1].append((C, B - 1))
    graph[B - 1].append((C, A - 1))

def prim():
    h = [(0, 0)]
    visited = [False] * N
    total_edge_weight = 0
    max_weight = -99

    while h != []:
        now_dist, now_node = heapq.heappop(h)

        if visited[now_node] == True:
            continue

        total_edge_weight += now_dist
        max_weight = max(max_weight, now_dist)

        for next_dist, next_node in graph[now_node]:
            if visited[next_node] == False:
                heapq.heappush(h, (next_dist, next_node))
        visited[now_node] = True
        #print(now_node, end= " ")

    return total_edge_weight, max_weight

total_edge_weight, max_weight = prim()
print(total_edge_weight - max_weight)



