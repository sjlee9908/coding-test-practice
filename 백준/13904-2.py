#input
import collections
import heapq

n = int(input())

report = []

for i in range(n):
    d, w = map(int, input().split())
    heapq.heappush(report, (-w, d))

#processing
to_do_report = collections.defaultdict(int)
while report:
    now_report = heapq.heappop(report)
    if to_do_report[now_report[1]] == 0:
        to_do_report[now_report[1]] = -now_report[0]
    else:
        remain_day = now_report[1]-1
        while remain_day != 0:
            if to_do_report[remain_day] == 0:
                to_do_report[remain_day] = -now_report[0]
                break
            else:
                remain_day -= 1

#output
print(sum(to_do_report.values()))
