import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        max_length = 0

        if "" == s:
            return 0

        if len(s) == 1:
            return 1

        while p1 < len(s):
            char_dict = collections.defaultdict(int)
            char_dict[s[p1]] = p1

            for p2 in range(p1+1, len(s), 1):
                if p2 == len(s) - 1:
                    if char_dict[s[p2]] == 0:
                        char_dict[s[p2]] = p2
                    return max(max_length, len(char_dict))

                if char_dict[s[p2]] != 0:
                    p1 = char_dict[s[p2]] + 1
                    max_length = max(max_length, len(char_dict))
                    break
                else:
                    char_dict[s[p2]] = p2


print(Solution.lengthOfLongestSubstring(None, "au"))






