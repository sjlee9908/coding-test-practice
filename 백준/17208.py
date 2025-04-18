import sys

N, M, K = map(int, sys.stdin.readline().split())
jobs = []
for _ in range(N):
    n, k = map(int, sys.stdin.readline().split())
    jobs.append((n, k))

