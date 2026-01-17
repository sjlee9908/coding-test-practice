import sys

t = int(sys.stdin.readline())
for i in range(t):
    a = map(int, sys.stdin.readline().split())
    print(sorted(a, reverse=True)[2])
