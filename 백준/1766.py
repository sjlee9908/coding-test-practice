import heapq
import sys

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
parent = [0] * (N + 1) #먼저 풀어야할 문제의 수
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B) #먼저 풀 문제 -> 나중에 풀 문제
    parent[B] += 1

#위상정렬
def topology_sort():
    #방문할 노드들이 저장된 heap
    que = []

    #먼저 방문할 노드들을 heap에 넣음
    for i in range(1, N+1):
        #먼저 풀어야할 문제의 수가 0이면 먼저 방문
        if parent[i] == 0:
            heapq.heappush(que, i)

    #que가 빌 때까지 반복
    while len(que) != 0:
        #방문
        v = heapq.heappop(que)
        print(v, end = " ")

        # 나중에 풀 문제의 parent 감소 & heap에다가 넣기
        for child in graph[v]:
            parent[child] -= 1
            if parent[child] == 0:
                heapq.heappush(que, child)


topology_sort()