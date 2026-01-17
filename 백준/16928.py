import collections
import sys

N, M = map(int, sys.stdin.readline().split())
ladders = [0] * 107
snakes = [0] * 107

for _ in range(N):
    f, t = map(int, sys.stdin.readline().split())
    ladders[f] = t

for _ in range(M):
    f, t = map(int, sys.stdin.readline().split())
    snakes[f] = t


que = collections.deque([(1,0)])
visited = [False] * 107
while True:
    loc, count = que.popleft()

    if visited[loc] == True:
        continue

    if loc >= 100:
        print(count)
        exit(0)

    visited[loc] = True

    for i in range(1, 7):
        if ladders[loc+i] != 0:
            que.append((ladders[loc + i % 101], count + 1))

        elif snakes[loc+i] != 0:
            que.append((snakes[loc + i], count + 1))

        else:
            que.append((loc + i, count + 1))
