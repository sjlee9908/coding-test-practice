import heapq
import sys

# input
N, M, X = map(int, sys.stdin.readline().split())
origin_graph = [[sys.maxsize] * N for _ in range(N)]  #원본 그래프
reversed_graph = [[sys.maxsize] * N for _ in range(N)]#역전 그래프

for _ in range(M):
    A, B, T = map(lambda x: int(x)-1, sys.stdin.readline().split())
    origin_graph[A][B] = T + 1  #원본그래프에 저장
    reversed_graph[B][A] = T + 1#역전그래프에 저장(출발, 도착지 반대로)


#process
#다익스트라 수행
def dijkstra(start, graph):
    q = []
    heapq.heappush(q, (0, start))
    dist = [sys.maxsize] * N
    dist[start] = 0

    while q != []:
        w, v = heapq.heappop(q)

        if dist[v] < w:
            continue

        for to_v, to_w in enumerate(graph[v]):
            if to_w + w < dist[to_v]:
                dist[to_v] = to_w + w
                heapq.heappush(q, (dist[to_v], to_v))

    return dist

#다익스트라 수행
go_dist = dijkstra(X-1, reversed_graph) #모든노드 -> X
turn_back_dist = dijkstra(X-1, origin_graph) #X -> 모든노드

#output
print(max(map(lambda x: go_dist[x] + turn_back_dist[x], range(N))))