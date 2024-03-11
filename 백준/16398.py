# https://www.acmicpc.net/problem/16398
import heapq
import sys

#input
n = int(sys.stdin.readline())
flow_list = [] #간선을 저장할 힙(그래프)
for fr in range(n):
    flows = list(map(int, sys.stdin.readline().split()))

    for to, price in enumerate(flows):
        if fr < to:
            #양방향 그래프, 간선을 heap에 삽입
            heapq.heappush(flow_list, (price, fr, to))
            heapq.heappush(flow_list, (price, to, fr))


#process
union_set = list(range(n)) #사이클 확인용 set
selected_flow = 0
total_price = 0
while selected_flow != n - 1: #트리 생성시 까지 수행
    price, fr, to = heapq.heappop(flow_list) #heap에서 pop

    #fr의 부모
    while union_set[fr] != fr:
        fr = union_set[fr]

    #to의 부모
    while union_set[to] != to:
        to = union_set[to]

    #동일하다면 같은 사이클
    if fr != to:
        union_set[fr] = to
        selected_flow += 1
        total_price += price

#output
print(total_price)
