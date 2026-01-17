import collections


class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_dq = collections.deque()
        for i in s:
            if i.isalnum():
                char_dq.append(i.lower())
        while len(char_dq) > 1:
            if char_dq.popleft() != char_dq.pop():
                return False
        return True

print(Solution.isPalindrome(None, "A man, a plan, a canal: Panama"))

