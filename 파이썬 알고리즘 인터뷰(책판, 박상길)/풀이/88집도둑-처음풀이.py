import collections


class Solution:
    dp = collections.defaultdict(int)

    def rob(self, nums: list[int]) -> int:
        if nums == []:
            return 0

        if dp[n] == 0:
            dp[n] = rob()
