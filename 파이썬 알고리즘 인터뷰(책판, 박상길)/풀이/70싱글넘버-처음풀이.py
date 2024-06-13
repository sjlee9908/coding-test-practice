import collections

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        counter: collections.Counter = collections.Counter(nums)
        for k, v in dict(counter).items():
            if v == 1:
               return k





Solution.singleNumber(0, [2,2,1])