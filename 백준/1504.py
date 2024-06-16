import heapq
import sys

#input
N, E = map(int, sys.stdin.readline().split())
graph = [[sys.maxsize] * (N) for _ in range(N)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c
a, b = map(lambda x: int(x)-1, sys.stdin.readline().split())

#다익스트라
def dijkstra(start):
    h = [(0, start)]
    dist = [sys.maxsize] * (N)
    path = [0] * N

    while h != []:
        now_dist, now = heapq.heappop(h)

        if dist[now] < now_dist:
            continue

        dist[now] = now_dist

        for to, to_dist in enumerate(graph[now]):
            if now_dist + to_dist < dist[to]:
                heapq.heappush(h, (now_dist + to_dist, to))
                dist[to] = now_dist + to_dist
                path[to] = now

    return dist, path

#거치는 노드를 check
def check_in(path, end, passby):
    while path[end] != 0:
        if end == passby:
            return True
        end = path[end]
    return False


#check
from_1_dist, from_1_path = dijkstra(0)
is_1a_in_b = check_in(from_1_path, a, b)
is_1b_in_a = check_in(from_1_path, b, a)

from_a_dist, from_a_path = dijkstra(a)
is_an_in_b = check_in(from_a_path, N-1, b)

from_b_dist, from_b_path = dijkstra(b)
is_bn_in_a = check_in(from_b_path, N-1, a)

ans = sys.maxsize

#각각의 경우를 check
if is_1a_in_b or is_an_in_b:
    ans = min(ans, from_1_dist[a] + from_a_dist[N-1])

if is_1b_in_a or is_bn_in_a:
    ans = min(ans, from_1_dist[b] + from_b_dist[N-1])

ans = min(ans, from_1_dist[a] + from_a_dist[b] + from_b_dist[N-1], from_1_dist[b] + from_b_dist[a] + from_a_dist[N-1])

#output
if ans >= sys.maxsize:
    print(-1)
else:
    print(ans)