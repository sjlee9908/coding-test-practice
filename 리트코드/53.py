class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = min(nums)
        now_sum = 0
        for num in nums:
            now_sum += num
            if max_sum < now_sum:
                max_sum = now_sum
            if now_sum < 0:
                now_sum = 0

        return max_sum

nums = [1]
print(Solution.maxSubArray(None, nums))
