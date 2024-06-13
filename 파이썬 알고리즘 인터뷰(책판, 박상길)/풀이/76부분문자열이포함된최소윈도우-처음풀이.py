import re


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        p = re.compile(".".split(t))
        m = p.match(s)

        if m:


