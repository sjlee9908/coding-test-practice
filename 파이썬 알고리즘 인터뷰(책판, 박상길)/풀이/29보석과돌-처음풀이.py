import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = collections.Counter(stones)
        res = 0
        for i in jewels:
            res += counter[i]
        return res

sol = Solution()
print(sol.numJewelsInStones("aAdnnn", "aAAbbbb"))



