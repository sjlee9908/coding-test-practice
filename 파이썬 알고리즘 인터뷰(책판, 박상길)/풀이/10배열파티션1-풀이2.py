class Solution:
    def Array_Partition(self, nums: list[int]) -> int:
        sum = 0
        nums.sort()
        for i, n in enumerate(nums):
            if i% 2 == 0:
                sum+=n
        return sum