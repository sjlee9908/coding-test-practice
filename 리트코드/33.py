import collections


class Solution:
    def search(self, nums: list[int], target: int) -> float:
        nums = collections.deque(nums)
        idx = 0
        while nums[-1] < nums[0]:
            nums.rotate(-1)
            idx += 1

        print(nums)
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            print(mid)
            if nums[mid] == target:
                return (mid + idx) % len(nums)

            elif nums[mid] > target:
                right = mid - 1

            else:  # nums[mid] < target
                left = mid + 1
        return -1

print(Solution.search(None, [4,5,6,7,0,1,2], 0))