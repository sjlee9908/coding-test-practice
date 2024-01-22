#https://www.acmicpc.net/problem/2437
import sys

#input
n = int(sys.stdin.readline())
w = list(map(int, sys.stdin.readline().split()))

#processing
w.sort()
max_val = w[0]
if max_val != 1:
    print(1)
    exit(0)

for v in range(1, n):
    if max_val + 1 >= w[v]:  #새롭게 가능한 무게 중 최소은 w[v]
        max_val = max_val + w[v]
    else:
        break

#output
print(max_val + 1)