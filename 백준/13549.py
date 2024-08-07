import collections
import sys

N, K = map(int, sys.stdin.readline().split())
que = collections.deque()
min_t = sys.maxsize
que.append((N, 0))
visited = collections.defaultdict(lambda : sys.maxsize)

while len(que) != 0:
    n, t = que.popleft()

    if visited[n] <= t:
        continue
    visited[n] = t

    if n == K:
        min_t = min(t, min_t)

    if t <= min_t:
        if n > K and 1 <= n:
            que.append((n-1, t+1))
        else:
            if 1 <= n: que.append((n - 1, t + 1))
            if 1<= n <= 50000: que.append((2 * n, t))
            if n <= 99999: que.append((n + 1, t + 1))

print(min_t)