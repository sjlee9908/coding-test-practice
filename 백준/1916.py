#input
import collections
import heapq
import sys

# input
n = int(input())
m = int(input())

graph = collections.defaultdict(list)

for i in range(m):
    n1, n2, w = map(int, input().split())
    heapq.heappush(graph[n1], (w, n2))

start_n, end_n = map(int, input().split())

#processing
now_n = start_n
total_weight = collections.defaultdict(lambda: sys.maxsize)
total_weight[start_n] = 0

#다익스트라수행
while n != 0:
    for bus in graph[now_n]:
        if bus[0] + total_weight[now_n] < total_weight[bus[1]]:
            total_weight[bus[1]] = bus[0] + total_weight[now_n]
    if graph[now_n]:
        get_bus = heapq.heappop(graph[now_n])
        now_n = get_bus[1]
    else:
        n -= 1
        now_n = start_n


#output
print(total_weight[end_n])



