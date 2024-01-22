# https://www.acmicpc.net/problem/11779
import collections
import sys

#input
N = int(sys.stdin.readline())
E = int(sys.stdin.readline())
graph = [[sys.maxsize] * N for _ in range(N)]

for _ in range(E):
    u, v, e = map(lambda x: int(x)-1, sys.stdin.readline().split())
    if graph[u][v] > e+1: #u에서 v로 가는 여러 경로가 있을 수 있음, 최소값으로만 저장
        graph[u][v] = e+1
start, end = map(lambda x: int(x)-1, sys.stdin.readline().split())

#process
def get_min(dist, found):
    mind = sys.maxsize
    minv = -1

    for v in range(N):
        if found[v] == False and mind > dist[v]:
            mind = dist[v]
            minv = v

    return minv

def dijkstra():
    dist = list(graph[start])
    dist[start] = 0
    path = [start] * N
    found = [False] * N
    found[start] = True

    for i in range(N):
        u = get_min(dist, found)
        found[u] = True

        for w in range(N):
            if not found[w]:
                if dist[u] + graph[u][w] < dist[w]:
                    dist[w] = dist[u] + graph[u][w]
                    path[w] = u  #다익스트라 경로 저장
    return dist, path  #dist와 path를 return

dist_list, path_list = dijkstra()

#큐에 end->start 경로를 넣음
path = collections.deque()
path.append(end+1)
now = path_list[end]
while now != start:
    path.append(now+1)
    now = path_list[now]
path.append(start+1)

#output
print(dist_list[end])
print(len(path))
while len(path) != 0: #큐를 pop해가며 출력
    now = path.pop()
    print(now, end = " ")



