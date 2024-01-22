import collections
import copy


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        visited = collections.defaultdict(bool)
        graph = collections.defaultdict(list)
        ans = []

        for idx, num in enumerate(nums):
            graph[num] = nums[0:idx] + nums[idx + 1:]

        def dfs(n, now_ans):
            if visited[n]:
                return

            visited[n] = True
            now_ans.append(n)

            for next_num in graph[n]:
                dfs(next_num, now_ans)
            if len(now_ans) == len(nums):
                ans.append(copy.deepcopy(now_ans))

            now_ans.pop()
            visited[n] = False


        for start_n in nums:
            dfs(start_n, [])

        return ans


print(Solution.permute(None, [1, 2, 3]))