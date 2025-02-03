import collections
import sys

N, K = map(int, sys.stdin.readline().split())


def bfs():
    que = collections.deque([(0, N)])
    visited = collections.defaultdict(lambda: False)
    count = 0
    dist = sys.maxsize

    while len(que) != 0:
        w, n = que.popleft()

        if n == K and w <= dist:
            count += 1
            dist = w
        elif w > dist:
            return dist, count

        if visited[n] == True:
            continue
        visited[n] = True

        for nxtn in [n + 1, n - 1, 2 * n]:
            if 0 <= nxtn <= 100000:
                que.append((w + 1, nxtn))


print(*bfs(), sep="\n")