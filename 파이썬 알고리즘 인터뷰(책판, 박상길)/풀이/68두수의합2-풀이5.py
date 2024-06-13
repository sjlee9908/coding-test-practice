import bisect

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers, expected, k+1)
            if i < len(numbers) and numbers[i] == expected:
                return k+1, i+1