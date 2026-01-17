import collections
import sys
sys.setrecursionlimit(10 ** 4)

dp_table = collections.defaultdict(lambda : None)

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1


    if dp_table[(a,b,c)] != None:
        return dp_table[(a,b,c)]

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if a < b < c:
        dp_table[(a,b,c)] =  w(a, b, c - 1) + w(a, b-1, c-1) - w(a, b-1, c)

    else:
        dp_table[(a,b,c)] =  w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

    return dp_table[(a,b,c)]

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == -1: break
    print("w(%d, %d, %d) = %d"% (a, b, c, w(a, b, c)))


