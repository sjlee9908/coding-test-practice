import sys

N = int(sys.stdin.readline())
score_table = []


for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    score_table.append(row)

ex_min_table = score_table[0][:]
ex_max_table = score_table[0][:]

min_table = [sys.maxsize] * 3
max_table = [-sys.maxsize] * 3

for n in range(1, N):
    min_table = [sys.maxsize] * 3
    max_table = [-sys.maxsize] * 3
    for i in range(3):
        min_list = []
        max_list = []

        for ex_i in range(max(i-1, 0), min(i+1, 2) + 1):
            min_list.append(ex_min_table[ex_i] + score_table[n][i])
            max_list.append(ex_max_table[ex_i] + score_table[n][i])

        min_table[i] = min(
            min_table[i], *min_list
        )

        max_table[i] = max(
            max_table[i], *max_list
        )
    ex_min_table = min_table
    ex_max_table = max_table

print(max(ex_max_table), min(ex_min_table))