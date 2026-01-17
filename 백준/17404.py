# https://www.acmicpc.net/problem/17404
import collections
import sys

n = int(sys.stdin.readline())
w = collections.deque()
w.append(0)
for i in range(n):
    w.append(list(map(int, sys.stdin.readline().split())))

#     1   2   3   4   5   6   7 ... n
# R:0
# G:1
# B:2

def RGB_distance(now_n, now_c):
    if now_n == 1:
        if last == now_c:
            return sys.maxsize
        else:
            return w[1][now_c]

    if dp_table[now_n][now_c] != 0:
        return dp_table[now_n][now_c]

    tmp = sys.maxsize
    for i in range(3):
        if i != now_c:
            tmp = min(tmp, RGB_distance(now_n - 1, i) + w[now_n][now_c])
    dp_table[now_n][now_c] = tmp

    return dp_table[now_n][now_c]


dp_table = collections.defaultdict(lambda : collections.defaultdict(int))
last = 0
a = RGB_distance(n, 0)

dp_table = collections.defaultdict(lambda : collections.defaultdict(int))
last = 1
b = RGB_distance(n, 1)

dp_table = collections.defaultdict(lambda : collections.defaultdict(int))
last = 2
c = RGB_distance(n, 2)
print(min(a, b, c))
        
    