class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            c = s[p1]
            s[p1] = s[p2]
            s[p2] = c
            p1 += 1
            p2 -= 1