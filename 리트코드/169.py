import collections


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums_collection = collections.Counter(nums)
        return nums_collection.most_common(1)[0][0]

