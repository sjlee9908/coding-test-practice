import heapq

# input
n = int(input())

start_sort_heap = []
heapq.heapify(start_sort_heap)

for i in range(n):
    lec, start, end = map(int, input().split())
    heapq.heappush(start_sort_heap, (start, end))

# while start_sort_heap:
#     print(heapq.heappop(start_sort_heap))

# processing
end_sort_heap = []
heapq.heapify(end_sort_heap)

start, end = heapq.heappop(start_sort_heap)
heapq.heappush(end_sort_heap, (end, start))

while start_sort_heap:
    new_lec = heapq.heappop(start_sort_heap)
    now_lec = heapq.heappop(end_sort_heap)
    if new_lec[0] < now_lec[0]:
        start, end = new_lec
        heapq.heappush(end_sort_heap, (end, start))
        heapq.heappush(end_sort_heap, now_lec)
    else:
        start, end = new_lec
        heapq.heappush(end_sort_heap, (end, start))

# output
print(len(end_sort_heap))




