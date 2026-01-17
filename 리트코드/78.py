import collections


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = [[]]
        graph = collections.defaultdict(list)

        for i, n in enumerate(nums):
            graph[n] = nums[i+1:]

        print(graph)

        def dfs(now_ans, now_n):
            ans.append(now_ans[:])

            for next_n in graph[now_n]:
                now_ans.append(next_n)
                dfs(now_ans, next_n)
                now_ans.pop()

        for n in nums:
            dfs([n], n)

        return ans


print(Solution.subsets(None, [1,2,3]))