import collections


class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()

        for bracket in s:
            if bracket in ['{', '[', '(']:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                open_brac = stack.pop()
                if open_brac + bracket not in ["()", "{}", "[]"]:
                    return False

        if len(stack) != 0:
            return False
        return True

