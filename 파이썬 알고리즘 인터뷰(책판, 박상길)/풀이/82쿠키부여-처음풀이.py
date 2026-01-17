class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:

        if g == [] or s == []:
            return 0

        g.sort(reverse=True)
        s.sort(reverse=True)
        g_count = 0
        s_count = 0

        while g_count < len(g) and s_count < len(s):
            if g[g_count] > s[s_count]:
                g_count+=1
            else:
                s_count+=1
                g_count+=1

        return s_count