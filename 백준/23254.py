import sys
import pprint
import heapq


N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

score_heap = []

for idx, enc in enumerate(b):
    if a[idx] != 100:
        heapq.heappush(score_heap, (-min(enc, 100-a[idx]), -idx))

for _ in range(N * 24):
    if len(score_heap) != 0:
        enc, idx = heapq.heappop(score_heap)
        enc, idx = -enc, -idx

        if a[idx] <= 100:
            a[idx] = min(100, a[idx] + enc)
            heapq.heappush(score_heap, (-min(enc, 100-a[idx]), -idx))

print(sum(a))
