# https://www.acmicpc.net/problem/2629
import collections
import sys

wc = int(sys.stdin.readline())
ws = list(map(int, sys.stdin.readline().split()))
tc = int(sys.stdin.readline())
ts = list(map(int, sys.stdin.readline().split()))

w_counter = collections.Counter(ws)
dp_table = collections.defaultdict(lambda : "")


def get_yn(now_sum, now_t):
    if now_t > now_sum:
        dp_table[(now_sum, now_t)] = "N"
    if now_t == 0:
        dp_table[(now_sum, now_t)] = "Y"

    if dp_table[(now_sum, now_t)] != "":
        return dp_table[(now_sum, now_t)]


    for w in ws:
        if w_counter[w] > 0:
            w_counter[w] -= 1
            tmp = get_yn(now_sum - w , abs(now_t - w))
            w_counter[w] += 1
            dp_table[(now_sum, now_t)] = tmp
            if tmp == "Y":
                return tmp

    return "N"

for t in ts:
    print(get_yn(sum(ws), t), end = " ")

