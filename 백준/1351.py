import collections
import sys

N, P, Q = map(int, sys.stdin.readline().split())
dp_table = collections.defaultdict(lambda : None)  #기본값으로 None을 반환하는 dp_table
dp_table[0] = 1  #최초항은 1

#dfs(n)은
def dfs(n):
    if dp_table[n] != None:
        return dp_table[n]

    #점화식
    dp_table[n] = dfs(n//P) + dfs(n//Q)

    return dp_table[n]

print(dfs(N))