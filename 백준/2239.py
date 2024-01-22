import collections

n, v = map(int, input().split())

coins = []
for i in range(n):
    coins.append(int(input()))

dp = collections.defaultdict(int)

def get_count(v):
    if v <= 0:
        return 0
    elif v == 1:
        return 1

    if dp[v] == None:
        dp[v] = get_count(v-1) + get_count(v-2)
    else:
        return dp[v]

print(get_count(v))




