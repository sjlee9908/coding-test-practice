# https://www.acmicpc.net/problem/2661
import collections
import sys

n = int(sys.stdin.readline())
min_val = "9"* 80
val = ""

def dfs(level):
    global min_val
    global val

    if level == n:
        min_val = min(min_val, val)

    for num in ["1", "2", "3"]:
        bt = False
        tmp = val + num

        for i in range(0, level):
            if tmp[level-i : level+1] == tmp[level -i-1-i:level-i]:
                bt = True
                break

        if bt == True or (val != "" and val > min_val):
            continue

        tmp = val
        val = val + num
        dfs(level + 1)
        val = tmp


dfs(0)
print(min_val)

