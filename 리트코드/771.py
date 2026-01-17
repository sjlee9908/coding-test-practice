import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = collections.Counter(stones)
        return sum([counter[x] for x in jewels])
