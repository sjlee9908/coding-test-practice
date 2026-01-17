# input
import collections
import itertools
import sys

belt = collections.deque()

n, d, k, c = map(int, input().split())
for i in range(n):
    belt.append(int(sys.stdin.readline()))

# process
max_eat = 0
eat_sushi = collections.defaultdict(int)
for i in itertools.islice(belt, 0, k):
    eat_sushi[i] += 1

for i in range(len(belt)):
    eat_belt = itertools.islice(belt, 0, k)
    if c not in eat_sushi.keys():
        max_eat = max(max_eat, len(eat_sushi) + 1)
    else:
        max_eat = max(max_eat, len(eat_sushi))

    #print(list(eat_belt))
    #print("before", eat_sushi)
    eat_sushi[belt[0]] -= 1
    if eat_sushi[belt[0]] == 0:
        del eat_sushi[belt[0]]
    eat_sushi[belt[k]] += 1
    #print("after", eat_sushi)

    belt.rotate(-1)

# output
print(max_eat)
