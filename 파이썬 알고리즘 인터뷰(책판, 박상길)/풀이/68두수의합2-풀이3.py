import bisect

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers[k+1:], expected)
            if i < len(numbers[k+1:]) and numbers[i+k+1] == expected:
                return k+1, i+k+2