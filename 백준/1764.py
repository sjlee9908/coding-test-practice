import sys

dont_see = set()
dont_listen = set()

n, m = map(int, input().split())

for i in range(n):
    dont_see.add(input())

for i in range(m):
    dont_listen.add(input())

dont_see_listen = sorted(list(dont_see & dont_listen))
print(len(dont_see_listen))
for i in dont_see_listen:
    print(i)
