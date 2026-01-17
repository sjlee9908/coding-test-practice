#https://www.acmicpc.net/problem/23843
import heapq
import sys

#input
n, m = map(int, sys.stdin.readline().split())
t = list(map(lambda x: -int(x), input().split())) #max heap 구현을 위해 부호 반전

# processing
heapq.heapify(t) #heap 사용
consent = []
time = 0

#t가 비거나, 콘센트가 []가 아닐때까지
while t or consent != []:
    # m개 뽑음
    for i in range(m):
        # m개를 뽑는데, t가 비어있으면 못 뽑음 또 남은 콘센트가 없으면 못 뽑음
        if t and len(consent) < m:
            heapq.heappush(consent, -heapq.heappop(t))

    # 가장 작은 충전시간을 알고, 다시 삽입
    min_charge = 0
    if consent:
        min_charge = heapq.heappop(consent)
        heapq.heappush(consent, min_charge)

    #min_charge만큼 시간이 지남
    for i in range(len(consent)):
        consent[i] -= min_charge

    #min_charge만큼 시간 기록
    time += min_charge

    #0을 빼냄
    if consent:
        min_charge = heapq.heappop(consent)
    #consent가 비지 않았고, 0이 또 있는 경우 계속 빼냄
    while min_charge == 0 and consent:
        min_charge = heapq.heappop(consent)
    #0이 아닌 수를 빼내면, 다시 삽입
    if min_charge != 0:
        heapq.heappush(consent, min_charge)

#output
print(time)