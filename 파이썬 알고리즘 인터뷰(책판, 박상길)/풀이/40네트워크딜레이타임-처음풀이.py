class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        start_index = 0
        for i in times:
            if i[0] == k:
                break


