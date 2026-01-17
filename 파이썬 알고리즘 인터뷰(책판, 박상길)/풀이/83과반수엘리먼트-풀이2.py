import collections


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counts = collections.defaultdict(int)
        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)

            if counts[num] > len(nums) //2:
                return num