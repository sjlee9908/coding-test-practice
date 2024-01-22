import heapq

n = int(input())
card_deck = []
heapq.heapify(card_deck)

for i in range(n):
    heapq.heappush(card_deck, int(input()))

res = 0

while len(card_deck) != 1:
    n1 = heapq.heappop(card_deck)
    n2 = heapq.heappop(card_deck)
    n3 = n1 + n2
    res = res + n3
    heapq.heappush(card_deck, n3)

print(res)