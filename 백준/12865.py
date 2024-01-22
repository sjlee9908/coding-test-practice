import collections

n, k = map(int, input().split())

items = []
for i in range(n):
    items.append(tuple(map(int, input().split())))

dp_table = [[-1] * (k + 1) for _ in range(n + 1)]

def dfs(now_n, now_w):
    if dp_table[now_n][now_w] != -1:
        return dp_table[now_n][now_w]

    if now_n == 0 or now_w == 0:
        return 0

    within = -1
    if now_w >= items[now_n-1][0]:
        within = dfs(now_n-1, now_w-items[now_n-1][0]) + items[now_n-1][1]

    dp_table[now_n][now_w] = max(within, dfs(now_n-1, now_w))

    return dp_table[now_n][now_w]

print(dfs(n, k))


