import collections
import itertools
import sys

exp = sys.stdin.readline().rstrip()

stk = collections.deque()
brackets = []
res = set()

for idx, ch in enumerate(exp):
    if ch == "(": stk.append(idx)
    if ch == ")": brackets.append((stk.pop(), idx))

for i in range(1, len(brackets) + 1):
    li = list(itertools.combinations(brackets, i))
    for bracket in li:
        del_idx = [0] * 200
        s = ""

        for b in bracket:
            del_idx[b[0]] = 1
            del_idx[b[1]] = 1

        for idx, ch in enumerate(exp):
            if del_idx[idx] == 0: s += ch

        res.add(s)

print(*sorted(res), sep="\n")

