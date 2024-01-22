import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        if not prerequisites:
            return True

        graph = collections.defaultdict(list)
        cycle = [False] * numCourses
        visited = [False] * numCourses

        for course in prerequisites:
            graph[course[0]].append(course[1])

        def dfs(now_node):
            if cycle[now_node]:
                return False

            if visited[now_node]:
                return True

            cycle[now_node] = True
            visited[now_node] = True

            for next_node in graph[now_node]:
                if not dfs(next_node):
                    return False

            cycle[now_node] = False
            return True

        for v in list(graph):
            if not dfs(v):
                return False

        return True


print(Solution.canFinish(None, numCourses=20,
                         prerequisites=[[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]))
