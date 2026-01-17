import heapq
import sys

N = int(sys.stdin.readline())
jobs = []

for _ in range(N):
    d, t = map(int, sys.stdin.readline().split())
    jobs.append((t, d))

jobs.sort(reverse = True)

ex_start_day = sys.maxsize
start_day = None
for t, d in jobs:
    if ex_start_day <= t:
        t = ex_start_day - 1
    start_day = t - d + 1
    # print(ex_start_day, start_day)
    ex_start_day = start_day

print(start_day - 1)




