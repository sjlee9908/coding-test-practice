import collections
import sys

n = sys.stdin.readline()
q = collections.deque()

for i in range(int(n)):
    command = sys.stdin.readline()
    command = command.split()
    if command[0] == "push":
        q.append(int(command[1]))
    elif command[0] == "pop":
        print(-1) if len(q) == 0 else print(q.popleft())
    elif command[0] == "size":
        print(len(q))
    elif command[0] == "empty":
        print(1) if len(q) == 0 else print(0)
    elif command[0] == "front":
        print(-1) if len(q) == 0 else print(q[0])
    elif command[0] == "back":
        print(-1) if len(q) == 0 else print(q[-1])

