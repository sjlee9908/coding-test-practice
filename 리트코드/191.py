class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            if n & 0b1 == 0b1:
                res += 1
            n >>= 1
        return res


print(Solution.hammingWeight(None, 11))