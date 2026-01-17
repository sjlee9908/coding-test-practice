import heapq
import sys

n = int(sys.stdin.readline())
lectures= []
do_lecture = []

for _ in range(n):
    p, d = map(int, sys.stdin.readline().split())
    heapq.heappush(lectures, (d, p))

do_lecture_count = 0
while lectures != []:
    d, p = heapq.heappop(lectures)
    heapq.heappush(do_lecture, p)
    do_lecture_count += 1

    if d < do_lecture_count:
        heapq.heappop(do_lecture)
        do_lecture_count -= 1

print(sum(do_lecture))