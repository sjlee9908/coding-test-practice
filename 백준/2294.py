# https://www.acmicpc.net/problem/2294
import collections
import sys

sys.setrecursionlimit(99999)

n, k = map(int, sys.stdin.readline().split())
coin_list = set()
for _ in range(n):
    coin = int(sys.stdin.readline())
    coin_list.add(coin)
dp_table = collections.defaultdict(lambda : -1)

def dfs(value_sum):
    global dp_table

    if value_sum < 0:
        return 999999

    if dp_table[value_sum] != -1:
        return dp_table[value_sum]

    if value_sum == 0:
        return 0

    dp_table[value_sum] = 999999
    for coin in coin_list:
        dp_table[value_sum] = min(dp_table[value_sum], dfs(value_sum - coin) + 1)

    return dp_table[value_sum]

res = dfs(k)
if res == 999999:
    print(-1)
else:
    print(res)