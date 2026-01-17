import collections


class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        let_log = []
        dit_log = collections.deque()

        for i in logs:
            if i.split()[1].isdigit():
                dit_log.append(i)
            else:
                let_log.append(i)

        let_log.sort(key=lambda x: (x.split()[1:], x.split()[:1]))
        return let_log+list(dit_log)


print(Solution.reorderLogFiles(None, ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))