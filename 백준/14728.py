import sys

N, T = map(int, sys.stdin.readline().split())
chapters = []
for _ in range(N):
    K, S = map(int, sys.stdin.readline().split())
    chapters.append((K, S))
dp_table = [[-1] * (T+1) for _ in range(N+1)]

def dfs(now_n, now_t):
    if now_n < 0:
        return 0

    if dp_table[now_n][now_t] != -1:
        return dp_table[now_n][now_t]

    if now_t >= chapters[now_n][0]:
        dp_table[now_n][now_t] = max(dfs(now_n-1, now_t - chapters[now_n][0]) + chapters[now_n][1],
                                     dfs(now_n-1, now_t))

    dp_table[now_n][now_t] = max(dp_table[now_n][now_t], dfs(now_n-1, now_t))

    return dp_table[now_n][now_t]

print(dfs(N-1, T))
