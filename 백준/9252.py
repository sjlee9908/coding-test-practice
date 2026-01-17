import sys

sys.setrecursionlimit(99999)

p = sys.stdin.readline().rstrip()
q = sys.stdin.readline().rstrip()

m = len(p)
n = len(q)
dp_table = [[None] * (n + 1) for _ in range(m + 1)] # 테이블 생성
for i in range(m+1):
    for j in range(n+1):
        if i == 0 or j == 0:
            dp_table[i][j] = 0
        elif p[i-1] == q[j-1]:
            dp_table[i][j] = dp_table[i-1][j-1]+1
        else:
            dp_table[i][j] = max(dp_table[i-1][j], dp_table[i][ j-1])

length = dp_table[len(p)-1][len(q)-1]
lcs = "" # ①
i = len(p) # ②
j = len(q) # ②
while i > 0 and j > 0:
    v = dp_table[i][j]
    if v > dp_table[i][j-1] and v > dp_table[i-1][j] and v > dp_table[i-1][j-1]: # ③
        i -= 1
        j -= 1
        lcs = p[i] + lcs
    elif v == dp_table[i][j-1] and v > dp_table[i-1][j]:
        j -= 1
    else:
        i -= 1
print(len(lcs))
print(lcs)
