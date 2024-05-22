import heapq
import sys


def get_min_electric(slimes):
    electric = 1
    heapq.heapify(slimes)
    while len(slimes) > 1:
        s1 = heapq.heappop(slimes)
        s2 = heapq.heappop(slimes)

        heapq.heappush(slimes, s1 * s2)

        electric *= (s1 * s2)
        electric %= 1000000007

    return electric



T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    slimes = list(map(int, sys.stdin.readline().split()))
    print(get_min_electric(slimes))