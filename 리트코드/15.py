class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []

        if len(nums) < 3:
            return []

        for i in range(len(nums) - 2):
            left = i+1
            right = len(nums) - 1

            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum == 0 and \
                        [nums[i], nums[left], nums[right]] not in ans:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    right -=1
        return ans




print(Solution.threeSum(None, [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))
