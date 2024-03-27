# https://www.acmicpc.net/problem/11779
import collections
import heapq
import sys

#input
N = int(sys.stdin.readline())
E = int(sys.stdin.readline())
graph = [[sys.maxsize] * N for _ in range(N)]

for _ in range(E):
    u, v, e = map(lambda x: int(x)-1, sys.stdin.readline().split())
    if graph[u][v] > e+1: #u에서 v로 가는 여러 경로가 있을 수 있음, 최소값으로만 저장
        graph[u][v] = e+1
START, END = map(lambda x: int(x)-1, sys.stdin.readline().split())

#process
def dijkstra():
    dist = [sys.maxsize] * N
    path = [sys.maxsize] * N
    q = []
    heapq.heappush(q, (0, START))

    while q != []:
        w, v = heapq.heappop(q)

        if dist[v] < w:
            continue

        for to_v, to_w in enumerate(graph[v]):
            if to_w + w < dist[to_v]:
                dist[to_v] = to_w + w
                heapq.heappush(q, (dist[to_v], to_v))
                path[to_v] = v  #to_v를 가기 위해서는 v를 거쳐야함 = to_v로 가는 경로가 v때문에 갱신됨

    return dist, path


dist_list, path_list = dijkstra()

#큐에 end->start 경로를 넣음
path = collections.deque()
path.append(END+1)
now = path_list[END]
#도착지부터 출발지까지 역추적하며 deque에 push
while now != START:
    path.append(now+1)
    now = path_list[now]
path.append(START+1)

#output
print(dist_list[END])
print(len(path))
while len(path) != 0: #큐를 pop해가며 출력
    now = path.pop()
    print(now, end = " ")



