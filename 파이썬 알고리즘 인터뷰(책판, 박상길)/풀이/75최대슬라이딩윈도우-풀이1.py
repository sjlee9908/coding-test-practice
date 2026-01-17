class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if not nums:
            return nums

        r = []
        for i in range(len(nums)-k+1):
            r.append(max(nums[i:i+k]))

        return r