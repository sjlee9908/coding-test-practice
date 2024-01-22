import collections
import heapq

N = int(input())
classes = collections.deque()

for i in range(N):
    classes.append(tuple(map(int, input().split())))

classes = collections.deque(sorted(classes, key=lambda x: (x[0], x[1])))
room = [0]

for min_class in classes:
    min_room = heapq.heappop(room)

    if min_room <= min_class[0]:
        heapq.heappush(room, min_class[1])
    else:
        heapq.heappush(room, min_room)
        heapq.heappush(room, min_class[1])

print(len(room))





