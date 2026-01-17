import heapq
import sys

#input
v, e = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for _ in range(v+1)]
dist = [9999999999] * (v+1)

for _ in range(e):
    from_n, to_n, w = map(int, sys.stdin.readline().split())
    graph[from_n].append((to_n, w))

#process
def dijkstra(start):
    #heap을 사용한 다익스트라
    q = []
    heapq.heappush(q, (0, start))  #시작정점 삽입
    dist[start] = 0 #거리 초기화
    
    #heap이 빌 때까지 수행
    while q != []:
        #heap에서 가장 작은 (거리, 정점)을 뺌
        w, v = heapq.heappop(q)
        #만약, dist[v]가 기존 거리보다 작으면, (거리, 정점)은 유효하지 않음
        if dist[v] < w:
            continue
        #새로운 (가중치, 정점)을 heap에 삽입
        for u, next_w in graph[v]:
            new_w = w + next_w
            if new_w < dist[u]:
                dist[u] = new_w
                heapq.heappush(q, (new_w, u))

dijkstra(start)

#output
for i in range(1, v+1):
    if i == start:
        print(0)
    elif dist[i] != 9999999999:
        print(dist[i])
    else:
        print("INF")




