import collections
import heapq
import sys

# input
n = int(sys.stdin.readline())
distances = [int(sys.stdin.readline()) for i in range(n)]

max_distance = sum(distances)
all_distance = collections.defaultdict(int)
p1_to_p2 = 0

for p1_idx, p1 in enumerate(distances):
    for p2_idx, p2 in enumerate(distances):
        p1_to_p2
        all_distance[(p1_idx, p2_idx)] = min(max_distance - p1_to_p2, p1_to_p2)




