import collections

n, k = map(int, input().split(" "))

jewels = []
carry = []

for i in range(n):
    jewels.append(tuple(map(int, input().split(" "))))

for i in range(k):
    carry.append(int(input()))

jewels = collections.deque(sorted(jewels, key = lambda x:(-x[1], x[0])))
carry = collections.deque(sorted(carry))
print(jewels)
print(carry)

res = 0

now_carry = None
while True:
    if len(jewels) == 0 or (now_carry == None and len(carry) == 0):
        break

    if now_carry == None:
        now_carry = carry.popleft()
    now_jewels = jewels.popleft()
    print(now_jewels, now_carry)

    if now_jewels[0] <= now_carry:
        res += now_jewels[1]
        now_carry = None

print(res)
