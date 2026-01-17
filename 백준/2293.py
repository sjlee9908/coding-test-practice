import sys

N, K = map(int, sys.stdin.readline().split())
coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))

dp_table = [0] * (K+1)
dp_table[0] = 1

for coin in coins:
    for now_k in range(K+1):
        if now_k - coin >= 0:
            dp_table[now_k] += dp_table[now_k - coin]


print(dp_table[K])