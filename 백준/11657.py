import sys

N, M = map(int, sys.stdin.readline().split())
edges = []
for _ in range(M):
    A, B, C = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    edges.append((A, B, C+1))

def bf():
    dist = [sys.maxsize] * N
    dist[0] = 0

    for i in range(N):
        for edge in edges:
            from_n, to_n, w = edge
            if dist[from_n] != sys.maxsize and dist[to_n] > dist[from_n] + w:
                dist[to_n] = dist[from_n] + w
                if i == N-1:
                    print(-1)
                    exit(0)

    return dist

dist = bf()
for to, w in enumerate(dist):
    if to != 0:
        if w != sys.maxsize:
            print(w)
        else:
            print(-1)