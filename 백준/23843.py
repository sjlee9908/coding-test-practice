# input
import collections
import heapq

n, m = map(int, input().split())
t = list(map(lambda x: -int(x), input().split()))

#print(t)

# processing
heapq.heapify(t)
consent = []
time = 0

while t or consent != []:
    for i in range(m):
        if t and len(consent) < m:
            heapq.heappush(consent, -heapq.heappop(t))

    min_charge = 0
    if consent:
        min_charge = heapq.heappop(consent)
        heapq.heappush(consent, min_charge)

    for i in range(len(consent)):
        consent[i] -= min_charge

    time += min_charge

    if consent:
        min_charge = heapq.heappop(consent)
    while min_charge == 0 and consent:
        min_charge = heapq.heappop(consent)
    if min_charge != 0:
        heapq.heappush(consent, min_charge)

print(time)