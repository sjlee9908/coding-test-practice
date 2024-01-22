import collections
import heapq


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = collections.deque()
        ans = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while len(stack) != 0 and temperatures[stack[-1]] < temp:
                pop_temp = stack.pop()
                ans[pop_temp] = idx - pop_temp
            stack.append(idx)

        return ans




