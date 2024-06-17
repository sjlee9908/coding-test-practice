""""prim"""
import sys

#input
v_count = int(sys.stdin.readline())
e_count = int(sys.stdin.readline())
graph = [[sys.maxsize] * (v_count+1) for _ in range(v_count+1)]

for _ in range(e_count):
    u, v, e = map(int, sys.stdin.readline().split())
    graph[u][v] = e
    graph[v][u] = e


#process - prim
dist = [sys.maxsize] * (v_count+1)
dist[1] = 0
selected = [False] * (v_count+1)

#모든 노드 선택
for _ in range(v_count):
    #다음 노드 선정
    mind = sys.maxsize
    u = 0
    for i in range(1, v_count+1):
        if not selected[i] and dist[i] < mind:
            mind = dist[i]
            u = i
    selected[u] = True

    #간선리스트 갱신
    for v in range(1, v_count+1):
        if selected[v] == False and graph[u][v] < dist[v]:
            dist[v] = graph[u][v]

#output
#임의로 추가한 dist[0]은 제외
print(sum(dist[1:]))
