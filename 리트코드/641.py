class MyCircularDeque:
    def __init__(self, k: int):
        self.max_size = k
        self.q = [None] * k
        self.front = 0
        self.rear = 1
        self.now_size = 0

    def insertFront(self, value: int) -> bool:
        if self.now_size >= self.max_size:
            return False
        self.now_size += 1
        self.q[self.front] = value
        self.front -= 1
        if self.front < 0:
            self.front += self.max_size
        return True

    def insertLast(self, value: int) -> bool:
        if self.now_size >= self.max_size:
            return False
        self.now_size += 1
        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.max_size
        return True

    def deleteFront(self) -> bool:
        if self.now_size == 0:
            return False
        self.now_size -= 1
        self.front = (self.front + 1) % self.max_size
        return True

    def deleteLast(self) -> bool:
        if self.now_size == 0:
            return False
        self.now_size -= 1
        self.rear -= 1
        if self.rear < 0:
            self.rear += self.max_size
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.front + 1) % self.max_size]


    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.rear - 1]

    def isEmpty(self) -> bool:
        return self.now_size == 0

    def isFull(self) -> bool:
        return self.max_size == self.now_size