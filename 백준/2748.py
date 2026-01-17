import sys

n = int(sys.stdin.readline())
dp_table = [-1] * 100
dp_table[0] = 0
dp_table[1] = 1

def dfs(now_n):
    if dp_table[now_n] != -1:
        return dp_table[now_n]

    dp_table[now_n] = dfs(now_n-1) + dfs(now_n-2)

    return dp_table[now_n]

print(dfs(n))