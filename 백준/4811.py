import collections
import sys

sys.setrecursionlimit(100000)
dp_table = collections.defaultdict(lambda : -1)

def dfs(full_count, half_count):
    if dp_table[(full_count, half_count)] != -1:
        return dp_table[(full_count, half_count)]

    if half_count < 0 or full_count <0:
        return 0

    if full_count == 0 and half_count > 0:
        return 1

    dp_table[(full_count, half_count)] = (
            dfs(full_count-1, half_count+1) + dfs(full_count, half_count-1)
    )

    return dp_table[(full_count, half_count)]

while True:
    n = int(sys.stdin.readline())
    if n == 0: exit(0)
    print(dfs(n, 0))
