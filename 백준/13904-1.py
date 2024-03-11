import heapq
import sys

n = int(sys.stdin.readline())
work_list = []
do_work_list = []

for _ in range(n):
    d, w = map(int, sys.stdin.readline().split())
    heapq.heappush(work_list, (d, w))

while work_list != []:
    d, w = heapq.heappop(work_list)
    heapq.heappush(do_work_list, w)

    if len(do_work_list) > d:
        heapq.heappop(do_work_list)

print(sum(do_work_list))

