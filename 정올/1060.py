import sys
import heapq


N = int(sys.stdin.readline())
edges = []

for f in range(N):
    edge = list(map(int, sys.stdin.readline().split()))
    for t in range(N):
        if f > t:
            heapq.heappush(edges, (edge[t], f, t))

parent = [_ for _ in range(N)]
loss = 0

while len(edges) != 0:
    weight, f, t = heapq.heappop(edges)

    while parent[f] != f: f = parent[f]
    while parent[t] != t: t = parent[t]

    if f == t:
        continue
    
    parent[t] = f
    loss += weight

print(loss)
