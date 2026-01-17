import itertools
import sys

N, M = map(int, sys.stdin.readline().split())
graph = []
chicks = []
houses = []

for i in range(N):
    li = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if li[j] == 2: chicks.append((i, j))
        elif li[j] == 1: houses.append((i, j))
    graph.append(li)

chicks_list = list(itertools.combinations(chicks, M))
mind = sys.stdin
d = sys.maxsize
for chicks in chicks_list:
    ds = [sys.maxsize] * len(houses)
    for chick in chicks:
        for idx, house in enumerate(houses):
            ds[idx] = min(ds[idx], abs(chick[0] - house[0]) + abs(chick[1] - house[1]))
    d = min(d, sum(ds))


print(d)