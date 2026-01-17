import sys
import pprint

N = int(sys.stdin.readline().strip())
jobs = []
for i in range(N):
    t, p = map(int, sys.stdin.readline().strip().split())
    jobs.append((t, p))


# idx : (day)
# val : 최대 이익
dp_table = [0] * (N+1)
for i in range(1, N+1):
    dp_table[i] = max(dp_table[i], dp_table[i-1])
    due = i + jobs[i-1][0] - 1
    if due <= N:
        dp_table[due] = max(dp_table[due], dp_table[i-1] + jobs[i-1][1])

print(dp_table[N])


