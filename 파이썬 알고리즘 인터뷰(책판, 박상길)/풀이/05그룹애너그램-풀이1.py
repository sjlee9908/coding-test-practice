import collections


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = collections.defaultdict(list)
        for word in strs:
            anagrams["".join(sorted(word))].append(word)
        return list(anagrams.values())


a = ['cde', 'cfc', 'abc']
def fn(s):
    return s[0], s[-1]
scorted(a, key=fn)