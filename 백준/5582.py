import sys

s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()
dp_table = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]
max_v = 0


for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            dp_table[i][j] = (dp_table[i-1][j-1] + 1)
            max_v = max(max_v, dp_table[i][j])


print(max_v)


