import collections
import sys

sys.setrecursionlimit(10 ** 4)

num_string = sys.stdin.readline().rstrip()
dp_table = collections.defaultdict(lambda : -1)

for i in range(1, 11):
    dp_table[str(i)] = 1
for i in range(11, 27):
    dp_table[str(i)] = 2
dp_table["20"] = 1


def dfs(num_s):
    if num_s == '' or num_s[0] == '0':
        return 0

    if dp_table[num_s] != -1:
        return dp_table[num_s]

    tmp = 0
    if int(num_s[0:2]) <= 26:
        tmp += dfs(num_s[2::])
    tmp += dfs(num_s[1::])

    dp_table[num_s] = tmp % 1000000
    return dp_table[num_s]

print(dfs(num_string))
