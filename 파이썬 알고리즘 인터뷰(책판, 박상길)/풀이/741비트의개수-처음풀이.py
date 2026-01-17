class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        for i in str(bin(n)):
            if i == '1':
                res += 1
        return res