import collections
import re
from typing import Optional, Any


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> list[tuple[Optional[Any], int]]:
        paragraph = paragraph.lower()
        paragraph = re.sub(r'[^\w\s]',' ',paragraph)
        paragraph_words = list(map(lambda x: x if x not in banned else None, paragraph.split()))

        paragraph_counter = collections.Counter(paragraph_words)

        print(paragraph_counter)

        if paragraph_counter.most_common(1)[0][0] is None:
            return paragraph_counter.most_common(2)[1][0]
        else:
            return paragraph_counter.most_common(1)[0][0]



print(Solution.mostCommonWord(None, "a, a, a, a, b,b,b,c, c", ["a"]))

