import collections

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        result = []
        window = collections.deque()

        current_max = float('-inf')

        for i, v in enumerate(nums):
            window.append(v)
            if i < k-1:
                continue

            if current_max == float('-inf'):
                current_max = max(window)
            elif v > current_max:
                current_max = v

            result.append(current_max)

            if current_max == window.popleft():
                current_max = float('-inf')

        return result


