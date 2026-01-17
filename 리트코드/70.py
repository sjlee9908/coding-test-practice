class Solution:
    def __init__(self):
        self.tab = [None] * 100
        self.tab[0] = 0
        self.tab[1] = 1
        self.tab[2] = 2

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return self.tab[n]

        if self.tab[n] != None:
            return self.tab[n]

        self.tab[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.tab[n]


s = Solution()
print(s.climbStairs(3))






