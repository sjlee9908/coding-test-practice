import collections
import sys

sys.setrecursionlimit(100000)
n, m = map(int, input().split())

tree = collections.defaultdict(collections.deque)
good_word = collections.defaultdict(int)
n_list = list(map(int, input().split()))

for i, v in enumerate(n_list[1:]):
    tree[v].append(i + 2)

for j in range(m):
    i, w = map(int, input().split())
    good_word[i] += w


def dfs(i):
    if i == 0:
        return
    for j in tree[i]:
        good_word[j] += good_word[i]
        dfs(j)


dfs(1)

for i in range(1, n + 1):
    print(good_word[i], end=" ")
