import collections


class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        graph = collections.defaultdict(collections.deque)
        none_node = collections.deque()
        if n == 1:
            return [0]

        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        leaves = []
        for i in range(n+1):
            if len(graph[i]) == 1:
                leaves.append(i)

        while n > 2:
            n -= len(leaves)

            new_leaves = []
            for leaf in leaves:
                near_node = graph[leaf].pop()
                graph[near_node].remove(leaf)

                if len(graph[near_node]) == 1:
                    new_leaves.append(near_node)

            leaves = new_leaves

        return leaves