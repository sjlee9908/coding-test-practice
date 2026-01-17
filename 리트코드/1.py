import collections


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = collections.defaultdict(collections.deque)

        for idx, num in enumerate(nums):
            num_dict[num].append(idx+1)

        for num in nums:
            num_idx1 = num_dict[num].pop()
            if len(num_dict[(target - num)]) != 0:
                num_idx2 = num_dict[(target - num)].pop()
                return [num_idx1-1, num_idx2-1]


print(Solution.twoSum(None, nums = [3,3], target = 6))
