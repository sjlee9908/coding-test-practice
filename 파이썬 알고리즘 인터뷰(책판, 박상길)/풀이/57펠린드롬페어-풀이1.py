class Solution(object):
    def palindromePairs(self, words):
        def is_palindrome(word):
            return word == word[::-1]

        output = []
        for i, word1 in enumerate(words):
            for j,word2 in enumerate(words):
                if i == j:
                    continue
                if is_palindrome(word1 + word2):
                    output.append([i, j])
        return output

        