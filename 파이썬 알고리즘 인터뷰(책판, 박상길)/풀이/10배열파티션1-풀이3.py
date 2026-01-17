class Solution:
    def Array_Partition(self, nums: list[int]) -> int:
        return sum(sorted(nums)[::2])