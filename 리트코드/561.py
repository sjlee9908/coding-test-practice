class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        return sum(nums[::2])


print(Solution.arrayPairSum(None, [1,4,3,2]))