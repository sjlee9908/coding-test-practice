import collections


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        visited = collections.defaultdict(bool)
        graph = collections.defaultdict()
        ans = []

        for i in range(n):
            graph[i + 1] = list(range(n + 1))[i + 2:]

        def dfs(start_num, now_ans):
            if visited[start_num]:
                return

            visited[start_num] = True
            now_ans.append(start_num)
            if len(now_ans) == k:
                ans.append(now_ans[:])

            for next_num in graph[start_num]:
                dfs(next_num, now_ans)

            now_ans.pop()
            visited[start_num] = False

        for i in range(1, n+1):
            dfs(i, [])

        return ans