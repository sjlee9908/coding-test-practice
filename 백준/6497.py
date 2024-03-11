# https://www.acmicpc.net/problem/6497
import collections
import heapq
import sys

#process
def prim(graph_):
    light_price = 0 #현재까지의 비용
    sel_count = 0 #선택된 노드의 수
    dist_heap = [] #거리 측정용 힙
    visited = [False] * len(graph_) #장소 기록
    heapq.heappush(dist_heap, (0, 0)) #초기화

    #모든 노드를 선택할때 까지 반복
    while sel_count != len(graph_):
        price, sel_node = heapq.heappop(dist_heap) #선택

        if visited[sel_node] == False: #선택 X
            visited[sel_node] = True #선택
            light_price += price
            sel_count += 1

            #거리갱신
            for to, price in graph_[sel_node].items():
                if price != sys.maxsize:
                    heapq.heappush(dist_heap, (price, to))

    return light_price

#input
ans_list = []

while True:
    #m, n을 입력받음
    m, n = map(int, sys.stdin.readline().split())
    graph = collections.defaultdict(lambda : collections.defaultdict())
    total_price = 0

    #간선 입력받음
    for _ in range(n):
        x, y, z = map(int, sys.stdin.readline().split())
        graph[x][y] = z
        graph[y][x] = z
        total_price += z

    #만약 m, n이 0이면 출력하고 종료
    if m == 0 and n == 0:
        print(*ans_list)
        break

    #0 0이 아니면 절약비용을 계산해 append
    ans_list.append(total_price-prim(graph))