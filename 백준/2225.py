import sys

n, k = map(int, sys.stdin.readline().split())
dp_table = [[-1] * (k+1) for _ in range(n+1)]

def dfs(now_n, now_k):
    if dp_table[now_n][now_k] != -1:
        return dp_table[now_n][now_k]

    if now_k <= 1:
        return 1

    tmp = 0
    for i in range(now_n+1):
        tmp += dfs(now_n - i, now_k-1)

    dp_table[now_n][now_k] = tmp

    return dp_table[now_n][now_k]

print(dfs(n, k)%1000000000)
# for li in dp_table:
#     print(*li)



