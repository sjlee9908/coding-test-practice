import collections
import heapq


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        heapq.heapify(intervals)
        ans = collections.deque()

        while True:
            if len(ans) == 0:
                ans.append(heapq.heappop(intervals))
            else:
                new_section = heapq.heappop(intervals)
                old_section = ans[-1]

                if old_section[0] <= new_section[0] <= old_section[1]:
                    ans.pop()
                    ans.append([old_section[0], max(old_section[1], new_section[1])])
                else:
                    ans.append(new_section)
            if len(intervals) == 0:
                break

        return list(ans)

print(Solution.merge(None, intervals = [[1,4],[2,3]]))