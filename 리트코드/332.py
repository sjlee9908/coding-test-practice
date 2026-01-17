import collections
import heapq


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = collections.defaultdict(list)
        ans = []

        for from_loc, to_loc in tickets:
            heapq.heappush(graph[from_loc], to_loc)

        def dfs(now_loc):
            while graph[now_loc]:
                dfs(heapq.heappop(graph[now_loc]))
            ans.append(now_loc)

        dfs("JFK")
        return ans[::-1]


print(Solution.findItinerary(None, [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]))

