import collections
import sys

N = int(sys.stdin.readline())
skyline = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    skyline.append((x, y))

skyline.append((sys.maxsize, 0))

buildings = 0
stk = collections.deque()
for x, y in skyline:
    if len(stk) == 0:
        stk.append(y)

    else:
        while len(stk) != 0 and stk[-1] > y:
            stk.pop()
            buildings += 1

        if len(stk) != 0 and stk[-1] == y:
            continue
        else:
            stk.append(y)


print(buildings)









