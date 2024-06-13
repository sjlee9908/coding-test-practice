class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dic = {}
        for word in strs:
            key = str("".join(sorted(word)))
            if key not in dic.keys():
                dic[key] = [word]
            else:
                dic[key].append(word)
        return list(dic.values())



lol = Solution()
lol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
