import collections
import sys

N, P, Q = map(int, sys.stdin.readline().split())
dp_table = collections.defaultdict(lambda : None)
dp_table[0] = 1



def dfs(n):
    if dp_table[n] != None:
        return dp_table[n]

    dp_table[n] = dfs(n//P) + dfs(n//Q)

    return dp_table[n]

print(dfs(N))


