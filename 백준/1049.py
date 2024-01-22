import collections
import heapq
import sys

# input
n, m = map(int, sys.stdin.readline().split())
brand_line_6 = []
brand_line_1 = []
total = []

for i in range(m):
    line_6, line_1 = map(int, sys.stdin.readline().split())
    heapq.heappush(brand_line_6, line_6)
    heapq.heappush(brand_line_1, line_1)


line_6 = heapq.heappop(brand_line_6)
line_1 = heapq.heappop(brand_line_1)

# process
line_6_count = n // 6
line_1_count = n % 6

total.append((line_6_count+1) * line_6)
total.append(line_6_count * line_6 + line_1_count * line_1)
total.append(n * line_1)

# output
print(min(total))




