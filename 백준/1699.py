import math
import sys
sys.setrecursionlimit(10 ** 5)

N = int(sys.stdin.readline())
dp_table = [None] * (N+1)
dp_table[0] = 0

def dfs(n):
    if dp_table[n] != None:
        return dp_table[n]

    tmp = sys.maxsize
    lim = math.floor(n ** (1/2)) + 1
    for i in range(1, lim):
        tmp = min(tmp, dfs(n - (i ** 2)))
    dp_table[n] = tmp + 1

    return dp_table[n]

print(dfs(N))

