import collections
import sys

n = int(sys.stdin.readline())
dp_table = collections.defaultdict(lambda : -1)
dp_table[2] = 3
dp_table[4] = 11

def dfs(n):
    if dp_table[n] != -1:
        return dp_table[n]

    if n <= 0:
        return 0

    if n % 2 == 1:
        return 0

    dp_table[n] = dfs(n-2) * 4 - dfs(n-4)

    return dp_table[n]

print(dfs(n))