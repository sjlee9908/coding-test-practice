import heapq
import sys

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
parent = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    parent[B] += 1

# def topology_sort():
#     problem = []
#     solved = [False] * (N + 1)
#     i = 1
#     while len(problem) != N:
#         if parent[i] == 0 and solved[i] == False:
#             problem.append(i)
#             solved[i] = True
#             for child in graph[i]:
#                 parent[child] -= 1
#             i = 0
#
#         i += 1
#         i %= (N+1)
#
#
#     return problem

def topology_sort():
    que = []

    for i in range(1, N+1):
        if parent[i] == 0:
            heapq.heappush(que, i)

    while len(que) != 0:
        v = heapq.heappop(que)
        print(v, end = " ")

        for child in graph[v]:
            parent[child] -= 1
            if parent[child] == 0:
                heapq.heappush(que, child)


print(*topology_sort())