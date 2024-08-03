import collections
import sys

N = int(sys.stdin.readline())
tower = [sys.maxsize]
tower.extend(list(map(int, sys.stdin.readline().split())))
received_tower = [-1] *(N+1)

i = N
stk = collections.deque()

for i in range(N, -1, -1):
    while len(stk) != 0 and tower[stk[-1]] < tower[i]:
        idx = stk.pop()
        received_tower[idx] = i
    stk.append(i)

print(*received_tower[1:])








