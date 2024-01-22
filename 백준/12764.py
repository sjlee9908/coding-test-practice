# import collections
# import heapq
#
# N = int(input())
# com_time = collections.deque()
#
# for i in range(N):
#     com_time.append(tuple(map(int, input().split())))
#
# com_time = collections.deque(sorted(com_time, key=lambda x: (x[0], x[1])))
# com_using = collections.defaultdict(int)
# com_used = collections.defaultdict(int)
# com = [1000001]
#
#
# for min_time in com_time:
#     min_com = heapq.heappop(com)
#     ex_min = min_com
#
#     while min_com < min_time[0]:
#         min_com = heapq.heappop(com)
#         ex_min = min_com
#
#     heapq.heappush(com, min_com)
#
#     if ex_min <= min_time[0]:
#         heapq.heappush(com, min_time[1])
#         com_using[min_time[1]] = com_using[ex_min]
#     else:
#         heapq.heappush(com, ex_min)
#         heapq.heappush(com, min_time[1])
#         com_using[min_time[1]] = len(com)-1
#
#     com_used[com_using[min_time[1]]] += 1
#
#
# print(com_using)
# print(com_used)
#
# print(len(com_used.keys()))
# for i in com_used.keys():
#     print(com_used[i], end=" ")


import collections
import heapq

N = int(input())
com_time = collections.deque()

for i in range(N):
    com_time.append(tuple(map(int, input().split())))

com_time = collections.deque(sorted(com_time, key=lambda x: (x[0], x[1])))
com_using = collections.defaultdict(int)
com_used = collections.defaultdict(int)
com = [1000001]


for min_time in com_time:
    min_com = heapq.heappop(com)
    ex_min = min_com

    while min_com < min_time[0]:
        min_com = heapq.heappop(com)
        ex_min = min_com

    heapq.heappush(com, min_com)

    if ex_min <= min_time[0]:
        heapq.heappush(com, min_time[1])
        com_using[min_time[1]] = com_using[ex_min]
    else:
        heapq.heappush(com, ex_min)
        heapq.heappush(com, min_time[1])
        com_using[min_time[1]] = len(com)-1

    com_used[com_using[min_time[1]]] += 1


print(com_using)
print(com_used)

print(len(com_used.keys()))
for i in com_used.keys():
    print(com_used[i], end=" ")
