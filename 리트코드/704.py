class Solution:
    def search(self, nums: list[int], target: int) -> float:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            print(mid)
            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                right = mid - 1

            else:  # nums[mid] < target
                left = mid + 1
        return -1

print(Solution.search(None, [-1,0,3,5,9,12], 15))