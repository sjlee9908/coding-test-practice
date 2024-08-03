import sys

N, M, H = map(int, sys.stdin.readline().split())
blocks = []
dp_table = [[0] * N for _ in range(H + 1)]

for _ in range(N):
    block = [0]
    block.extend(list(map(int, sys.stdin.readline().split())))
    blocks.append(block)

for i in range(H+1):
    for j in range(N):
        for k in blocks[j]:
            if k == i and j == 0: dp_table[i][j] = 1
            elif j != 0: dp_table[i][j] += (dp_table[i-k][j-1])

print(dp_table[H][N-1] % 10007)






