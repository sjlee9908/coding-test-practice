import bisect


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        pivot = nums.index(min(nums))
        new_nums = []

        for i in range(pivot, len(nums)):
            new_nums.append(nums[i])

        for i in range(pivot):
            new_nums.append(nums[i])

        index = bisect.bisect_left(new_nums, target)
        if index < len(new_nums) and new_nums[index] == target:
            return (index + pivot) % len(new_nums)
        else:
            return -1
