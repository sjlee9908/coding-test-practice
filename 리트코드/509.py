class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        n1 = 0
        n2 = 1
        for _ in range(2, n+1):
            n3 = n1 + n2
            n1, n2 = n2, n3

        return n2


print(Solution.fib(None, 3))