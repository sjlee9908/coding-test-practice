import sys

N = int(sys.stdin.readline())
lines = [(0,0)]
for _ in range(N):
    lines.append(tuple(map(int, sys.stdin.readline().split())))

dp_table = [sys.maxsize] * N

