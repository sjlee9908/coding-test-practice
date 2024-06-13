import heapq

class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        heap = []

        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))

        res = []

        while heap:
            person = heapq.heappop(heap)
            res.insert(person[1], [-person[0], person[1]])

        return res
