import collections
import re

s = input()

if "0" not in s:
    print(0)
    exit(0)

if "1" not in s:
    print(0)
    exit(0)

s = re.sub("0+", "0", s)
s = re.sub("1+", "1", s)
counter_01 = collections.Counter(s)
print(counter_01.most_common()[-1][1])