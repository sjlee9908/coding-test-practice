import math
import sys

dp_table = [0] * (2 ** 15)
dp_table[1] = 1


def dfs(n, t):
    if t > 4:
        return 0

    if n == 0:
        return 1

    if dp_table[n] != 0:
        return dp_table[n]

    m = int(n ** (1/2)) + 1
    for i in range(1, m):
        dp_table[n] += dfs(n - i**2, t+1)

    return dp_table[n]


while True:
    N = int(sys.stdin.readline())
    if N == 0: break
    print(dfs(N, 0))






