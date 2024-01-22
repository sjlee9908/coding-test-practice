import collections
import sys

n = sys.stdin.readline()
stack = collections.deque()

for i in range(int(n)):
    command = sys.stdin.readline()
    command = command.split()
    if command[0] == "push":
        stack.append(int(command[1]))
    elif command[0] == "pop":
        print(-1) if len(stack) == 0 else print(stack.pop())
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        print(1) if len(stack) == 0 else print(0)
    elif command[0] == "top":
        print(-1) if len(stack) == 0 else print(stack[-1])

