import collections
import heapq


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        task_book = collections.Counter(tasks)
        task_heap = []
        n += 1
        task_schd = [0] * (n)
        total_cycle = 0

        for key in task_book:
            heapq.heappush(task_heap, (-task_book[key], key))


        while task_heap != []:
            tv = 0
            for i in range(n):
                if task_heap == []:
                    break
                task = heapq.heappop(task_heap)
                task = (task[0] + 1, task[1])
                tv += 1
                if task[0] != 0:
                    task_schd[i] = task


            for i in range(n):
                if task_schd[i] != 0:
                    heapq.heappush(task_heap, task_schd[i])
                    task_schd[i] = 0

            if task_heap != []:
                total_cycle += n
            else:
                total_cycle += tv


        return total_cycle


