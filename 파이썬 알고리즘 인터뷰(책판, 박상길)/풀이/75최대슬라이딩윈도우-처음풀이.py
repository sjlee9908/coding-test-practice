class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        now_max = max(nums[0:k])
        res.append(now_max)

        for i in range(1, len(nums)-k+1):
            if now_max == nums[i-1]:
                now_max = max(nums[i:k+i])
                res.append(now_max)
            elif now_max >= nums[i+k-1]:
                res.append(now_max)
            elif now_max < nums[i+k-1]:
                now_max = nums[i+k-1]
                res.append(now_max)

        return res