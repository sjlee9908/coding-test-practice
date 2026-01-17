import collections
import sys

N = int(sys.stdin.readline())
vp = []
for _ in range(N):
    n, p = map(int, sys.stdin.readline().split())
    vp.append((n, p))

vp.sort()
print(vp)
cost = [0] * (N)
lcost = 0
rcost = 0
for i in range(N):
    cost[i] += (lcost + vp[i-1][1]) * abs(vp[i][0] - vp[i-1][0])
    lcost = (lcost + vp[i-1][1]) * abs(vp[i][0] - vp[i-1][0])

    cost[N-1-i] += (rcost + vp[N-1-i][1]) * abs(vp[N-1-i][0] - vp[N-1-i-1][0])
    rcost = (rcost + vp[N-1-i][1]) * abs(vp[N-1-i][0] - vp[N-1-i-1][0])
    # print("asdf", vp[N-1-i][0] - vp[N-1-i-1][0])
    print(lcost, rcost)

print(cost)

cost = sys.maxsize
post = None
for i in range(N):
    if cost > rcost[i] + lcost[i]:
        cost = rcost[i] + lcost[i]
        post = i

print(post + 1)


