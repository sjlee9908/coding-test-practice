import sys

N = 1000 - int(sys.stdin.readline().strip())
COIN = [500, 100, 50, 10, 5, 1]

COIN = sorted(COIN, reverse=True)
count = 0
for coin in COIN:
    count += (N // coin)
    N %= coin

print(count)

