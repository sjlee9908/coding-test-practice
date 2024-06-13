import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()

        def dfs(i):
            if i in traced:
                return False
            traced.add(i)

            for y in graph[i]:
                if not dfs(y):
                    return False

            traced.remove(i)
            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True

