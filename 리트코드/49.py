import collections


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        word_dict = collections.defaultdict(list)

        for word in strs:
            word_dict[str(sorted(word))].append(word)

        return list(word_dict.values())


#print(Solution.groupAnagrams(None, ["eat", "tea", "tan", "ate", "nat", "bat"]))
