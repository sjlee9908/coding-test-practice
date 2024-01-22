import collections


class MyQueue:
    def __init__(self): #lifo -> append, pop
        self.in_s = collections.deque()
        self.out_s = collections.deque()

    def push(self, x: int) -> None:
        self.in_s.append(x)

    def pop(self) -> int:
        self.peek()
        return self.out_s.pop()

    def peek(self) -> int:
        if len(self.out_s) == 0:
            while len(self.in_s) != 0:
                self.out_s.append(self.in_s.pop())
        return self.out_s[-1]

    def empty(self) -> bool:

        return len(self.out_s) == 0 and len(self.in_s) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()