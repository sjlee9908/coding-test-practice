class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()

        i, j = 0, 0
        cookie_child = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                cookie_child += 1
                i += 1
                j += 1
            elif g[i] > s[j]:
                j += 1

        return cookie_child


