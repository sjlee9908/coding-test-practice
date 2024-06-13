import collections

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result  ^= num

        return result









Solution.singleNumber(0, [2,2,1])