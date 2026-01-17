import collections

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)



sol = Solution()
print(sol.numJewelsInStones("aAdnnn", "aAAbbbb"))



