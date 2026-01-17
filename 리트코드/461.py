import collections

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ans = collections.deque()
        ans.append(max(nums[0:k]))

        for i in range(0, len(nums)-k):
            print(ans)
            if ans[-1] == nums[i-1]:
                ans.append(max(nums[i:i+k]))
            elif ans[-1] <= nums[i+k]:
                ans.append(nums[i+k])
            elif ans[-1] >= nums[i+k]:
                ans.append(ans[-1])
            else:
                ans.append(max(nums[i:i + k]))

        return list(ans)

print(Solution.maxSlidingWindow(None, [1,3,-1,-3,5,3,6,7] , 3))