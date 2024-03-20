import heapq
import sys

n = int(sys.stdin.readline())
max_heap = [] # 중간보다 작은 것들
min_heap = [] # 중간보다 큰 것들

#초기 중간값, 어떤 값이든 들어오면 갱신됨
mid = 99999
for _ in range(n):
    #숫자 입력 받음
    num = int(sys.stdin.readline())

    #현재 들어온 값을 중간값과 비교해 min_heap, max_heap에 넣음
    if num <= mid:
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)

    #두 heap의 길이를 맞춰줌 -> 길이 차이가 난다면, 중간값이 갱신된 것
    #min_heap이 큰 경우, max_heap의 요소 1개 삽입
    if len(max_heap) < len(min_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))

    # max_heap이 큰 경우, min_heap의 요소 1개 삽입
    if len(max_heap) > len(min_heap) + 1: #min_heap에 중간값을 저장하기 때문에, +1
        heapq.heappush(min_heap, -heapq.heappop(max_heap))

    #출력
    mid = -heapq.heappop(max_heap)
    print(mid)
    heapq.heappush(max_heap, -mid)
