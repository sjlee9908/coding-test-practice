import sys

N = int(sys.stdin.readline())
dp_table = [sys.maxsize] * (N+1)

def dfs(n):
    if n == 0:
        return 0
    if n < 0:
        return sys.maxsize
    if dp_table[n] != sys.maxsize:
        return dp_table[n]

    dp_table[n] = min(dfs(n-3), dfs(n-5)) + 1

    return dp_table[n]

res = dfs(N)
if sys.maxsize <= res:
    print(-1)
else:
    print(res)
