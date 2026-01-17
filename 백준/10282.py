import collections
import heapq
import sys

#다익스트라
def dijkstra(start):
    que = []
    que.append((0, start))
    dist = [sys.maxsize] * (n+1)

    while len(que) != 0:
        now_time, now_com = heapq.heappop(que)

        if dist[now_com] < now_time:
            continue
        dist[now_com] = now_time

        for next_time, next_com in graph[now_com]:
            if dist[next_com] > next_time + dist[now_com]:
                heapq.heappush(que, (next_time + dist[now_com], next_com))

    return dist

#test case 개수 입력
TC = int(sys.stdin.readline())
for _ in range(TC):
    #input
    n, d, c = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        heapq.heappush(graph[b], (s, a))

    #process
    dist = dijkstra(c)
    count = 0
    max_d = 0

    #output
    for d in dist[1::]:
        if d != sys.maxsize:
            count += 1
            max_d = max(max_d, d)
    print(count, max_d)