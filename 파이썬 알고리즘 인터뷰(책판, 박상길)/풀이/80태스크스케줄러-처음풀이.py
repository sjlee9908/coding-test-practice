import collections

class Solution:
    def leastInterval(self, tasks: list[str], n:int) -> int:
        counter = collections.Counter(tasks)
        res = 0
        c = 0
        print(counter)
        while True:
            mc = counter.most_common(n+1)
            print(mc)
            res += c
            c = 0
            for i in mc:
                if i[1] != 0:
                    res += 1
                    counter[i[0]] -= 1
                else:
                    c+=1
            if len(mc) < n+1:
                c += (n+1-len(mc))
            mc = counter.most_common(1)
            if mc[0][1] == 0:
                return res





print(Solution.leastInterval("as",["A","A","A","B","B","B"], n = 2))