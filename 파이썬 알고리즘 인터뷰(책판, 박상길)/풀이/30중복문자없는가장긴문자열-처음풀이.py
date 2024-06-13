import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                counter = collections.Counter(s[i:j+1])
                if counter.most_common()[0][1] >= 2:
                    break
                else:
                    res = max(res, len(s[i:j+1]))
        return res

sol = Solution()
print(sol.lengthOfLongestSubstring("pwwkew"))