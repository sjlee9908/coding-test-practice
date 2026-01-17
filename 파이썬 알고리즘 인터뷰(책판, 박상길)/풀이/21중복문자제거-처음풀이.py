class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        mapping_string = {}

        for i in range(0, len(s)):
            if s[i] not in mapping_string:
                mapping_string[s[i]] = [i]
            else:
                mapping_string[s[i]].append(i)

        mapping_alpha = sorted(mapping_string.items())
        print(mapping_alpha)

        marker = []

        for k, v in mapping_alpha:
            if len(v) == 1:
                marker.append(k)

        for k, v in mapping_alpha:
            if k in marker:
                v = int(v)
            else:
                v = [x for x in v if ]



sol = Solution()
sol.removeDuplicateLetters("cbacdcbc")


