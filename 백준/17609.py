# input
import collections

n = int(input())
_s = collections.deque()

for i in range(n):
    _s.append(input())


# processing
def is_palindrome(s: str):
    if len(s) == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 0

    p1 = 0
    p2 = len(s) - 1
    while p1 <= p2:
        if s[p1] != s[p2]:
            if s[p1:p2] == s[p1:p2][::-1] or s[p1+1:p2+1] == s[p1+1:p2+1][::-1]:
                return 1
            else:
                return 2
        p1 += 1
        p2 -= 1
    return 0


# output
for i in _s:
    print(is_palindrome(i))
