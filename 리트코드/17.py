def isPalindrome(s: str) -> bool:
    return s[::] == s[::-1]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ""
        length = len(s)

        for start in range(length):
            for end in range(length, start, -1):
                if isPalindrome(s[start:end]):
                    if len(palindrome) < len(s[start:end]):
                        palindrome = s[start:end]
                    break


        return palindrome


print(Solution.longestPalindrome(None, "cbbd"))
