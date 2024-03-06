# https://www.acmicpc.net/problem/6497
import collections
import heapq
import sys

#process
def prim(graph_):
    light_price = 0
    sel_count = 0
    dist_heap = []
    visited = [False] * len(graph_)
    heapq.heappush(dist_heap, (0, 0))

    while sel_count != len(graph_):
        price, sel_node = heapq.heappop(dist_heap)
        if visited[sel_node] == False:
            visited[sel_node] = True
            light_price += price
            sel_count += 1

            for to, price in graph_[sel_node].items():
                if price != sys.maxsize:
                    heapq.heappush(dist_heap, (price, to))

    return light_price

#input
ans_list = []

while True:
    m, n = map(int, sys.stdin.readline().split())
    graph = collections.defaultdict(lambda : collections.defaultdict())
    total_price = 0

    for _ in range(n):
        x, y, z = map(int, sys.stdin.readline().split())
        graph[x][y] = z
        graph[y][x] = z
        total_price += z

    if m == 0 and n == 0:
        print(*ans_list)
        break


    ans_list.append(total_price-prim(graph))