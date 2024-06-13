class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        num = []
        letter = []
        for i in logs:
            flag = 0
            j = i.split(" ")
            for l in j:
                if l in "0123456789":
                    num.append(i)
                    flag = 1
                    break
            if flag == 0:
                letter.append(i)

        letter.sort(key = lambda x: (x.split()[1:], x.split()[0]))
        res = letter + num
        return res

lol = Solution()
lol.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])







