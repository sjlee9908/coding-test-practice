class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []

        def dfs(new_target, now_ans, new_candidates):
            if new_target < 0:
                return

            if new_target == 0:
                ans.append(now_ans[:])
                return

            for i, n in enumerate(new_candidates):
                now_ans.append(n)
                dfs(new_target - n, now_ans, new_candidates[i::])
                now_ans.pop()

        dfs(target, [], candidates)
        return ans

print(Solution.combinationSum(None, [2,3,6,7], 7))