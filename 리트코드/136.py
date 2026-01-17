import collections


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        counter = collections.Counter(nums)
        li = counter.most_common()
        return li[-1][0]