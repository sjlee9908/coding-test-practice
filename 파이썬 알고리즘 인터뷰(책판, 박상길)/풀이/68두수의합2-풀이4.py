import bisect

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            nums = numbers[k+1:]
            i = bisect.bisect_left(nums, expected)
            if i < len(nums) and numbers[i+k+1] == expected:
                return k+1, i+k+2