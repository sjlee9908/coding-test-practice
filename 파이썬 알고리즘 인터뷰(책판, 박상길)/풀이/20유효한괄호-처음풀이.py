import collections

class Solution:
    def isValid(self, s: str) -> bool:
        dq = collections.deque()

        if s == "" :
            return True

        for c in s:
            if c in "[{(":
                dq.append(c)

            else:
                if len(dq) == 0:
                    return False
                if ( c == "}" and dq.pop() != "{"):
                    return False
                elif (c == "]" and dq.pop() != "["):
                    return False
                elif (c == ")" and dq.pop() != "("):
                    return False


        return len(dq) == 0

sol = Solution()
print(sol.isValid("()[]{}"))

