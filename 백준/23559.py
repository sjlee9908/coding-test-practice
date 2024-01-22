import collections
import heapq
import math
import sys

# input
n, m = map(int, sys.stdin.readline().split())
menu = collections.deque()
taste = []
total_taste = 0

for i in range(n):
    m5000, m1000 = map(int, sys.stdin.readline().split())
    menu.append((m5000, m1000))
    heapq.heappush(taste, (-abs(m5000-m1000), i))

# processing
while n > 0 and m >= 1000:
    select_taste = heapq.heappop(taste)
    menu_idx = select_taste[1]
    if m >= 5000 and menu[menu_idx][0] > menu[menu_idx][1]:
        total_taste += menu[menu_idx][0]
        m -= 5000
    else:
        total_taste += menu[menu_idx][1]
        m -= 1000
    n -= 1

# output
print(total_taste)