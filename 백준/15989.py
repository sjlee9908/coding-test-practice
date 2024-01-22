# https://www.acmicpc.net/problem/2294
import collections
import sys

sys.setrecursionlimit(99999)

t = int(sys.stdin.readline())

def get_num(num):
    if num <= 3:
        return num

    if dp_table[num] != 0:
        return dp_table[num]

    dp_table[num] =(
            get_num(num-3) + num //2 + 1
    )


    return dp_table[num]



for _ in range(t):
    dp_table = [0] * 10001
    num = int(sys.stdin.readline())
    print(get_num(num))