import collections


class MyCircularQueue:
    def __init__(self, k: int):
        self.dq = collections.deque()
        self.size = k

    def enQueue(self, value: int) -> bool:
        if len(self.dq) == self.size:
            return False
        self.dq.append(value)
        return True

    def deQueue(self) -> bool:
        if len(self.dq) == 0:
            return False
        self.dq.popleft()
        return True

    def Front(self) -> int:
        if len(self.dq) == 0:
            return -1
        return self.dq[0]

    def Rear(self) -> int:
        if len(self.dq) == 0:
            return -1
        return self.dq[-1]

    def isEmpty(self) -> bool:
        if len(self.dq) == 0:
            return True
        return False

    def isFull(self) -> bool:
        if len(self.dq) == self.size:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()