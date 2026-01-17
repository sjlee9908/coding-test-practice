class MyCircularQueue:
    def __init__(self, k: int):
        self.max_size = k
        self.q = [0] * k
        self.front = 0
        self.rear = 0
        self.now_size = 0

    def enQueue(self, value: int) -> bool:
        if self.now_size >= self.max_size:
            return False
        self.now_size += 1
        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.max_size
        return True

    def deQueue(self) -> bool:
        if self.now_size == 0:
            return False
        self.now_size -= 1
        self.front = (self.front + 1) % self.max_size
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.rear - 1]

    def isEmpty(self) -> bool:
        return self.now_size == 0

    def isFull(self) -> bool:
        return self.max_size == self.now_size

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()