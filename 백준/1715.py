import heapq

#input
n = int(input())
card_deck = []

for i in range(n):
    heapq.heappush(card_deck, int(input()))

#process
res = 0

while len(card_deck) != 1:
    #2개의 카드 뭉치를 뺌, 이 때 카드뭉치는 최소값이라는 게 보장됨
    n1 = heapq.heappop(card_deck)
    n2 = heapq.heappop(card_deck)
    #비교횟수 계산
    n3 = n1 + n2
    res = res + n3
    #새롭게 나온 카드뭉치를 heap에 저장
    heapq.heappush(card_deck, n3)

#출력
print(res)