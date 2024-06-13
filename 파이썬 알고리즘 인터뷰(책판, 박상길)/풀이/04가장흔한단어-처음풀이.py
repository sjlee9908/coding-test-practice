import collections
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = paragraph.lower()
        paragraph_re = re.sub("[^\w]", " ", paragraph)
        paragraph_list = paragraph_re.split(" ")
        counter = dict(collections.Counter(paragraph_list))

        for i in banned:
            if i in counter:
                del counter[i]

        if " " in counter:
            del counter[" "]

        if "" in counter:
            del counter[""]

        print(counter)
        max_value = 0
        max_key = 0
        for k, v in counter.items():
            if(v > max_value):
                max_value = v
                max_key = k

        return max_key




lol = Solution()
print(lol.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["2345345"]))